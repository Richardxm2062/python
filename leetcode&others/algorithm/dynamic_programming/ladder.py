""""
共有 n 阶的楼梯,每次上升1步or2步
但不能连续两轮跳 1 阶，请问有多 少种方案可以爬到楼顶?
dp[n] = dp[n-1] + dp[n-2]
由于无后效性消失,与之前的状态有关因此:
1. dp[n][2] = dp[n-2][1] + dp[n-2][2]
2. dp[n][1] = dp[n-1][2]

"""

def dp_solve(n, dp = None) :
    #初始化dp[n][1] or dp[n][2] 
    if dp == None :
        dp = [[0]*3 for _ in range(n+1)]      #行索引为[0,n]  列索引为[0,1,2]
        dp[1][1] = 1
        dp[2][1] = 0
        dp[2][2] = 1 

        
    for i in range(3,n+1) :
            dp[i][1] = dp[i-1][2]
            dp[i][2] = dp[i-2][1] + dp[i-2][2]
    
    res = dp[i][1] + dp[i][2]
    
    return res 


def main() :
    n = int(input("输入阶梯数:"))
    res = dp_solve(n)
    print(res)
    

if __name__ == "__main__":
    main()