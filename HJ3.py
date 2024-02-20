import random
def main() : 
    N = int(input())
    ls = [] 
    for i in range(N) :
        randomnum = random.randint(1,10)

        ls.append(randomnum)
        
        for num in range(len(ls)) :
            if randomnum == num :
                ls.remove(randomnum)
            else :
                continue

    ls.sort()
    for j in ls :
        print(j)
    
        

if __name__ == "__main__" :
    main()

#原题不需要自己生成随机数
#使用更好的方法进行去重 set()函数可以将列表包含的非重合元素转换成一个集合， 再使用list()转换为列表