"""
广度优先算法 
使用队列deque完成:先进先出
为了防止重复遍历顶点，我们需要借助一个哈希表 visited 来记录哪些节点已被访问。
"""

from collections import deque
from GraphAdj import GraphAdjList,Vertex


"""
使用的是邻接表(矩阵的遍历非常简单)
"""

def bfs(graph:GraphAdjList, start_vertex:int) :
    res = []        #顶点遍历序列



def main() :
    mat_list = [[1,2],[0,3,5],[0,3,4],[1,2,4,5],[2,3],[1,3]]
    graph = GraphAdjList(mat_list)
