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
数量为9 行数为4。 则每列2个元素 显然2x4<9不够。 
1.找到最小列数
2.开始从外围填充 
填充优先级:
填充第一行 填充其他行的末尾元素 倒叙填充末尾行
"""
#输入个数,行数,列数
def solve(n, m, min) :
    #构建待填充元素列表
    out_list = [_ for _ in range(1,n+1)]    #原始个数[1,n]
    out_list = list(map(str, out_list))     #转化为字符串类型
    
    for _ in range(min*m - n) :             #待补充个数
        out_list.append('*')
    
    #构建输出矩阵 m*n大小 初始元素为 "0"
    out_mat = [['0' for _ in range(min)] for _ in range(m)]
    
    #重新填充输出矩阵
    
    





#找到最小列数
def find_min(n, m) :
    #min储存最小列
    min = 0
    for i in range(1,n+1) :
        if i*m < n :
            continue
        if i*m >= n :
            min = i
            #找到后跳出循环
            break
        
    return min 




def main() :
    in_list = list(map(int, input().split()))
    
    #字数个数[0,999]
    n = in_list[0]
    
    #行数(要求每行元素一样多)
    m = in_list[1]

    min = find_min(n, m)
    

if __name__ == "__main__" :
    main()