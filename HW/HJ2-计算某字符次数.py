def main() :
    strings = input()
    strings = strings.split()
    target = input()
    str_ls = []
    num = 0
    for word in strings :
        for sg in list(word):
            if target.casefold() == sg.casefold() :     #casefold()方法可以进行大小写不敏感的比较，或者使用upper lower方法进行统一转化
                num += 1
            else :
                continue
    print(num)
    

if __name__ == "__main__" :
    main()