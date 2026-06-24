import os
import shutil

# =========================================================
# 功能说明
# =========================================================
#
# 用于恢复 WordtoPDF(Merge).py 运行前状态
#
# 功能：
#
# 1. 查找所有 word 文件夹
# 2. 将 word 内的 docx 移回上一层目录
# 3. 删除空 word 文件夹
# 4. 删除所有 pdf 文件
#
# =========================================================


def restore_word_files(root_dir):

    restore_count = 0
    delete_pdf_count = 0

    # =====================================================
    # 第一步：恢复 Word 文件
    # =====================================================

    for root, dirs, files in os.walk(root_dir):

        if os.path.basename(root) != "word":
            continue

        parent_dir = os.path.dirname(root)

        print("\n--------------------------------")
        print(f"发现 word 文件夹：")
        print(root)
        print("--------------------------------")

        for file in files:

            if not file.endswith(".docx"):
                continue

            src = os.path.join(root, file)
            dst = os.path.join(parent_dir, file)

            try:

                shutil.move(src, dst)

                restore_count += 1

                print(f"恢复 Word：{file}")

            except Exception as e:

                print(f"恢复失败：{file}")
                print(e)

        try:

            os.rmdir(root)

            print("删除空 word 文件夹")

        except:

            pass

    # =====================================================
    # 第二步：删除所有 PDF
    # =====================================================

    for root, dirs, files in os.walk(root_dir):

        for file in files:

            if not file.endswith(".pdf"):
                continue

            pdf_path = os.path.join(root, file)

            try:

                os.remove(pdf_path)

                delete_pdf_count += 1

                print(f"删除 PDF：{file}")

            except Exception as e:

                print(f"删除失败：{file}")
                print(e)

    # =====================================================
    # 统计
    # =====================================================

    print("\n================================")
    print("恢复完成")
    print(f"恢复 Word 数量：{restore_count}")
    print(f"删除 PDF 数量：{delete_pdf_count}")
    print("================================")


# =========================================================
# 主入口
# =========================================================

def main():

    print("请输入需要恢复的目录路径：")

    root_dir = input().strip()

    root_dir = root_dir.strip("'").strip('"')

    if not os.path.exists(root_dir):

        print("❌ 路径不存在")

        return

    restore_word_files(root_dir)


if __name__ == "__main__":

    main()