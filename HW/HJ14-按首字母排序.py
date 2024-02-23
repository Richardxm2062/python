def main() :
    num = int(input())
    list = []

    for i in range(num) :
        list.append(input())
    
    list.sort()
    for j in list :
        print(j)
    
if __name__ == "__main__" :
    main()