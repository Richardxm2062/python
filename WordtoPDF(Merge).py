import os
import re
import subprocess
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from pypdf import PdfReader, PdfWriter

SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"


# ====== 工具 ======

def parse_input_paths(s):
    paths = re.findall(r"'([^']+)'", s)
    if not paths:
        paths = [line.strip() for line in s.splitlines() if line.strip()]
    return paths


def natural_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def find_common_root(file_list):
    if not file_list:
        return None
    return os.path.commonpath(file_list)


# ====== docx处理（保留页眉页脚逻辑） ======

def process_docx_format(doc_path):
    doc = Document(doc_path)

    for section in doc.sections:
        # 删除页眉
        for p in section.header.paragraphs:
            p.text = ""

        # 清空页脚
        footer = section.footer
        for p in footer.paragraphs:
            p.text = ""

        # 添加页码
        p = footer.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        run = p.add_run()

        fldChar1 = OxmlElement('w:fldChar')
        fldChar1.set(qn('w:fldCharType'), 'begin')

        instrText = OxmlElement('w:instrText')
        instrText.set(qn('xml:space'), 'preserve')
        instrText.text = "PAGE"

        fldChar2 = OxmlElement('w:fldChar')
        fldChar2.set(qn('w:fldCharType'), 'end')

        run._r.append(fldChar1)
        run._r.append(instrText)
        run._r.append(fldChar2)

    doc.save(doc_path)


def convert_to_pdf(doc_path):
    subprocess.run([
        SOFFICE,
        "--headless",
        "--convert-to", "pdf",
        doc_path,
        "--outdir", os.path.dirname(doc_path)
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def process_docx(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.startswith("~$"):
                continue
            if file.endswith(".docx"):
                file_path = os.path.join(root, file)
                print(f"[处理docx] {file_path}")

                try:
                    process_docx_format(file_path)
                    convert_to_pdf(file_path)
                except Exception as e:
                    print(f"❌ docx失败: {file_path}")
                    print(e)


# ====== PDF分类 ======

def collect_pdfs(root_dir):
    A, B = [], []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)

                if "解析" in file:
                    A.append(full_path)
                elif "原卷" in file:
                    B.append(full_path)

    return A, B


# ====== PDF合并（带书签） ======

def merge_pdfs(file_list, output_path):
    writer = PdfWriter()
    current_page = 0

    for f in file_list:
        name = os.path.basename(f)
        print(f"[合并] {name}")

        try:
            reader = PdfReader(f)
        except:
            print(f"❌ 跳过损坏文件: {f}")
            continue

        num_pages = len(reader.pages)

        title = name.replace(".pdf", "")
        title = title.replace("（解析版）", "").replace("（原卷版）", "")

        writer.add_outline_item(title, current_page)

        for page in reader.pages:
            writer.add_page(page)

        current_page += num_pages

    with open(output_path, "wb") as f:
        writer.write(f)


# ====== 单路径流程 ======

def process_one(root_dir):
    if not os.path.exists(root_dir):
        print(f"❌ 路径不存在: {root_dir}")
        return

    print("\n==============================")
    print(f"处理路径: {root_dir}")
    print("==============================")

    process_docx(root_dir)

    A, B = collect_pdfs(root_dir)

    A.sort(key=lambda x: natural_key(os.path.basename(x)))
    B.sort(key=lambda x: natural_key(os.path.basename(x)))

    print(f"解析数量: {len(A)}")
    print(f"原卷数量: {len(B)}")

    # ⭐ 修复输出路径
    if A:
        out_dir_A = find_common_root(A)
        merge_pdfs(A, os.path.join(out_dir_A, "(解析).pdf"))

    if B:
        out_dir_B = find_common_root(B)
        merge_pdfs(B, os.path.join(out_dir_B, "(原卷).pdf"))

    print("✅ 完成")


# ====== 主入口 ======

def main():
    print("请输入一个或多个路径：")
    user_input = input()

    paths = parse_input_paths(user_input)

    if not paths:
        print("❌ 未识别到路径")
        return

    for p in paths:
        process_one(p)


if __name__ == "__main__":
    main()