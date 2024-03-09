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
    
    #按坐标进行填充 
    x_start = 0
    y_start = 0
    
    #两个控制方向的变量
    directions = [0,1,0,-1,0]
    dir = 0
    
    #控制轮次的变量 即确定剩下的矩阵形状
    ct = 0
    
    #重新填充输出矩阵
    while out_list :                            #只要out_list非空 将会持续执行
        out_mat[x_start][y_start] = out_list[0]
        out_list.pop(0)
        
        #持续循环直到一个合法的坐标出现
        while True :
            new_x = x_start + directions[dir]
            new_y = y_start + directions[dir+1]
            
            #判断当前坐标是否 合法
            per = permission(new_x, new_y, row, col, out_mat, ct)
            #当前坐标允许 跳出
            if  per == 1 :
                break 
            
            elif  per == 0 :
                #因为越界不合法 转向继续
                dir += 1
                continue
            
            elif per == -1 :
                #达到一个轮次 重置
                #给出下轮循环的状态跳出
                ct += 1
                row -= 2*ct
                col -= 2*ct
                dir = 0 
                new_x,new_y = x_start,y_start+1
                break
        
        #接受这个新坐标 继续循环填充
        x_start,y_start = new_x,new_y       

    return out_mat


def permission (x, y, row, col, out_mat, ct) :
    #未达到边界 且当前元素未填充
    if x in range(ct,row+ct) and y in range(ct,col+ct) and out_mat[x][y] == '*' :
        return 1
    
    #因为超出边界而非法
    elif  x not in range(ct,row+ct) or y not in range(ct,col+ct) :
        return 0
        
    #在边界内 但达到一轮填充次数
    elif x in range(ct,row+ct) and y in range(ct,col+ct) and out_mat[x][y] != '*' : 
        return -1
        
    
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