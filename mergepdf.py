import os
import re
from pypdf import PdfReader, PdfWriter

ROOT_DIR = "/Users/richard/Documents/Physics/高中物理/1 资料/0 同步/0 JC/2[shk] 25-26同步/16 选修3/3 原子核/5 同步与复习讲义"  # ← 改这里


def natural_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


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


def merge_pdfs(file_list, output_path):
    writer = PdfWriter()

    for f in file_list:
        reader = PdfReader(f)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)


def main():
    A, B = collect_pdfs(ROOT_DIR)

    A.sort(key=lambda x: natural_key(os.path.basename(x)))
    B.sort(key=lambda x: natural_key(os.path.basename(x)))

    print(f"解析数量: {len(A)}")
    print(f"原卷数量: {len(B)}")

    output_A = os.path.join(ROOT_DIR, "解析.pdf")
    output_B = os.path.join(ROOT_DIR, "原卷.pdf")

    if A:
        print("合并解析...")
        merge_pdfs(A, output_A)

    if B:
        print("合并原卷...")
        merge_pdfs(B, output_B)

    print("完成")


if __name__ == "__main__":
    main()