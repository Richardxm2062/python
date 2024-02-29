def main() :
    in_list = input().split()
    in_list.reverse()
    out_str = ' '.join(in_list)         #记得以空格分隔
    print(out_str)
    
if __name__ == "__main__" :
    main()