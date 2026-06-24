# =========================================================
# 功能说明
# =========================================================
#
# 输入：
#
# 1. 待分类目录
#
#    例如：
#
#    /Users/richard/Downloads/静电场及其应用
#
#
# 2. 目标目录
#
#    例如：
#
#    /Users/richard/Documents/Physics/高中物理
#
#
# 程序会扫描待分类目录下的所有一级文件夹，
# 根据关键词自动移动到目标目录对应分类中。
#
#
# 匹配优先级：
#
# 知识清单
# ↓
# 单元测试
# ↓
# 讲义
# ↓
# 专项
# ↓
# 专题
# ↓
# 重难点训练
# ↓
# 分层作业
#
#
# 匹配成功立即移动，不再继续判断。
#
# =========================================================

import os
import shutil

RULES = [

    ("知识清单", "7 知识清单"),

    ("单元测试", "6 综合测试"),
    ("周周练", "6 综合测试"),

    ("专项", "4 专项与专项练习"),

    ("专题", "3 模型与方法"),

    ("讲义", "5 同步与复习讲义"),

    ("重难点训练", "2 重难点训练"),

    ("分层作业", "1 分层作业"),

]


def classify_folder(folder_name):

    for keyword, target in RULES:

        if keyword in folder_name:
            return target

    return None


def main():

    print("请输入待分类目录：")
    source_dir = input().strip().strip("'").strip('"')

    print("请输入目标目录：")
    target_root = input().strip().strip("'").strip('"')

    if not os.path.isdir(source_dir):

        print("❌ 待分类目录不存在")
        return

    if not os.path.isdir(target_root):

        print("❌ 目标目录不存在")
        return

    moved_count = 0

    for name in os.listdir(source_dir):

        source_path = os.path.join(source_dir, name)

        if not os.path.isdir(source_path):
            continue

        target_category = classify_folder(name)

        if target_category is None:

            print(f"⚠️ 未匹配: {name}")
            continue

        category_dir = os.path.join(
            target_root,
            target_category
        )

        os.makedirs(category_dir, exist_ok=True)

        target_path = os.path.join(
            category_dir,
            name
        )

        if os.path.exists(target_path):

            print(f"⚠️ 已存在，跳过: {name}")
            continue

        shutil.move(
            source_path,
            target_path
        )

        moved_count += 1

        print(
            f"✅ {name}"
            f" -> "
            f"{target_category}"
        )

    print()
    print(f"完成，共移动 {moved_count} 个文件夹")


if __name__ == "__main__":

    main()