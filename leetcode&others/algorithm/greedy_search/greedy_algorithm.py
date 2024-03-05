"""
给定 n 个硬币 面值分别为 val[i] 目标金额为 tar
求解 凑出目标金额的最小硬币数量 如果无法凑出返回 -1
贪心算法: 从目标金额尽可能的贪心(取最大面值)回溯
n = 6 val = [1,5,10,20,50,100] tar = 131
答案 chocie = [1,10,20,100] 共计4个硬币
"""

"""贪心算法在每次局部决策都做出最优解 但并不能保证是全局最优解"""

#n硬币数量 val硬币面值列表 tar目标金额 choice选择列表
def greedy_search(n, val, tar, choice = None, level_p = None) : 
    if choice == None :
        level_p = n-1
        choice = []
    
    greedy_solve(n, val, tar, choice, level_p)
    
    return choice


def greedy_solve(n, val, tar, choice ,level_p) :
   """贪心算法并不适合使用递归法"""
   """最好使用while进行"""
   
   for i in range(n-1, -1, -1) :
        
        if val[i] <= tar :
            choice.append(val[i])
            tar -= val[i]
            level_p -= 1
            greedy_solve(n, val, tar, choice,level_p)
            return choice
            
        #两个终止情况: 1.凑整了 2.凑到tar的值已经比val所有的值小 切不为0
        else:
            if tar < val[0] and tar != 0 :
                return choice
            
            if tar == 0 :
                return choice 
            
            continue


def main() :
    tar = int(input("请输入目标金额:"))
    n = int(input("请输入硬币数量:"))
    val = list(map(int,input("输入对应的硬币面值,空格分隔:").split()))
    val.sort()
    choice = greedy_search(n, val, tar)
    #根据返回的choice和判断是否凑完了
    if sum(choice) != tar :
        print("无法找到")
    else:
        print("\n","最小硬币数量为{}".format(len(choice)),"\n","选取的硬币面值分别是:","\n","{}".format(choice))


if __name__ == "__main__" :
    main()