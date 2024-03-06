"""题目
n种重量互不相等的砝码[1,10]  val[i]重量[1,2000] 每种砝码的num[j]数量[1,10]
这些砝码称重 共有多少种种不同的重量组合 (包括 0)
"""

"""思路
输入n val num 不重复的重量列表res 
根据元素被选次数choice 构造当前循环层的 可选砝码重量列表 val 
循坏遍历该层 查看是否允许被选择(num 中值是否为0) 不允许 continue 
选择某元素  减次数(num中元素值-1)
计算现在的 总重 是否重复出现在 res
递归到下一层
终止条件:num 中的所有元素为 0(需要all函数)
返回层中总重量每层值不一样是 自动回溯的
num 列表中的 值需要回溯
"""

"""暴力搜索:超时严重(递归太深)"""
def violent_solve(val, num, res = {0}, wg = 0, pointer = 0) :        #默认值加0
    #终止条件(不加pointer可以不写)
    if all(ele == 0 for ele in num) :
        pointer += 1
        return res,pointer
    
    for i,j in enumerate(val[pointer:]) :       #i为索引值 j为重量
        if num[i] != 0 :                        #可以被选取
            wg += j
            num[i] -= 1                         #无论是否在结果列表都应该减次数
            res.add(wg) 
            
            #递归层
            violent_solve(val, num, res, wg)    
            
            #回溯层
            num [i] += 1                    #可选次数回溯
            wg -= j                         #总重回溯 
                
        else :
            continue                            #当前元素不可被选跳过循环         
               
    return res
    
    """
    不要在循环内的回溯层直接return
    在函数尾部 return 能保证顶层的循环不被跳出
    """

"""速度更快"""
def solve(val, num, res = {0}, ls=[]) :
    #直接将所有的砝码放在一个列表里
    for i,j in enumerate(num) :
        for c in range(j) :
            ls.append(val[i])
    #这样则不需要多次深层递归 嵌套循环即可
    """res 作为不重复的历史总重 并不断向上面添加砝码"""
    for i in ls :
        for j in list(res) :                    #res在每次重新放砝码后 会更新
            res.add(i+j)                        #添加并去重

    return res


def main():
    #处理输入
    n = int(input())
    val = list(map(int,input().split()))
    num = list(map(int,input().split()))
    #res = violent_solve(val, num)
    #print(res)
    #print(len(res))
    res2 = solve(val, num)
    print(len(res2))
    

if __name__ == "__main__" :
    main()