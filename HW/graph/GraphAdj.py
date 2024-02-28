"""
添加或删除边:直接在邻接矩阵中修改指定的边即可,无向需要同时更新两个边.
添加顶点:在邻接矩阵的尾部添加一行一列,并全部填0即可.
删除顶点:在邻接矩阵中删除一行一列。
初始化:
传入n个顶点,初始化长度为n的顶点列表vertices
初始化n^2大小的邻接矩阵 adjMat

"""

"""使用邻接矩阵 表示图"""
from multiprocessing import set_forkserver_preload
from operator import ne
from re import S


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
"""

"""顶点实例化,需要放在前面"""
"""实力化后顶点将可以有更多属性"""
"""除非是一个引用,否则同等大小的 val:int 转化的Vertex对象依旧是不同一个"""
class Vertex :
    def __init__(self, val:int) :
        self.val = val


"""使用邻接表 表示图"""
class GraphAdjList : 
    def __init__(self, edges:list[list[int]]) : 
        self.vertices : list[Vertex] = []
        self.adj_list : dict[Vertex, list[Vertex]] = {}
        ls = []
        for i,edge in enumerate(edges) :
            self.vertices.append(Vertex(i)) 
            self.adj_list[self.vertices[i]] = self.val_vex(edge)               #将顶点和边转化为Vertex类并添加到字典
                                        

    def val_vex(self, vals:list[int]) :
        """输入列表[int] 返回列表[Vertex]"""
        return [ Vertex(ele) for ele in vals ]
    
    def vex_val(self, vertices:list[Vertex]) :
        """输入列表[Vertex] 返回列表[int] """
        return [ ele.val for ele in vertices ] 
    
    def size(self) :
        return len(self.vertices)
        
    """输入顶点和边"""
    def add_edge(self, vertex:int, edge :list[int]) :
        new_vex = Vertex(vertex)
        self.vertices.append(new_vex)

        new_edge = [self.vertices[i] for i in edge]                      #这里不能使用val_vex将输入的列表转化为Vertex对象
        self.adj_list[new_vex] = new_edge
        
        """这里必须使用self.vertices的索引进行查找或者添加"""
        """尽管Vertex(3)中3的值一样,但是对于不同来源的3,仍旧不会是同一个对象"""
        
        """在其他边添加新顶点"""
        for ele in edge :
            self.adj_list[self.vertices[ele]].append(new_vex)          

    def del_edge(self, vertex:int) :
        del_edge = self.adj_list[self.vertices[vertex]]         #顶点值对应的关系列表[2,3,5](Vertex对象)
        self.adj_list.pop(self.vertices[vertex])                #删除键值对
        """删除关邻边"""
        for ele in del_edge :           
            self.adj_list[ele].remove(self.vertices[vertex])    #这里ele元素来自新边转为[Vertex],里面的所有旧顶点必须来自self.vertices
        self.vertices.pop(vertex)

    def pt(self) :
        print(" 邻接表 =")
        len = self.size()
        for i in range(len) :
            print(i," -> ",[ j.val for j in self.adj_list[self.vertices[i]]] )


if __name__ == "__main__" :
    vertices_arr = [0,1,2,3,4,5]
    mat_arr = [[0,1,1,1,0,0],[1,0,1,0,1,1],[1,0,0,1,1,0],[0,1,1,0,1,1],[0,0,1,1,0,0],[0,1,0,1,0,0]]
    graph_arr = GraphAdjMat(vertices_arr,mat_arr)
    print("矩阵实现")
    graph_arr.add_mat(6)
    graph_arr.del_mat(6)
    graph_arr.pt()
         
    mat_list = [[1,2],[0,3,5],[0,3,4],[1,2,4,5],[2,3],[1,3]]
    print("\n","链表实现")
    graph_list = GraphAdjList(mat_list)
    print("\n","添加顶点6,关系[2,3,5]")
    graph_list.add_edge(6,[2,3,5])
    graph_list.pt()
    print("\n","再次删除顶点6,和关邻边")
    graph_list.del_edge(6)
    graph_list.pt()
