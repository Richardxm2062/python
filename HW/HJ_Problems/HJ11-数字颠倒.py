def main() :
    in_list = list(input())
    in_list.reverse()
    out_str = ''.join(in_list[:])
    print(out_str)


if __name__ == "__main__" :
    main()