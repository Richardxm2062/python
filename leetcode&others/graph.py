"""图-链表
"""

from time import sleep


class Vertex :
    def __init__(self, name, value) :
        self.name = name
        self.val = value
        

class GraphAdjList :
    def __init__(self, vex_name, values, mat_list) :    #输入为顶点名字列表 对应值 关系矩阵
        #顶点列表属性 邻接表
        self.vertices : list[Vertex] = []
        self.adj_mat = {}

        """处理输入"""
        #1.将 vex_name, values 转化为 Vertex对象储存为属性
        self.vertices = self.to_vertex(vex_name, values)
        
        #2.构造邻接表 将mat_list 每一行从self.vertices找到对应 作为边添加
        for i,edge in enumerate(mat_list) :
            self.adj_mat[self.vertices[i]] = self.add_edge(vex_name, edge)
        

    def to_vertex(self , vex_name, values) :
         
        return [Vertex(vex_name[i], values[i]) for i in range(len(vex_name))]
        

    def add_edge(self, vex_name, edge) :
        
        return [self.vertices[vex_name.index(ele)] for ele in edge]
    
    
    def del_vertex(self, tar) :
        for vex in self.vertices :
            if vex.name == tar :
                del_vex = vex
        
        for ele in self.adj_mat[del_vex] :                           #对应的边
            self.adj_mat[ele].remove(del_vex)                        #删除邻接边包含的此顶点
        self.adj_mat.pop(del_vex)
        self.vertices.remove(del_vex)
        
        
    def add_vertex(self, tar_name, tar_val, rl):                       #rl为与其他的关系表
        add_vex = Vertex(tar_name, tar_val)
        self.vertices.append(add_vex)   
        self.adj_mat[add_vex] = []
        for ele in rl :
            for vex in self.vertices :
                if ele == vex.name :
                    self.adj_mat[vex].append(add_vex)               #邻边添加新顶点
                    self.adj_mat[add_vex].append(vex)               #新顶点添加边
         
        
    def pt(self):
        for keys,values in self.adj_mat.items() :
            print(keys.name,[ele.name for ele in values ])
            

        

def main() :
    vex_name = ['A','B','C','D','E','F']
    values = [3,5,6,1,2,7,8]
    mat_list = [['B','C'],['A','C','F'],['A','B','D','E'],['C'],['C','F'],['B','E']]
    graph_list = GraphAdjList(vex_name, values, mat_list)
    print("邻接表为=")
    graph_list.pt()
    print("删除顶点\'F\'")
    graph_list.del_vertex('F')
    graph_list.pt()
    print("添加顶点\'F\'")
    graph_list.add_vertex('F', 8, ['B','E'])
    graph_list.pt()


if __name__ == "__main__" :
    main()