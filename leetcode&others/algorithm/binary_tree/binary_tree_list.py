"""链表二叉树
"""

from typing import Optional

class TreeNode :                                                #类声明必须放在main函数前，且被优先加载
    
    #二叉树类节点
    def __init__(self, val:Optional[int] = None , name:Optional[str] = None) :  
        self.val = val                                          #节点值
        self.name = name
        self.left : Optional[TreeNode] = None                   #Union[]使得属性可以是指定的类型或者None
        self.right : Optional[TreeNode] = None

def creat_node() :
    
    #初始化二叉树-创建七个节点
    n1 = TreeNode(1,"1"); n2 = TreeNode(2,"2"); n3 = TreeNode(3,"3")
    n4 = TreeNode(4,"4"); n5 = TreeNode(5,"5"); n6 = TreeNode(6,"6")
    n7 = TreeNode(7,"7"); 

    #构建指针
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7

    return n1,n2,n3,n4,n5,n6,n7                         #必须返回
