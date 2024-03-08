"""题目
查找节点值为7的所有节点,并输出找到每个7的路径,并要求路径中不包含节点"3"
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from binary_tree import binary_tree_list
from typing import Optional

def dfs (root:Optional[binary_tree_list.TreeNode],  path:list[Optional[str]], res:list[list[Optional[str]]], val:int) :
    """现将当前节点加入path"""

    if root == None :
        return
    
    """根节点->左子树->右子树"""
    """res返回达到值为7的所有路径 path记录当前路径"""
    if root is not None :
        if root.name != '3' :
            path.append(root.name)
            if root.val == val :
                res.append(list(path))                  #这里必须保存path列表的副本，可以使用copy()
        else :
            return
            
    dfs(root.left,path,res,val)
    dfs(root.right,path,res,val)
    
    path.pop()                                          #当达到子叶节点时,左右都为None,返回到该层时回退路径

    return res
    

def main() :
    """节点2 4 7 8 的节点值为7"""
    #构建节点
    n1 = binary_tree_list.TreeNode(4,"1") ; n2 = binary_tree_list.TreeNode(7,"2")
    n3 = binary_tree_list.TreeNode(3,"3") ; n4 = binary_tree_list.TreeNode(7,"4")
    n5 = binary_tree_list.TreeNode(1,"5") ; n6 = binary_tree_list.TreeNode(2,"6")
    n7 = binary_tree_list.TreeNode(7,"7") ; n8 = binary_tree_list.TreeNode(7,"8")
    
    #构建指针
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    n5.left = n8
    res = dfs(n1,[],[],7)
    """[['1', '2'], ['1', '2', '4'], ['1', '2', '5', '8']]"""
    print(res)


if __name__ == "__main__" :
    main()