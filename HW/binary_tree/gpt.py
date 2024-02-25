from collections import deque
from typing import Union
from unittest import result 
from binary_tree import TreeNode


def bft(root: Union[TreeNode, None]) -> list[int]:
    result = []  # 创建一个列表，用于存储遍历结果

    if root is None:
        return result  # 如果根节点为空，则直接返回空列表

    # 初始化队列，用于广度优先搜索
    queue = [root]

    while queue:
        node = queue.pop(0)  # 弹出队列的第一个节点
        result.append(node.val)  # 将节点值添加到结果列表中

        # 将节点的子节点添加到队列中
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result  # 返回遍历结果列表
