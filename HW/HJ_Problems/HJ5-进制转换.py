def main() :
    indata = input()
    indata = list(indata)
    outdata = 0                                   #赋值即是声明
    oxdic1 = dict(A=10,B=11,C=12,D=13,E=14,F=15)  
    oxdic2 = dict(a=10,b=11,c=12,d=13,e=14,f=15)  #删除开头,每次的索引值都是0
    for i in range(2) :                             
        indata.pop(0)
    
    #最高位指数
    exp = len(indata) - 1

    for element in indata :
        if element in oxdic1 :
            value = oxdic1[element] * (16**exp)
            outdata = outdata + value
            exp -= 1 
        elif element in oxdic2 :
            value = oxdic2[element] * (16**exp)
            outdata = outdata + value
            exp -= 1 
        else :
            value = int(element) * (16**exp)
            outdata = outdata + value
            exp -= 1 
        
    # 部分进制转化可以用连接 这里只需要加起来 pp.append(''.join(outdata[:]))
    print(outdata)

if __name__ == "__main__" :
    main()

#进制转换:
    """
    每个进制的展开式从右到左指数为0增涨,自身为底,直接计算后均为10进制
    10->16 :除以16 以次得到商和余数,将商继续除以16直到为0.
    依次次得到从右到左乘数(商表示)除了多少次有多少位
    例如3648 转化为 16进制为E40
    被除数  除数  商  余数 位次
    3648   16   228  0    0
    228    16   14   4    1
    14     16   0    14   2
    把商换成16进制 就是 0xE40
    """
    