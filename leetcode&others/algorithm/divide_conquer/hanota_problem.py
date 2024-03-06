"""汉诺塔分治问题
将f(n)问题分解为两个子问题的合并:f(n) = f(n-1) + f(1)
1. 将n-1个圆盘借助C从A移至B。 
2. 将剩余1个圆盘从A直接移至C。
3. 将n-1个圆盘借助A从B移至C。
"""


def solve(n:int, src:list[int], buffer:list[int], tar:list[int] ) :
    """src原列表 buffer缓冲列表 tar目的地列表"""
    
    """已知解f(1) A->C """
    if n == 1 :
        mv(src,tar)
        return  
    
    """未知解f(n-1)将 n-1个 借助C从A->B"""
    #该层递归将被执行完后才会继续执行后续,因此相当于移动n-1后再继续操作
    solve(n-1,src,tar,buffer)
    
    """剩余一个圆盘直接移动"""
    mv(src,tar)
    
    """未知解f(n-1)将 n-1 个借助A 从B->C"""
    solve(n-1,buffer,src,tar)
    
    return src,buffer,tar


def mv(src:list[int], tar:list[int]) :
    """在柱子之间移动"""
    tar.append(src.pop())                             #顶端推出与加入

def main(): 
    hanota = [6,5,4,3,2,1]                            #从大到小适合pop append
    print("初始三柱子为 : ")
    print([hanota,[],[]],"\n")
    res = solve(len(hanota),hanota,[],[])
    print("移动后 : ")
    print(res)
    

if __name__ == "__main__":
    main()