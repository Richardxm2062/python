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
    # 按单引号分割
    parts = s.split("'")

    # 取奇数位（真正路径）
    paths = [p.strip() for i, p in enumerate(parts) if i % 2 == 1]

    # 如果没有引号 → 按行解析
    if not paths:
        paths = [line.strip() for line in s.splitlines() if line.strip()]

    return paths


def natural_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def find_common_root(file_list):
    if not file_list:
        return None

    common = os.path.commonpath(file_list)

    if os.path.isfile(common):
        return os.path.dirname(common)

    return common


# ====== 提取章节名 & 类型名 ======

def extract_names(root_dir):
    parent = os.path.basename(os.path.dirname(root_dir))
    current = os.path.basename(root_dir)

    parent_name = re.sub(r'^\d+[-\d]*\s*', '', parent)
    current_name = re.sub(r'^\d+\s*', '', current)

    return parent_name, current_name


# ====== docx处理 ======

def process_docx_format(doc_path):
    doc = Document(doc_path)

    for section in doc.sections:
        for p in section.header.paragraphs:
            p.text = ""

        footer = section.footer
        for p in footer.paragraphs:
            p.text = ""

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

        # ⭐ 跳过 word 目录（关键）
        if os.path.basename(root) == "word":
            continue

        word_files = []

        for file in files:
            if file.startswith("~$"):
                continue

            if file.endswith(".docx"):
                file_path = os.path.join(root, file)
                print(f"[处理docx] {file_path}")

                try:
                    process_docx_format(file_path)
                    convert_to_pdf(file_path)
                    word_files.append(file_path)
                except Exception as e:
                    print(f"❌ docx失败: {file_path}")
                    print(e)

        if word_files:
            word_dir = os.path.join(root, "word")

            if not os.path.exists(word_dir):
                os.makedirs(word_dir)

            for file_path in word_files:
                filename = os.path.basename(file_path)
                target_path = os.path.join(word_dir, filename)

                if not os.path.exists(target_path):
                    os.rename(file_path, target_path)
                else:
                    print(f"⚠️ 已存在，跳过: {filename}")


# ====== PDF分类 ======

def collect_pdfs(root_dir):
    A, B = [], []

    for root, dirs, files in os.walk(root_dir):

        # ⭐ 跳过 word 目录
        if os.path.basename(root) == "word":
            continue

        for file in files:
            if not file.endswith(".pdf"):
                continue

            # ⭐ 跳过已经合并过的PDF
            if file.startswith("(") or "）(" in file:
                continue

            full_path = os.path.join(root, file)

            if "解析" in file:
                A.append(full_path)
            elif "原卷" in file:
                B.append(full_path)

    return A, B


# ====== PDF合并 ======

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


# ====== 主流程 ======

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

    parent_name, current_name = extract_names(root_dir)

    if A:
        out_dir_A = find_common_root(A)
        filename_A = f"{parent_name}({current_name})(解析).pdf"
        merge_pdfs(A, os.path.join(out_dir_A, filename_A))

    if B:
        out_dir_B = find_common_root(B)
        filename_B = f"{parent_name}({current_name})(原卷).pdf"
        merge_pdfs(B, os.path.join(out_dir_B, filename_B))

    print("✅ 完成")


# ====== ⭐ 判断是否是任务目录（修复版） ======

def has_target_files(dir_path):
    for f in os.listdir(dir_path):
        full_path = os.path.join(dir_path, f)

        # ⭐ 必须是文件（关键修复）
        if not os.path.isfile(full_path):
            continue

        if f.endswith(".docx") or f.endswith(".pdf"):
            return True

    return False


# ====== 主入口 ======

def main():
    print("请输入一个或多个路径：")
    user_input = input()

    paths = parse_input_paths(user_input)

    if not paths:
        print("❌ 未识别到路径")
        return

    for p in paths:
        if not os.path.exists(p):
            print(f"❌ 路径不存在: {p}")
            continue

        # ⭐ 如果是“章节目录”（名字像 运动学）
        # 才拆子目录
        if re.search(r'\d+\s*\S+', os.path.basename(p)) is None:
            subdirs = [
                os.path.join(p, d)
                for d in os.listdir(p)
                if os.path.isdir(os.path.join(p, d))
            ]

            if subdirs:
                print(f"\n检测到子目录，按子目录处理: {p}")
                for sub in subdirs:
                    process_one(sub)
                continue

        # ⭐ 默认：直接处理
        process_one(p)


if __name__ == "__main__":
    main()