def main() :
    in_data = int(input())
    count = 0

    while in_data != 0 :
        val2 = in_data % 2          #余数值
        
        if val2 == 1 :
            count += 1
        
        in_data = in_data // 2

    print(count)


if __name__ == "__main__" :
    main()