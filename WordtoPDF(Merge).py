import os
import re
import subprocess
from docx import Document
from pypdf import PdfReader, PdfWriter

# LibreOffice 路径（固定）
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"


# ====== 工具函数 ======

def clean_input_path(path):
    """去掉 mac 复制路径两侧的单引号"""
    path = path.strip()
    if path.startswith("'") and path.endswith("'"):
        path = path[1:-1]
    return path


def natural_key(s):
    """按数字排序"""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


# ====== 第一步：docx → 删除页眉 → 转 PDF ======

def remove_headers(doc_path):
    doc = Document(doc_path)
    for section in doc.sections:
        for p in section.header.paragraphs:
            p.text = ""
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
                print(f"[转换] {file_path}")

                try:
                    remove_headers(file_path)
                    convert_to_pdf(file_path)
                except Exception as e:
                    print(f"❌ docx处理失败: {file_path}")
                    print(e)


# ====== 第二步：分类 PDF ======

def collect_pdfs(root_dir):
    A = []  # 解析
    B = []  # 原卷

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)

                if "解析" in file:
                    A.append(full_path)
                elif "原卷" in file:
                    B.append(full_path)

    return A, B


# ====== 第三步：合并 PDF ======

def merge_pdfs(file_list, output_path):
    writer = PdfWriter()

    for f in file_list:
        print(f"[合并] {os.path.basename(f)}")
        reader = PdfReader(f)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)


# ====== 主流程 ======

def main():
    # 1️⃣ 输入路径
    input_path = input("请输入文件夹路径：\n")
    root_dir = clean_input_path(input_path)

    if not os.path.exists(root_dir):
        print("❌ 路径不存在")
        return

    print("\n====== 第一步：docx → PDF ======")
    process_docx(root_dir)

    print("\n====== 第二步：收集 PDF ======")
    A, B = collect_pdfs(root_dir)

    A.sort(key=lambda x: natural_key(os.path.basename(x)))
    B.sort(key=lambda x: natural_key(os.path.basename(x)))

    print(f"解析数量: {len(A)}")
    print(f"原卷数量: {len(B)}")

    print("\n====== 第三步：合并 ======")

    if A:
        output_A = os.path.join(root_dir, "(解析).pdf")
        merge_pdfs(A, output_A)

    if B:
        output_B = os.path.join(root_dir, "(原卷).pdf")
        merge_pdfs(B, output_B)

    print("\n✅ 全部完成")


if __name__ == "__main__":
    main()