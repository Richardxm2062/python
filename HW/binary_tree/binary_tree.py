from typing import Union

class TreeNode :                                       #类声明必须放在main函数前，且被优先加载
    
    #二叉树类节点
    def __init__(self, val:int) :    
        self.val:int = val                             #节点值
        self.left : Union[TreeNode,None] = None        #Union[]使得属性可以是指定的类型或者None
        self.right: Union[TreeNode,None] = None

def creat_node() :
    
    #初始化二叉树-创建十个节点
    n1 = TreeNode(val = 1); n2 = TreeNode(val = 2); n3 = TreeNode(val = 3)
    n4 = TreeNode(val = 4); n5 = TreeNode(val = 5); n6 = TreeNode(val = 6)
    n7 = TreeNode(val = 7)

    #构建指针
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7

    return n1,n2,n3,n4,n5,n6,n7                         #必须返回






















