"""

完美二叉树通过层序遍历,根节点索引为0,用列表构造整个
左子节点的索引为 2i+1 右子节点的索引为 2i+2 (类似于链表构造的指针作用)
表示空子节点,通过显示的使用None,则适用于更多的二叉树

对象需要的功能:
属性:tree
查询:长度,当前索引节点的值,左子节点的索引值,右子节点的索引值,父节点的索引值

"""

from typing import Union


class TreeNode_arr :
    #数组构造树
    def __init__(self,arr: list[Union[int,None]]) :
        self.tree = arr        
        self.res = []                       #结果储存

    #列表容量   
    def size(self) : 
         return len(self.tree)   
    
    #获取索引为i的节点的值
    def val(self,i : int) :
        #越界判断 
        if i < 0 or i >= self.size() :      #len的返回值是索引最大值+1
            return None

        else :
            return self.tree[i]
        
    #获取其他节点的索引值
    def left(self, i:int) :
        return 2*i+1
    
    def right(self, i:int) :
        return 2*i+2
    
    def parent(self, i:int) :
        return (i-1)//2
    
    #层序遍历 :直接遍历数组即可
    def level_order(self) :
        #可以在其他方法中定义对象的新的属性,最好在初始化函数定义完

        for ele in self.tree : 
            if ele is not None :
                self.res.append(ele)
        
        return self.res
    
    
    def dfs(self, i:int, order:str) :
        self.res = []                                 #初始化
        #空节点直接返回
        if self.val(i) is None :
            #return以确保返回到上一递归层不再执行后序添加值代码
            return
        
        if order == "pre" :
            self.pre_order(i, self.res)               #定义函数后调用,在对象
            return self.res
        
        if order == "in" :
            self.in_order(i, self.res)                #定义函数后调用,在对象
            return self.res
        
        if order == "post" :
            self.post_order(i, self.res)              #定义函数后调用,在对象
            return self.res


    def pre_order(self, i:int , arr:list =[]) :
        if self.val(i) is None :
            #return以确保返回到上一递归层不再执行后序添加值代码
            return arr
        
        self.res.append(self.val(i))
        self.pre_order(self.left(i),arr)
        self.pre_order(self.right(i),arr)
        return self.res
    
    
    def in_order(self, i:int, arr:list) :
        if self.val(i) is None :
            #return以确保返回到上一递归层不再执行后序添加值代码
            return  arr
        
        self.in_order(self.left(i),arr)
        self.res.append(self.val(i))
        self.in_order(self.right(i),arr)
        return self.res
    
    
    def post_order(self, i:int, arr:list) :
        if self.val(i) is None :
            #return以确保返回到上一递归层不再执行后序添加值代码
            return arr
        
        self.post_order(self.left(i),arr)
        self.post_order(self.right(i),arr)
        self.res.append(self.val(i))
        return self.res


#测试
def main() :
    My_t = TreeNode_arr([1, 2, 3, 4, None, 6, 7, 8, 9, None, None, 12, None, None, 15])        #按层序顺序写的
    print(My_t.tree," 大小为 ",My_t.size())
    print("节点值为6(索引为5)的左子节点索引为",My_t.left(5),"值为",My_t.tree[My_t.left(5)])
    res = My_t.level_order()
    print("层序遍历结果",res)
    res = My_t.dfs(0,"pre")
    print("dfs前序遍历结果",res)
    res = My_t.dfs(0,"in")
    print("dfs中序遍历结果",res)
    res = My_t.dfs(0,"post")
    print("dfs后序遍历结果",res)
    

if __name__ == "__main__" :
    main()


    

    
