"""题目
疫情期间,小明隔离在家,百无聊赖,在纸上写数字玩。他发明了一种写法：
给出数字个数n和行数m(0 < n ≤ 999,0 < m ≤ 999)   
从左上角的1开始,按照顺时针螺旋向内写方式,依次写出2,3...n,最终形成一个m行矩阵。
小明对这个矩阵有些要求：
1.每行数字的个数一样多
2.列的数量尽可能少
3.填充数字时优先填充外部
4.数字不够时,使用单个*号占位
"""

"""思路
模拟蚂蚁移动进行填充
首行填充时 行坐标不变 纵坐标+1  [0,+1]
竖向填充时 纵坐标不变 行坐标+1  [+1,0]
尾行填充时 行坐标不变 纵坐标-1  [0,-1]
竖向填充时 纵坐标不变 行坐标-1  [-1,0]
得到控制方向的 列表 [0,1,0,-1,0] (这个是难点)
"""

#输入个数,行数,列数
def solve(n, row, col) :
    #构建待填充元素列表
    out_list = [_ for _ in range(1,n+1)]        #原始个数[1,n]
    out_list = list(map(str, out_list))         #转化为字符串类型
    
    #构建输出矩阵 m*n大小 初始元素为 "*"
    out_mat = [['*' for _ in range(col)] for _ in range(row)]
    
    #控制轮次的变量 即确定剩下的矩阵形状
    ct = 0
    
    #剩余待填充元素指标
    p = 1
    
    #索引偏移量
    ct = 0
    
    
    
    #循环填充
    while True :
        p = add(row, col, , out_list, p)
        if p == 1 :
            #一轮填充结束
            ct += 1
            row -= 2*ct
            col -= 2*ct
        else :
            break

    return out_mat
    
def permission (out_list) :
    if out_list == [] :
        return 0
    
    else :
        return 1
    
#填充函数    
def add(row, col, mat, out_list, p):
    #首行填充
    for i in range(col) :
        mat[0][i] = out_list[0]
        out_list.pop(0)
        p = permission(out_list)
        if p == 0 :         #填充完毕 立刻停止
            return p 
        
    #中行升序填充
        for ele in mat[1:row] :
            ele[-1] = out_list[0]
            out_list.pop(0)
            p = permission(out_list)
            if p == 0 :         #填充完毕 立刻停止
                return p 
                
    #尾行倒序填充
    for i in range(col-1, -1, -1) :
        mat[-1][i] = out_list[0]
        out_list.pop(0)
        p = permission(out_list)
        if p == 0 :         #填充完毕 立刻停止
            return p 
        
    #中行降序填充
    for ele in mat[row-1:0:-1] :
        ele[0] = out_list[0]
        out_list.pop(0)
        p = permission(out_list)
        if p == 0 :         #填充完毕 立刻停止
            return p

    
     
#找到最小列数
def find_col(n, row) :
    #col储存最小列
    col = 0
    for i in range(1,n+1) :
        if i*row < n :
            continue
        if i*row >= n :
            col = i
            #找到后跳出循环
            break
        
    return col 


def main() :
    in_list = list(map(int, input().split()))
    
    #字数个数[0,999]
    n = in_list[0]
    
    #行数(要求每行元素一样多)
    row = in_list[1]

    col = find_col(n, row)
    
    res = solve(n, row, col)
    for i,j in enumerate(res) :
        print(' '.join(j))
    

if __name__ == "__main__" :
    main()