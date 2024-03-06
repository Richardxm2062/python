"""子集问题
寻找一个整数数组的所有子集合
"""
from typing import Any, Optional

#需要当前数组,以及index,结果res
def subset(arr:list[int], start_p:int, res = None) -> Optional[list[Any]] : #   使用any类型 是因为res作为二维列表包含空集合
    """arr数组  start_p当前起点 res二维结果列表"""
    if res == None :
        res = [[]]
    
    length = len(arr)                   #总长度        
    ele : list[int] = []                #初始化遍历数组
    if start_p >= length :              #终止条件
        return res                      #这里只返回了最右子树,必须总返回
    
    """遍历当前节点及子叶节点"""
    for i in range(length-start_p) :    #length-start_p为当前子树剩余元素
        ele.append(arr[i+start_p])      #正确索引为 0+起点索引
        res.append(ele.copy())          #向列表中添加列表,必须添加副本(引用问题)
    
    start_p += 1                        #指向下一个子树
    subset(arr,start_p,res)             
    
    return res                          #递归必须在尾部返回一下,某子树返回是不够的
   
def main() :
    arr = [1,2,3,4,5]                         
    res = subset(arr,0)
    print(res)


if __name__ == "__main__":
    main()