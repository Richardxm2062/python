"""
全排列:[1,2,3] -> [1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]
思路:
对于当前输入列表 构造长度循环
依次选取元素放入choice uc放置除被选择元素外的 所有元素
递归传递 uc为空时 添当前choice到res 返回
回溯时choice开始删除最近添加的元素 并将该元素放置到 uc最新删除的元素位置

注意:
uc列表在弹出与添加回溯的过程中与choice列表添加和回溯删除是不一样的
在for循环中 uc从左依次取值弹出,回溯却使用了append方法在右边进行添加元素
那么在上层某个循环 开始在i=1开始,从uc继续取下一个值 所取出的值将和原本规划的不一样
1.使用双端队列deque 左添加
2.从右向左开始遍历uc取值(range不允许负步长 所以自己反转)
注意 尝试在uc[i]取值处创建一个副本以保证取值的有序性是无法做到的 copy()会被重复计算(即总是当前uc)
"""

"""
总结经验:
对于深度递归 并在子结构 使用数组(动态类型) 构造循环时 
在回溯过程中 注意构造循环的数组的删除添加方向一致性 
"""
#from collections import deque

#uc为未被选择的元素 res为全局结果 choice为已经被选择的元素 
def solve(uc, res = [], choice = []) :
    
    #终止条件 添加至res列表 返回该层
    if uc == [] :                                   #该节点不再有未被选择的元素
        res.append(choice.copy()) 
        return 

    for i in reversed(range(len(uc))) :             #未被选择的列表
        choice.append(uc[i])                        #依次添加元素
        #剔除掉索引值,保留重复元素
        uc = [uc[j] for j in range(len(uc)) if j != i]                       
        #uc = deque([x for x in uc if x!= uc[i]])    
        solve(uc,res,choice)                        #开始递归
        """返回层"""
        uc.append(choice.pop())                     #回溯选择列表,并将弹出的元素加入uc
        #uc.appendleft(choice.pop()) 
        
    return res 
    

def main() :
    arr = [1,2,3]
    res = solve(arr)
    print(res)


if __name__ == "__main__" : 
    main()
