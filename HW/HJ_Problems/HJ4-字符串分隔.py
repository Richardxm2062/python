def main() :
    #拆分题，从8开始拆 %运算是取余计算，//是取商
    St = input()
    lt = len(St)
    out(St,lt)
    

def out(arr,length) :
    ls = list(arr)
    pp = []
    #补充0的个数
    zero_num = 8 - length % 8
    if zero_num == 8:
        zero_num = 0
        
    else :
        for i in range(zero_num) :
            #必须要添加字符0而非整数0
            ls.append("0")      

    for j in range(0,len(ls),8) :
        #将列表的部分元素使用"".jion()方法变成一个字符，" "有空格的话将会使每个元素之前有个空格
        #join() 方法用于将序列中的元素以指定的字符串连接生成一个新的字符串。其语法为：str.jion(sequence)。str为分隔符 ""为空
        pp.append("".join(ls[j:j+8]))       
        #这里的pp是个嵌套列表
        print(pp[0])
        #用完临时的pp列表后清空                        
        pp.clear()


if __name__ == "__main__" :
    main()