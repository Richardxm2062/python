import os
import subprocess
from docx import Document

ROOT_DIR = "/Users/richard/Documents/Physics/高中物理/1 资料/0 同步/0 JC/2[shk] 25-26同步/16 选修3/3 原子核/5 同步与复习讲义"
SOFFICE = "/Applications/LibreOffice.app/Contents/MacOS/soffice"


def convert_to_docx(input_path):
    """把兼容模式 doc 转成标准 docx"""
    subprocess.run([
        SOFFICE,
        "--headless",
        "--convert-to", "docx",
        input_path,
        "--outdir", os.path.dirname(input_path)
    ])


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
    ])


def process():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.startswith("~$"):
                continue

            if file.endswith(".docx"):
                file_path = os.path.join(root, file)

                print(f"处理: {file_path}")

                try:
                    # 1️⃣ 强制重新保存为标准 docx
                    convert_to_docx(file_path)

                    # 重新获取路径（LibreOffice可能覆盖）
                    new_path = file_path

                    # 2️⃣ 删除页眉
                    remove_headers(new_path)

                    # 3️⃣ 转 PDF
                    convert_to_pdf(new_path)

                except Exception as e:
                    print(f"❌ 失败: {file_path}")
                    print(e)


if __name__ == "__main__":
    process()