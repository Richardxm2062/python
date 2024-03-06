"""桶排序
将浮点数的值区间扩大,并作为索引放到桶中
每个桶的值域独立且有序(索引结果)
"""

from random import random

def bucket_sort(arr:list[float]) :
    num = len(arr) 
    #创建总数的1/2个桶
    k = num // 2 + 1
    buckets = [[] for _ in range(k)]
     
    #数据区间为[0,1),将数据映射到[0,k+1),并作为索引值放入桶中
    #这样每个桶之间的值域是独立且有序的
    for num in arr :
        i = int(num*k)              #数据量要求比较大
        buckets[i].append(num)     
        
    #对每个桶进行排序操作
    for bucket in buckets :
        bucket.sort()
        
    res = []
    for row in buckets :
        res += row
    
    print(res)        
    
    
def main() :
    arr = []
    for i in range(5) :
        arr.append(random())
    
    bucket_sort(arr)
  
  
if __name__ == "__main__" :
    main()
    