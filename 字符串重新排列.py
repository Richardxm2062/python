"""
处理后输出:
1、单词内部调整:对每个单词字母重新按字典序排序
2、单词间顺序调整:
1)统计每个单词出现的次数,并按次数降序排列
2)次数相同,按单词长度升序排列
3)次数和单词长度均相同,按字典升序排列请输出处理后的字符串,每个单词以一个空格分隔。
输入描述:
一行字符串,每个字符取值范围:【a-ZA-Z0-9】以及空格,字符串长度范围:【1,1,1000】
例1:
输入
This is an apple
输出
an is This aelpp
例2:
输入:
My sister is in the house not in the yard
输出:
in in eht eht My is not adry ehosu eirsst
"""

def permutation(in_list) :
    for i,ele in enumerate(in_list) :
        lst :list[str] = []                          #临时列表
        lst = list(ele)                              #每个单词构成的列表并排序
        lst.sort()
        in_list[i] = ''.join(lst)                    #还原为字符串后放回列表
    
    dic = {}
    for ele in in_list :
        dic[ele] = 0                                 #初始化字典
    
    for ele in in_list :
        dic[ele] += 1                                #统计每个单词出现的次数
        
    keys = dic.keys()
    vals = dic.values()
    vals.sort()
        
    
    
    return 0 



def main() :
    in_list = input().split()
    permutation(in_list)


if __name__ == "__main__" :
    main()