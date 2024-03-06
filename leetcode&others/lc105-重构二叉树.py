"""题目
通过前、中序遍历结果重构二叉树结构
"""

"""思路
前序: 根|左子树|右子树      中序:左子树|根|右子树|
前序第一个元素为 根节点。 根节点在中序中 得到左、右子树的长度
因此在前序 可将数组 按个数 划分,再利用前序数组重构
"""


from turtle import right
from typing import Optional


class TreeNode :
    def __init__(self,val):
        self.val = val
        self.left = Optional[TreeNode]
        self.left = Optional[TreeNode]
        
        
def ReCreate_TreeNode (preres, inres, left_len = None, right_len = None) :
    if left_len == None :
        left_len,right_len = divide_preres(preres, inres)       
    
    


def divide_preres(preres, inres) :
    root_node = preres[0]                           #根节点元素
    root_node_index = inres.index(root_node)        #中序数组根节点元素索引值
    #左右长度
    left_len = inres[:root_node_index]              
    right_len = inres[:root_node_index]
    
    return left_len,right_len
    
def main() :
    preres = list(map(int,input().split()))
    inres = list(map(int,input().split()))
    ReCreate_TreeNode(preres,inres)


if __name__ == "__main__" :
    main()        