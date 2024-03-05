"""
1. 输入数组并建立大顶堆(非库用法)。完成后，最大元素位于堆顶。
2. 将堆顶元素(第一个元素)与堆底元素(最后一个元素)交换。完成交换后，堆的长度减 1 ，已排序元
素数量加 1 。
3. 从堆顶元素开始，从顶到底执行堆化操作(sift down)。完成堆化后，堆的性质得到修复。
4. 循环执行第 2. 步和第 3. 步。循环 n - 1 轮后，即可完成数组排序。
"""


"""不使用第三方库"""

#大顶堆 建堆
def sift_down(arr:list[int] ,length:int, n:int) :                 #长度动态变化,需要向下传递当前长度、数组、当前节点
    """堆有效长度length,当前节点n,最大值的节点max"""
    while True :
        l = 2*n + 1              #左节点索引
        r = 2*n + 2              #右节点索引
        max = n
        """找到三个节点中值最大的节点索引"""
        if l < length and arr[l] > arr[max] :
            max = l
        if r < length and arr[r] > arr[max] :
            max = r
        """如果当前节点为最大,则无需堆化,跳出"""
        if max == n :
            break
        
        """和当前父节点交换值"""
        arr[n],arr[max] = arr[max],arr[n]
        """将根节点更新到索引值为max的节点(此时的值为小)"""
        n = max 
        
      
def heap_sort (arr:list[int]) :
    """最大长度为树最右下角的索引,找到其父节点的索引(i-1)//2"""
    """此父节点索引为除叶节点之外的最大索引值,即 非叶节点个数"""
    """堆化所有非叶节点(都是自下而上)"""
    for i in range((len(arr)-2)//2,-1,-1) :                    #倒序中,左开右闭,遍历到0需要到-1
        sift_down(arr,len(arr),i)
    print(arr)
        
    """进行堆排序"""
    # 从堆中提取最大元素，循环 n-1 轮
    for i in range(len(arr)-1,-1,-1):
    # 交换根节点与最右叶节点(交换首元素与尾元素) 
        arr[0], arr[i] = arr[i], arr[0]
        sift_down(arr, i, 0)
    
    
def main() :
    arr = [2,3,5,7,1,8,9,0]
    heap_sort(arr)
    print(arr)
    

if __name__ == "__main__" : 
    main()