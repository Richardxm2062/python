"""
添加或删除边:直接在邻接矩阵中修改指定的边即可,无向需要同时更新两个边.
添加顶点:在邻接矩阵的尾部添加一行一列,并全部填0即可.
删除顶点:在邻接矩阵中删除一行一列。
初始化:
传入n个顶点,初始化长度为n的顶点列表vertices
初始化n^2大小的邻接矩阵 adjMat

"""

"""使用邻接矩阵 表示图"""
class GraphAdjMat :
   
    def __init__(self, vertices:list[int], adj_mat:list[list[int]]):
        """构造方法"""
        #顶点列表:元素代表"顶点值" 索引代表"顶点索引"
        self.vertices: list[int] = vertices                              #参数与属性同名,但参数的值并不会自动传递给该属性
        self.adj_mat: list[list[int]] = adj_mat
        

    def size(self) -> int :
        """获取顶点数"""
        return len(self.vertices)                                   #d大小属性是动态变化的,不建议设置为属性
    
    def add_vertex(self, var:int) : 
        #仅仅添加顶点
        self.vertices.append(var)
        return self.vertices

    """扩充邻接矩阵"""
    def add_mat(self, var:int) :    
        #添加顶点
        self.add_vertex(var)                         
        length = self.size()        
        #添加行     
        self.adj_mat.append([0]*(length-1))                         #需要先添加行
        #添加列
        for row in self.adj_mat :                               #在每一行后面加一个元素达到添加列的效果
            row.append(0)
        
    """删除顶点与邻接矩阵对应的行列"""
    def del_mat(self, index:int) :
        self.vertices.pop(index)
        """删除索引值对应的行与列"""
        self.adj_mat.pop(index)                                 #删除二维列表的行
        for row in self.adj_mat :
            row.pop(index)

    def pt(self) :
        print("邻接矩阵 = ")
        print("******",self.vertices,"\n")
        for i,vex in enumerate(self.vertices) :
            print(vex," -> ",self.adj_mat[i])
            


    """
    如果需要在二维列表中查找某个值的索引,enumerate()函数用于在迭代过程中同时获得行索引和行内容
    for i,row in enumerate(list)
    """

"""
为了方便添加与删除顶点，以及简化代码，我们使用列表(动态数组)来代替链表。
使用哈希表来存储邻接表,key 为顶点实例,value 为该顶点的邻接顶点列表(链表)。
顶点实例化,使用Vertex类,这样不再通过索引删除
P193
"""

"""顶点实例化,需要放在前面"""
class Vertex :
    def __init__(self, val:int) :
        self.val = val


"""使用邻接表 表示图"""
class GraphAdjList : 
    def __init__(self, vertices:list[int], adj_mat:list[list[int]]) : 
        self.vertices : list[Vertex] = list(map(Vertex,vertices))           #顶点列表
        self.adj_mat : list[list[Vertex]] =[]                               #对应矩阵
        
        for row in adj_mat :                                                
            self.adj_mat.append(list(map(Vertex,row)))
        
        self.adj_list : dict[Vertex,list[Vertex]] = {}                      #链表:每个顶点->邻接顶点列表

        for i,v in enumerate(self.vertices) :
            self.adj_list[v] = self.adj_mat[i]

    def size(self) :
        return len(self.vertices)


    def add_vertex(self, val:int) :
        vex = Vertex(val)
        if vex in self.vertices :
            return
        else :
            self.vertices.append(vex) 
        
    def add_mat(self) :
        return
    
    def pt(self):
        """打印邻接表"""
        print(" 邻接表 =")
        for i in range(self.size()):
            print(self.vertices[i].val," -> ",[ v.val for v in self.adj_mat[i] ])


if __name__ == "__main__" :
    vertices_arr = [0,1,2,3,4,5]
    mat_arr = [[0,1,1,1,0,0],[1,0,1,0,1,1],[1,0,0,1,1,0],[0,1,1,0,1,1],[0,0,1,1,0,0],[0,1,0,1,0,0]]
    graph_arr = GraphAdjMat(vertices_arr,mat_arr)
    print("矩阵实现")
    graph_arr.add_mat(6)
    graph_arr.pt()

    vertices_list = [0,1,2,3,4,5]          
    mat_list = [[1,2],[0,3,5],[0,3,4],[1,2,4,5],[2,3],[1,3]]
    print("链表实现")
    graph_list = GraphAdjList(vertices_list,mat_list)
    graph_list.pt()
