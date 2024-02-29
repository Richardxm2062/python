def main():
    str = input("请输入一串字符串，空格分隔")
    str = str.split()                                       #split()方法直接返回一个列表不用再list()
    if all(num.isalpha() for num in str) :                  #isalpha()方法检测是否只包含字符串,isinstance()函数可以判断类型不能判断仅包含
        fl = str[-1]
        length = len(fl)                                    #len()对非数组，对字符串使用时直接给出单个字符数
        print("最后一个单词为{},长度为{}".format(fl,length))
        return 0
    else :
        print("输入的字符串并非只包含字母")
        return -1
        

if __name__ == "__main__":
    main()