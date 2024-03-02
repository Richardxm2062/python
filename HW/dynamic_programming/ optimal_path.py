"""
给定一个 n x m 的二维网格 grid ，网格中的每个单元格包含一个非负整数，表示该单元格的代价。
机器人以左上角单元格为起始点，每次只能向下或者向右移动一步，直至到达 右下角单元格。
请返回从左上角到右下角的最小代价路径的和
dp[i][j] = min{ dp[i][j-1], dp[i-1][j] } + cost_grid[i][j]
"""
"""
答案:
13
"""

"""动态规划搜索:从起点到终点"""
from turtle import left, right


def dynamic_search(cost_grid, dp = []) :
    x_len = len(cost_grid)
    y_len = len(cost_grid[0])
   
    dp =  [[0 for _ in range(y_len)] for _ in range(x_len)]

    #遍历整个dp表
    for i in range(x_len) :
        for j in range(y_len) :
            dp[i][j] = dynamic_solve(i,j,dp,cost_grid)          # type: ignore
            
    return dp

def dynamic_solve(x:int,y:int,dp,cost_grid):
    if dp[x][y] != 0 :                                          #已经求解过的值直接使用 避免重复求解子问题
        return dp[x][y]
    
    elif x < 0 or y < 0 :
        return 1000                                             #越界给一个比较大的损耗 会在min里被省去
    
    elif x ==0 and y == 0:
        return cost_grid[0][0]
    
    else : 
        val = min(dynamic_solve(x-1,y,dp,cost_grid),dynamic_solve(x,y-1,dp,cost_grid)) + cost_grid[x][y]
        return val 
    

"""暴力搜索:从终点到起点"""
#是一种穷尽所有路线的解法:从终点回头算
def violent_search (cost_grid) :
    #在搜索过程记录已经求过的dp
    x_len = len(cost_grid)
    y_len = len(cost_grid[0])
    
    dp =  [[0 for _ in range(y_len)] for _ in range(x_len)]
    val = violent_solve(x_len-1,y_len-1,cost_grid)
    
    return val

def violent_solve(x,y,cost_grid) :
    if x < 0 or y < 0 :                           #越界判断
        return 1000
    
    #到达左上角顶点停止
    elif x == 0  and y == 0 :
        return cost_grid[0][0]

    up_val = violent_solve(x-1,y,cost_grid) 
    left_val = violent_solve(x,y-1,cost_grid)
    return min(up_val,left_val) + cost_grid[x][y]
        
  
def main():
    cost_grid = [[1,3,1,5],[2,2,4,2],[5,3,2,1],[4,3,5,2]]
    
    res = dynamic_search(cost_grid)
    print("动态规划搜索的结果:{}".format(res[-1][-1]))
    
    res = violent_search(cost_grid)
    print("暴力搜索的结果:{}".format(res))    


if __name__ == "__main__" :
    main()