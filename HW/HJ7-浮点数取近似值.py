def main() :
    ft = float(input())
    pivot = 0.5
    bt = 0
    
    while ft - bt > 0 :
        bt += 1
    
    #找到小数点前的数字
    bt -= 1
    af = ft - bt 
    if af < 0.5 :
        print(bt)
    
    else :
        bt += 1 
        print(bt)
    
    #最后需要输出整数而非浮点数

if __name__ == "__main__" :
    main()