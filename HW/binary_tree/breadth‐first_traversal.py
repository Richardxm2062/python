"""
层序遍历 (breath-firt traversal)

广度优先遵循逐层推进
通常借助 队列 deque (先进先出) 来实现。

deque时collections里的一个类(双端队列)
a = deque()     #初始化
a.append()      #尾添加
a.appendleft()  #左添加
a.pop()         #尾删除
a.popleft()     #左删除

"""
from collections import deque
from typing import Union
from binary_tree import TreeNode,creat_node


def main () :
    n1,n2,n3,n4,n5,n6,n7 = creat_node()

    #bft遍历
    Node_Val = bft(n1)
    print(Node_Val)


def bft(root : Union[TreeNode,None] ) -> list[int] :
    res = []                                      #初始化一个空列表用于储存遍历节点的值
    if  root == None :
        return res                                #根节点为空时返回空列表
    
    else:
        arr : deque[TreeNode] = deque()           #初始化一个元素为TreeNode的双端列表(deque类型),类似于 A : List[int] = []
        arr.append(root)                          #根节点加入双端队列
    
    while arr :                                   #非空则重复执行(空列表,字典,元组都是False,数值类0是False),在循环内为空并不会立刻终止代码
        node : TreeNode = arr.popleft()           #队列出列,并返回这个节点,或者 = arr[0] 然后再删除元素(先进先出)
        res.append(node.val)
        if node.left is not None :
            arr.append(node.left)                 #左子节点非空,加入arr,while循环继续执行
        if node.right is not None :
            arr.append(node.right)                #左子节点非空,加入arr,while循环继续执行
    return res

    """
    在这两个判断里很好的体现了广度优先搜索,当为root节点的下一层时
    子节点的下两个子节点都为非空,队列arr会出现两个新节点[2,3],弹出节点2加入子节点4,5
    得到[3,4,5],以次进行弹出仍旧是上一层的节点3。由此进行层遍历
    

    """

if __name__ == "__main__" :
    main()



