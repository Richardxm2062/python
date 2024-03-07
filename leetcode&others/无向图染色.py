"""题目
无向图染色,每个节点可为红色(1)或者黑色(0)
保证所有相邻节点不能同时为红色
给出所有的方案种数量
"""

from tracemalloc import start
from typing import Optional


class Vertex :
    def __init__(self, name:Optional[str] , value:Optional[int] = None ) :
        self.name = name
        self.val = value
        

class GraphAdjList :
    def __init__(self, vex_name, mat_list, values:Optional[list[int]] = None) :    #输入为顶点名字列表 对应值 关系矩阵
        #顶点列表属性 邻接表
        self.vertices : list[Vertex] = []
        self.adj_mat : dict[Vertex,list[Vertex]] = {}

        """处理输入"""
        #1.将 vex_name, values 转化为 Vertex对象储存为属性
        self.vertices = self.to_vertex(vex_name, values)
        
        #2.将顶点作为键添加
        for vex in self.vertices :
            self.adj_mat[vex] = []
        
        #3.构造邻接表 将mat_list 每一行从self.vertices找到对应 作为边添加
        self.add_edge(mat_list)
        

    def to_vertex(self , vex_name, values:Optional[list[int]] = None) :
        if values == None :
            return [Vertex(vex_name[i]) for i in range(len(vex_name))]
        
        else :
            return [Vertex(vex_name[i], values[i]) for i in range(len(vex_name))]
        

    def add_edge(self, mat_list) :
        for i,edge in enumerate(mat_list) :
            for ele in edge :
                for vex in self.vertices :
                    if vex.name == ele :
                        self.adj_mat[self.vertices[i]].append(vex)
        
    
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
            

def solve(graph:GraphAdjList, start_point:str):
    """黑色为0 红色为1"""
    for vex in graph.vertices :
        if vex.name == start_point :
            start_vex = vex                     #找到起点 

    res = backtracing_search(graph, start_vex) 
    
    return res
    

"""找出多个方案需要回溯"""
def backtracing_search(graph:GraphAdjList, start_vex:Vertex, visited = None, res = []):
    if visited == None :
        visited = set[Vertex]()
    
    """当前节点"""
    #1.将当前节点添加到 visited 集合中
    visited.add(start_vex)  
    #2.根据限制尝试染色赋值1 or 0 
    for color in [0,1]:                               #两种颜色都进行循环染色
        #每次尝试填色都先清空
        start_vex.val = None            
        #周围存在红色 则只能染黑色
        if any( ele.val == 1 for ele in graph.adj_mat[start_vex]) :                         
            start_vex.val = 0
        
        else :
            start_vex.val = color                        #染色
        
        #去过所有节点后 保存未存在过的解
        if len(visited) == len(graph.vertices) :          
            _ = [ _.val for _ in graph.vertices]
            if _ not in res :
                res.append(_)
        
        #继续遍历存在没有去过的节点
        for vex in graph.adj_mat[start_vex] :           #如果不存在未访问过的节点则不会进入下一层             
            if vex in visited :
                continue
            else :
                backtracing_search(graph, vex, visited, res)
        
        
    #for循环结束时 即所有填色都尝试过了 返回上个节点时删除本节点信息
    visited.remove(start_vex)
    start_vex.val = None
    
    return res
    
 
def main() :
    vex_name = ['1','2','3','4']
    mat_list = [['2','3'],['1','4'],['1','4'],['2','3']]
    graph_list = GraphAdjList(vex_name,  mat_list, values=None)
    print("邻接表为=")
    graph_list.pt()
    res = solve(graph_list, '1')
    print(len(res))


if __name__ == "__main__" :
    main()