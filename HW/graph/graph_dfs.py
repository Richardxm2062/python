"""
深度优先遍历是一种优先走到底、无路可走再回头的遍历方式。
这种“走到尽头再返回”的算法范式通常基于递归来实现.
仍旧需要一个哈希表 visited 来储存走过的顶点
"""

from GraphAdj import GraphAdjList, Vertex 

"""dfs通常是递归,所以需要传递的参数比bfs更多"""
"""多次输入例子,默认参数只会被使用,因此在函数定义时设置默认参数为可变对象
（例如空列表 [] 或空集合 set()）时，会导致这个可变对象在多次调用中被共享和修改。"""
def dfs(graph:GraphAdjList, point:Vertex , visited = None, res = None):
    """None是无法赋值给set[Vertex] list[Vertex],因此直接赋值None"""
    if visited is None:
        visited = set[Vertex]()
    if res is None:
        res  = list[Vertex]()

    res.append(point)  
    visited.add(point)                                  #记录访问过的节点
    
    for adj_vertex in graph.adj_list[point] :
        
        if adj_vertex in visited :
            continue
        
        else :
            dfs(graph, adj_vertex, visited, res)                                         
           
    return res


def main() :
    mat_list1 = [[1,3],[0,2,4],[1,5],[0,4,6],[1,3,5,7],[2,4,8],[3,7],[4,6,8],[5,7]]
    graph1 = GraphAdjList(mat_list1)
    start_vertex1 = graph1.vertices[0]
    res1 = graph1.vex_val(dfs(graph1,start_vertex1))
    print(res1,"\n")
    """答案为[0,1,2,5,4,3,6,7,8]"""
    
    
    mat_list2 = [[1,3],[0,2],[1,5],[0],[5],[2,4,6],[5]]
    graph2 = GraphAdjList(mat_list2)
    start_vertex2 = graph2.vertices[0]
    res2 = graph2.vex_val(dfs(graph2,start_vertex2))
    print(res2)
    """答案为[0,1,2,5,4,6,3]"""


if __name__ == "__main__":
    main()