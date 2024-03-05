class GraphAdjList:
    def __init__(self, vertices: list[int], adj_mat: list[list[int]]):
        # 创建顶点对象列表
        self.vertices: list[Vertex] = [Vertex(val) for val in vertices]
        
        # 将邻接矩阵中的索引映射为顶点对象
        self.adj_mat: list[list[Vertex]] = []
        for row in adj_mat:
            vertex_row = [self.vertices[idx] for idx in row]
            self.adj_mat.append(vertex_row)

class Vertex:
    def __init__(self, val: int):
        self.val = val

# 示例用法
vertices = [1, 2, 3]
adj_mat = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]

graph = GraphAdjList(vertices, adj_mat)

# 打印顶点列表
print([vertex.val for vertex in graph.vertices])

# 打印邻接矩阵
for row in graph.adj_mat:
    print([vertex.val for vertex in row])
