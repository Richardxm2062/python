def main() :

    global ct                                          #初始化全局变量
    ct = 0
    
    while True :
        arr_str = input("请输入一组数组，以空格分割:")
        arr_str = arr_str.split()
        if all(num.isdigit() for num in arr_str) :
            arr = list(map(int,arr_str))
            quick_sort(arr)
            print(arr)
            break

        else :
            print("数组包含非数字")


def quick_sort(arr) :
    if len(arr) <= 1 :                                  
        return arr

    else :
        global ct
        ct += 1
        print("第{}次调用快排".format(ct))
        pivot = arr[0]      #pivot是一个基准数，通常取第一个
        less_than_p = [x for x in arr[1:]  if x <= pivot]
        greater_than_p = [y for y in arr[1:]  if y > pivot]
        print("第{}次pt为".format(ct),pivot)
        print("第{}次lp".format(ct),less_than_p)                           #.format()为占位符,依次替换{}。使用位置为双引号后
        print("第{}次gp".format(ct),greater_than_p)                          
        quick_sort(less_than_p)                                           #这里将持续递归使用此函数直至小于等于的数组被排序结束
        quick_sort(greater_than_p)
        arr[:] = less_than_p + [pivot] + greater_than_p                   #.extend方法原数组被修改并不返回新数组，旧元素并不需要被保留
        print("开始返回递归")
        print("第{}次递归后arr为".format(ct),arr)


if __name__ == "__main__" :
    main()


#在递归中会反复用到lp gp p arr等变量名。在最后一次递归结束中arr的值将被返回给gp，意味着gp的值将被修改。比如[2,3,4,3,2]这个数组
#在第二次递归的时候gp=[3,4,3]进行快排，它将被引用给arr这个参数(它尽管是母列表，在这个局部函数里它只是gp的引用)，之后得到的arr[3,3,4]
#将会返回给gp 由此gp得到值将是排序好的列表。不再是[4]或者[3,4,3]