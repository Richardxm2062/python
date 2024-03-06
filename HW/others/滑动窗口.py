"""题目
instr = "ADFSDFBSDF" 
tar = 'DB'
找出存在tar中每个字符的 最小子串
"""

def solve(instr, tarstr) :
    instr = list(instr)
    tarstr = list(tarstr)
    
    left_pointer = 0 
    right_pointer = 1
    res = [['0']]                                           #记录满足条件的最小区间  
    sl = slice(left_pointer,right_pointer)                  #切片操作
    are = instr[sl]                 #当前指针区间
    while True : 
        sl = slice(left_pointer,right_pointer)              #必须更新
        are = instr[sl]
        if tarstr[0] in are and tarstr[1] in are :          #当前区间存在字符串tar的字符
            #更新解
            if res[0] == ['0'] :
                res[0] = are 
            if len(are) < len(res[0]) :
                res[0] = are                         
            left_pointer += 1                               #左指针移动缩小区间
            
        else :                                              #当前区间不存在所需的字符
            right_pointer += 1                              #右指针移动扩大区间
            
        if right_pointer > len(instr) :                    #越界
            break
        
    return res


def main() :
    instr = input()
    tarstr = input()
    res = solve(instr,tarstr)
    print(res[0])
    
   
if __name__ == "__main__" :
    main()
