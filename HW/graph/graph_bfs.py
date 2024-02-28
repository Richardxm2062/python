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
    visited : set[Vertex] = set([start_vertex])                 #历史顶点set类
    que : deque[Vertex] = deque()                               #双端队列
    
    que.append(start_vertex)
    
    """直到找不到顶点加入队列结束"""
    while len(que) > 0 :
        vet = que.popleft()                                     #出队(已在队列中则表明没有访问过可以加入res)
        res.append(vet)
        for ele in graph.adj_list[vet] :                        #ele是list[Vertex]
            if ele in visited :
                continue
            
            else :
                que.append(ele)                                 #未被访问过 入队
                visited.add(ele)                                #加入访问过的列表
    return graph.vex_val(res)


def main() :
    mat_list1 = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
    graph1 = GraphAdjList(mat_list1)
    res1 = bfs(graph1,0)
    print(res1)
    """答案为[0,1,3,2,4,6,5,7,8]"""

    mat_list2 = [[1,3],[0,2],[1,5],[0],[5],[2,4,6],[5]]
    graph2 = GraphAdjList(mat_list2)
    res2 = bfs(graph2,0)
    print(res2)
    """答案为[0,1,3,2,5,4,6]"""

if __name__ == "__main__" :
    main()