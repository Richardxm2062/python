def main() : 
    indata = list(input())
    indata_set = set(indata)            #乱序去重
    indata_list = list(indata_set)  
    length = len(indata_list)           #统计个数
    print(length)

if __name__ == "__main__" :
    main()