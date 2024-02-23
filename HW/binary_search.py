def main() :
    
    while True :
        arr_str = input("输入数组，空格分隔:")
        target = input("输入目标数字")
        arr = arr_str.split()

        if target.isdigit() :
            target = int(target)

            if all(num.isdigit() for num in arr) :
                arr = list(map(int,arr))
                arr.sort()
                binary_search(arr,target)
                return 0

            else :
                print("目标数组包含非数字")

        else :
            print("目标数字非数字")


def binary_search(arr,target):
    left , right = 0 , len(arr) - 1 

    while left <= right:                           #必须是小于等于，这样在单数字数字在left right相等时至少能执行一次判断
        mid = (left + right) // 2                  #//表示整除(向下区取整) **表示指数
        if target == arr[mid] :
            print("目标数存在,且为位置索引为{}".format(mid)) 
            return mid                             #return才能结束整个函数,break仅仅是结束当前循环部分的代码

        elif target < arr[mid] :
            right = mid - 1
            continue

        else :                                     #python的多选控制为if elif else(elif可以有条件 else没有)
            left = mid + 1                          
            continue
    arr.insert(left,target)                        #insert方法是先索引值后目标值,被占用的元素后移
    print("不存在,数组插入为{}".format(arr))          #二分查找法的重点是 left总是指向被插入值的索引点
                                                   #不理解这一点的话考虑左右指针执行到相邻后续的指针变化
                                                   #python 使用insert方法插入并不返回任何东西print("不存在,数组插入为{}".format(arr.insert(left,target)))是错误写法

                                            
if __name__ == "__main__" :
    main()