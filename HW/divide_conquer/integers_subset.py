"""
寻找一个整数数组的所有子集合
"""
from typing import Optional

#需要当前数组,以及index,结果res
def subset(arr:list[int], start_p:int, res = [[]])  :
    """arr数组  start_p当前起点"""
    
    length = len(arr)                   #总长度        
    ele : list[int] = []                #初始化遍历数组
    if start_p > length :               #终止条件
        return res
    
    """遍历当前节点及子叶节点"""
    for i in range(length-start_p-1) :    #length-start_p为当前子树剩余元素
        ele.append(arr[i+start_p])      #正确索引为 0+起点索引
        res.apend(ele)
    start_p += 1                        #指向下一个子树
    subset(arr,start_p,res)             
   
   
def main() :
    arr = [1,2,3,4,5]
    res = []
    res = subset(arr,0)
    print(res)


if __name__ == "__main__":
    main()