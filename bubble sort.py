def main() :
    while True :                                            #持续循环到正确输入
        arr_str = input("请输入一组数组，并用空格分割:")
        arr = arr_str.split()                               #将空格输入的字符数组以空格分割返回列表
        if all(n.isdigit() for n in arr) :                  #all函数接受一个可迭代对象，isdigit可以检查字符串是否只包含数字
            arr = list(map(int,arr))                        #for n in arr 创建了一个迭代器,n代表了迭代器的当前元素
            bubble(arr)
            print(arr)
            break                                           #如果这里没有break,当if判断有false时(存在字符)并不会继续执行else反而会重头开始
    
        else :
            print("输入包含非数字")
            


def bubble(arr):
    length = len(arr)
    for i in range(length):                             #外层循环遍历的总次数为列表的元素个数
        for j in range(0,length-i-1):                   #内层循环进行对比用新的迭代器,总次数为第(i+1)个元素后面的元素个数(请区分索引和个数)
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            

if __name__ == "__main__" :                             #__name__不需要加双引号
    main()
