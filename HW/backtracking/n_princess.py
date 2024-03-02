"""
n x n大小的棋盘上放置 n 个皇后
皇后可以攻击同列、同行、正反对角线上的其他皇后
试问 n 个皇后互相不能攻击 的排列有多少种
约束: 多个皇后均互相不在同一行 同一列 正反对角线上
策略:
1.采用逐行放置  2.当前位置是否为允许位置 
3.放置皇后  4.判断当前当前放置数是否为n    5.为n:排列放入结果res (清空p_list)or 通过当前放置的位置更新np_list
np_list最好使用set 以免重复
"""
from typing import Optional

#主体第1行的循环
def solve(n, choice:Optional[list[list[int]]] = None, np_list:list[list[int]] = [], res = []) :
    #初始化
    if choice == None : 
        choice = []
        
    for lp in range(n) :
        choice.append([0,lp])                          #填充当第一行
        np_list = permission(n,choice,np_list)         #依据当前的选择 添加不允许填充的坐标
        row_pointer = 1
        permutation(n, row_pointer, choice, np_list)   #执行后续行的试探排列
        choice.pop()                                   #回退第一行后清除第一行的填充
        row_pointer -= 1 
        np_list = permission(n,choice,np_list)
    
    return res 

def permutation(n:int, row_pointer:int = 1, choice = [], np_list = [], res = []) :
    """某一层执行试探排列"""
    
    #子树的终止条件
    if row_pointer >= n :
        #选择了4个坐标则为一种方案
        if len(choice) == 4 :           
            res.append(choice.copy())
        return res
    
    #将该层继续视为主体 行指针row_pointer
    for lp in range(n) :
        if [row_pointer,lp] not in np_list :
            #填充并更新Np_list
            choice.append([row_pointer,lp])
            np_list = permission(n,choice,np_list) 
            #递归到下一层
            row_pointer += 1
            permutation(n, row_pointer, choice, np_list) 
            #删除元素开始回溯
            choice.pop()        
            #np_list也需要回溯       
            np_list = permission(n,choice,np_list) 
            #行指针也要回退
            row_pointer -= 1                             
    
    return res


#permission 不允许被放置的坐标 
def permission(n, choice, np_list:list[list[int]]):
    for position in choice :
        rowp = position[0]
        lp = position[1]
        #当前行每个位置都不被允许
        for i in range(n) :
            if [rowp,i] not in np_list :
                np_list.append([rowp,i]) 
        #当前列的每个位置都不被允许
        for j in range(n) : 
            if [j,lp] not in np_list :
                np_list.append([j,lp])
        #寻找正反对角线
        #寻找左上角
        for i in range(n*n) :     #一个很大的搜索循环 while不好用 判断在每个循环的开始
            rowp -= 1
            lp -= 1 
            if rowp in range(n) and lp in range(n):     #都在范围内
                if [rowp,lp] not in np_list :
                    np_list.append([rowp,lp])
            else :        
                rowp = position[0]
                lp = position[1]                        #任意一个不在 跳出回位
                break
            
        #寻找左下角
        for i in range(n*n) :     
            rowp += 1
            lp -= 1 
            if rowp in range(n) and lp in range(n):     
                if [rowp,lp] not in np_list :
                    np_list.append([rowp,lp])
            else :                  
                rowp = position[0]
                lp = position[1]                    
                break
            
        #寻找右上角
        for i in range(n*n) :     
            rowp -= 1
            lp += 1 
            if rowp in range(n) and lp in range(n):     
                if [rowp,lp] not in np_list :
                    np_list.append([rowp,lp])
            else :   
                rowp = position[0]
                lp = position[1]                                    
                break
            
        #寻找右下角
        for i in range(n*n) :     
            rowp += 1
            lp += 1 
            if rowp in range(n) and lp in range(n):     
                if [rowp,lp] not in np_list :
                    np_list.append([rowp,lp])
            else :   
                rowp = position[0]
                lp = position[1]                                    
                break
        
    return np_list


def main() :
    n = int(input("输入皇后个数(>3):"))
    res = solve(n)
    print(res)


if __name__ == "__main__" :
    main()