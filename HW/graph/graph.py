"""
添加或删除边:直接在邻接矩阵中修改指定的边即可,无向需要同时更新两个边.
添加顶点:在邻接矩阵的尾部添加一行一列,并全部填0即可.
删除顶点:在邻接矩阵中删除一行一列。
初始化:
传入n个顶点,初始化长度为n的顶点列表vertices
初始化n^2大小的邻接矩阵 adjMat

"""

class GraphAdjMat :
    def __init__(self, vertices:list[int], edges:list[list[int]]):
        """构造方法"""
        #顶点列表:元素代表"顶点值" 索引代表"顶点索引"
        self.vertices: list[int] = []
        self.edges: list[list[int]] = []

    def size(self) -> int :
        """获取顶点数"""
        return len(self.vertices)

    