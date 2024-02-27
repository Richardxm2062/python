"""
广度优先算法 
使用队列deque完成:先进先出
为了防止重复遍历顶点，我们需要借助一个哈希表 visited 来记录哪些节点已被访问。
"""

from collections import deque
from GraphAdj import GraphAdjMat


"""
使用的是邻接表(矩阵的遍历非常简单)
"""

def bfs(graph:GraphAdjMat, start_vertex:int) :
    res = []        #顶点遍历序列



def main() :
    vertices = [0,1,2,3,4,5]
    adj_mat = [[0,1,1,1,0,0],[1,0,1,0,1,1],[1,0,0,1,1,0],[0,1,1,0,1,1],[0,0,1,1,0,0],[0,1,0,1,0,0]]
    graph = GraphAdjMat(vertices,adj_mat)
