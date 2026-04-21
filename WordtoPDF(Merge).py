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


# ====== docx处理（核心升级） ======

def process_docx_format(doc_path):
    doc = Document(doc_path)

    for section in doc.sections:
        # ===== 删除页眉 =====
        for p in section.header.paragraphs:
            p.text = ""

        # ===== 清空页脚 =====
        footer = section.footer
        for p in footer.paragraphs:
            p.text = ""

        # ===== 插入页码（居中） =====
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
    for root, dirs, files in os.walk(root_dir):
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
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)
                if "解析" in file:
                    A.append(full_path)
                elif "原卷" in file:
                    B.append(full_path)
    return A, B


# ====== PDF合并 ======

def merge_pdfs(file_list, output_path):
    writer = PdfWriter()

    for f in file_list:
        print(f"[合并] {os.path.basename(f)}")
        reader = PdfReader(f)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)


# ====== 单路径流程 ======

def process_one(root_dir):
    if not os.path.exists(root_dir):
        print(f"❌ 路径不存在: {root_dir}")
        return

    print(f"\n==============================")
    print(f"处理路径: {root_dir}")
    print(f"==============================")

    # 1️⃣ docx处理
    process_docx(root_dir)

    # 2️⃣ 收集PDF
    A, B = collect_pdfs(root_dir)

    A.sort(key=lambda x: natural_key(os.path.basename(x)))
    B.sort(key=lambda x: natural_key(os.path.basename(x)))

    print(f"解析数量: {len(A)}")
    print(f"原卷数量: {len(B)}")

    # 3️⃣ 合并
    if A:
        merge_pdfs(A, os.path.join(root_dir, "(解析).pdf"))
    if B:
        merge_pdfs(B, os.path.join(root_dir, "(原卷).pdf"))

    print("✅ 完成")


# ====== 主入口 ======

def main():
    print("请输入一个或多个路径（支持复制多个）：")
    user_input = input()

    paths = parse_input_paths(user_input)

    if not paths:
        print("❌ 未识别到路径")
        return

    for p in paths:
        process_one(p)


if __name__ == "__main__":
    main()