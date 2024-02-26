"""

堆 「heap」是一种满足特定条件的完全二叉树,主要可分为两种类型:
(完全二叉树是一种二叉树，其中除了最后一层外，每一层的节点都必须填满，且最后一层的节点都尽量靠左排列。)
‧「小顶堆 min heap」:任意节点的值 ≤ 其子节点的值。
‧「大顶堆 max heap」:任意节点的值 ≥ 其子节点的值。
堆通常用于实现优先队列，大顶堆相当于元素按从大到小的顺序出队的优先队列。
从使用角度来看， 我们可以将“优先队列”和“堆”看作等价的数据结构。

实现堆通常使用 heapq 模块
heapify(iterable): 将可迭代对象转换为 小顶堆。时间复杂度为 O(n)。
heappush(heap, item): 将元素插入堆中,并保持堆的不变性。
heappop(heap): 弹出并返回堆中的最小元素。
heapreplace(heap, item): 弹出并返回堆中的最小元素,同时将新元素插入堆中。
heappushpop(heap, item): 将新元素插入堆中,然后弹出并返回堆中的最小元素。
nlargest(n, iterable, key=None): 返回可迭代对象中最大的 n 个元素。
nsmallest(n, iterable, key=None): 返回可迭代对象中最小的 n 个元素。

"""

import heapq
from multiprocessing import heap

def main() :
    arr = [3,2,5,7,1,4,8,6,9]
    print("原数组为",arr)
    heapq.heapify(arr) 
    print("堆结构为",arr)           #默认小顶堆,且堆化的结果并不唯一
    print(heapq.nlargest(5,arr))   #以大到小返回最大的5个元素 












if __name__ == "__main__" :
    main()


