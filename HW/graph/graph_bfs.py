"""
广度优先算法 
使用队列deque完成:先进先出

1. 将遍历起始顶点 startVet 加入队列，并开启循环。
2. 在循环的每轮迭代中，弹出队首顶点并记录访问，然后将该顶点的所有邻接顶点加入到队列尾部。 
3. 循环步骤 2. 直到所有顶点被访问完毕后结束。
为了防止重复遍历顶点，我们需要借助一个哈希表 visited (set类) 来记录哪些节点已被访问。
"""

from collections import deque
from GraphAdj import GraphAdjList,Vertex


"""
使用的是邻接表(矩阵的遍历非常简单)
"""

def bfs(graph:GraphAdjList, start_point:int) :
    res = []                                                    #顶点遍历序列
    start_vertex = graph.vertices[start_point]                  #Vertex起点顶点
    visited = set[Vertex]([start_vertex])


def main() :
    mat_list = [[1,2],[0,3,5],[0,3,4],[1,2,4,5],[2,3],[1,3]]
    graph = GraphAdjList(mat_list)




if __name__ == "__main__" :
    main()