"""
深度优先搜索(depth-fist travserval)
前序、中序、后序遍历都属于递归实现,反复调用自身直到走到尽头
先走到一边的尽头,回溯继续(围绕树的外围走一圈)

"""

from collections import deque
from binary_tree import TreeNode,creat_node
from typing import Union


def main () :
    n1,n2,n3,n4,n5,n6,n7 = creat_node()

    #初始化储存列表
    res = []
    #请选择某一序执行
    pre_oder(n1,res)
    print("前序深度搜索:",res)
    res= []
    in_oder(n1,res)
    print("中序深度搜索:",res)
    res = []
    post_oder(n1,res)
    print("后序深度搜索:",res)
    


#前序
def pre_oder(root:Union[TreeNode,None],res:list[int]) -> list[int] :
    #访问优先级 根节点->左子树->右子树
    if root is None : 
        return res
    else :
        #下面三行的顺序决定了 遍历序
        res.append(root.val)            #储存当前根节点值,因此优先级最高
        pre_oder(root.left,res)         #递归左子树,优先级为次
        pre_oder(root.right,res)        
        return res


#中序
def in_oder(root:Union[TreeNode,None],res:list[int]) -> list[int] :
    #访问优先级 左子树->根节点->右子树
    if root is None : 
        return res
    else :
        #下面三行的顺序决定了 遍历序
        in_oder(root.left,res)          #优先递归左子树,搜索到左子树的叶节点再回溯,优先级最高
        res.append(root.val)            #储存当前根节点值,因此优先级为次
        in_oder(root.right,res)        
        return res
    
#后序
def post_oder(root:Union[TreeNode,None],res:list[int]) -> list[int] :
    #访问优先级 右子树->根节点->左子树
    if root is None : 
        return res
    else :
        #下面三行的顺序决定了 遍历序
        post_oder(root.right,res)       #优先递右子树,搜索到右子树的叶节点再回溯,优先级最高
        res.append(root.val)            #储存当前根节点值,因此优先级为次
        post_oder(root.left,res)        
        return res
    

if __name__ =="__main__" :
    main()