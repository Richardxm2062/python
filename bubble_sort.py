def main() :
    while True :                                                #持续循环到全部为true,存在false从头开始
        arr_str = input("请输入一组数组，并用空格分割:")
        arr_str = arr_str.split()                               #将空格输入的字符数组以空格分割返回列表
        if all(n.isdigit() for n in arr_str) :                  #all函数接受一个可迭代对象，isdigit可以检查字符串是否只包含数字 isalpha()方法检查是否只包含字母
            arr = list(map(int,arr_str))                        #for n in arr 创建了一个迭代器,n代表了迭代器的当前元素
            bubble_sort(arr)
            print(arr)
            return arr                                           #如果这里没有break,当if判断有false时(存在字符)并不会继续执行else反而会重头开始
    
        else :
            print("输入包含非数字")
            


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):                                 #外层循环遍历的总次数为列表的元素个数
        for j in range(0,length-i-1):                       #内层循环进行对比用新的迭代器,总次数为第(i+1)个元素后面的元素个数(请区分索引和个数)
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            

if __name__ == "__main__" :                                 #__name__不需要加双引号
    main()
