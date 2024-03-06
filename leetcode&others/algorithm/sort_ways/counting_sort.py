"""计数排序
用于整数数组排序,将整数作为索引插入 count 数组,其索引因此为排序
遍历count数组其数值为重复次数
"""

def counting_sort(arr:list[int]) :
    #最大数值
    max_val = max(arr)
    
    #计数容器,最大索引值为max_val
    counting = [0 for _ in range(max_val+1)]
    #对arr遍历,其值作为索引,并使counting对应位置数值+1(计数方法)
    for ele in arr :
        counting[ele] += 1
    
    #重新装填arr,counting val索引为值,值counter为次数
    left_point = 0
    for val,counter in enumerate(counting):
        for c in range(counter):                #重复元素插入次数
            arr[left_point+c] = val             #从左指针开始
        #移动指针:
        left_point += counter
            
            
def main() :
    arr = [5,1,1,5,3,7,8,2,9,0,0,3,1,5,2,6,7,8]
    counting_sort(arr)
    print(arr)


if __name__ == "__main__" :
    main()