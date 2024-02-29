def main() :
    n = int(input())
    dict = {}
    key = []
    
    for i in range(n) : 
    
        indata = input().split()
        indata = list(map(int,indata))                  #对列表每一个元素使用int函数 需要用到map 重点

        if indata[0] in key :
            val = dict[indata[0]] + indata[1]
            dict[indata[0]] = val
            val = 0

        else :
            key.append(indata[0])
            dict[indata[0]] = indata[1]

        indata.clear()

    #items()方法可以返回一个关于键值对的可迭代对象,不需要排序的话可以使用这个方法输出
    
    key.sort()
    for k in key :
        print(k,dict[k])  
    
    #变量之间的逗号就是一个空格

if __name__ == "__main__" : 
    main()