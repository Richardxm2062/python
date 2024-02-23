"""
动态规划: 01 背包问题

有一个背包可以装物品的总重量为c
现有N个物品,物品w[i],价值v[i]
用背包装物品,能装的最大价值是多少
(每个物品只允许被用一次,因此有最优子问题)

dp[i][j]:将前i的物体放入容量为j的背包 所获得得最大价值 V

考虑放入第i个物品的情况
I. w[i]>j 即物品大于当前j背包容易 那么 dp[i][j] = dp[i-1][j]    (继承前i-1个物品所获得的最大价值)

II. w[i]<j 即可以选择放入背包
    1.放入 : dp[i][j] = dp[i-1][j-w[i]] + v[i]  (部分继承放入前i-1个物品 且容量为 j-w[i]的最大值)
    2.不放入 : dp[i][c] = dp[i-1][c]   
通过以上两种大情况(三种小类)实际得到了 两个dp值,取最大的一个 
dp[i][j] = max{ dp[i-1][c]  dp[i-1][j-w[i]]  }
(所有的值都为整数)
eg.
ct = 5 ; num = 3 ;wg = [1,2,3] ; val = [60,100,120] ;  
最大价值220 物品组合[2,3]

"""

def main() :
    
    ct = int(input("输入背包最大容量:"))
    num = int(input("输入物品个数:"))
    #保持wg val dp对于同一个物品的索引一致性也不能去在索引0的位置添加一个0
    wg = []
    val = []
    
    for i in range(num) :
        lt = list(map(int,(input("质量从小到大依次输入 质量与价值 用空格分开:").split())))
        wg.append(lt[0])
        val.append(lt[1])
    
    solve(ct,num,wg,val)



def solve(ct,num,wg,val) :
    
    #创建一个初始化的二维列表,表示为前i个物品容量为j的情况下的最大价值
    dp = [[0 for _ in range(ct+1)] for _ in range(num+1)]
    
    #前往后遍历进行填表,(为了防止i-1的边界问题创建二维数组的时候均高了一维)
    for i in range(1,num+1) : 
        for j in range(1,ct+1) :
            #当前物品重量大于当前容量
            if wg[i-1] > j :
                dp[i][j] = dp[i-1][j]   #继承i-1的值
            else :
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-wg[i-1]] + val[i-1])        
    
    #最大出现的位置一定会在表格的最右下角(最大背包容量),但并非仅仅在右下角出现
    #于是我们需要用回溯算法找到正确的物品组合
    trace(dp,ct,num)
    
def trace (dp,ct,num):
    for i in range(num+1,1,-1) :
        
        continue




if __name__ == "__main__" :
    main()