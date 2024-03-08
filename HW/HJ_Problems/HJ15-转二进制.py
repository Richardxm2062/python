"""题目
输入一个 int 型的正整数，计算出该 int 型数据在内存中存储时 1 的个数。
(即转为2进制后包含1的个数)
"""

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