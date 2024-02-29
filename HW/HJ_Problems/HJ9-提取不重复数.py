def main() :
    indata = input()                            #输入int类型数据
    pivot_list = []
    outdata_list = []

    indata_list = list(indata)                  #将字符串的每个字符转化为独立的元素放在列表
                                                #或者使用列表推到模式: indata_list = [for char in indata]
                                                #set方法去重会乱序
    indata_list.reverse()                       #这里必须先翻转保证从右向左读，去重再翻转答案错误
    for ele in indata_list :
        if ele not in pivot_list :
            pivot_list.append(ele) 
            outdata_list.append(ele) 
        else :
            continue

    outdata_list = ''.join(outdata_list[:])
    print(outdata_list)


if __name__ == "__main__" :
    main()