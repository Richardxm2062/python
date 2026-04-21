import os
import re
from pypdf import PdfReader, PdfWriter


# ====== 解析输入路径 ======

def parse_input_paths():
    print("请输入路径（支持多路径）：")
    print("方式1：'/路径1' '/路径2'")
    print("方式2：多行粘贴\n")

    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except EOFError:
            break

    text = "\n".join(lines)

    # 优先匹配 '路径'
    paths = re.findall(r"'([^']+)'", text)

    # 如果没有引号 → 按行读取
    if not paths:
        paths = [line.strip() for line in lines if line.strip()]

    return paths


# ====== 排序 ======

def natural_key(s):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r'(\d+)', s)]


# ====== 收集PDF ======

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


# ====== 合并 ======

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

def process_one(root_dir):
    if not os.path.exists(root_dir):
        print(f"❌ 路径不存在: {root_dir}")
        return

    print(f"\n=== 处理: {root_dir} ===")

    A, B = collect_pdfs(root_dir)

    A.sort(key=lambda x: natural_key(os.path.basename(x)))
    B.sort(key=lambda x: natural_key(os.path.basename(x)))

    print(f"解析数量: {len(A)}")
    print(f"原卷数量: {len(B)}")

    if A:
        merge_pdfs(A, os.path.join(root_dir, "(解析).pdf"))
    if B:
        merge_pdfs(B, os.path.join(root_dir, "(原卷).pdf"))

    print("✅ 完成")


def main():
    paths = parse_input_paths()

    if not paths:
        print("❌ 未识别路径")
        return

    for p in paths:
        process_one(p)


if __name__ == "__main__":
    main()