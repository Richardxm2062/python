"""题目
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
"""思路
字典类型是没法根据值进行排序的 因此考虑列表 [单词,次数,长度] 优先级:次数降序 长度升序 单词音节升序
需要使用到sorted函数的高级用法 sorted(arr,key = lamda x: (-x[0],x[1],x[0])) 
对列表 arr进行排序 使用参数key接受自定义排序 每一行元素 [单词,次数,长度] 
传入 lamda函数 -x[1]表示对第1个元素降序(优先) x[1]对第1个元素升序 x[0]表示最后按第0个元素升序
"""

from difflib import restore
from turtle import left


def permutation(in_list) :
    for i,ele in enumerate(in_list) :
        lst :list[str] = []                          #临时列表
        lst = list(ele)                              #每个单词构成的列表并排序
        lst.sort()
        in_list[i] = ''.join(lst)                    #还原为字符串后放回列表
    
    res = []
    dic = {}
    #初始化字典
    for ele in in_list :
        dic[ele] = [ele,0,len(ele)]                      #单词、次数、长度
    
    #统计次数
    for ele in in_list :
        dic[ele][1] += 1
    
    vals = list(dic.values())
    vals = sorted(vals,key= lambda x: (-x[1],x[2],x[0]))
    
    for row in vals :                                   #这里不仅要添加单词本身 还要多次添加重复出现的单词
        for i in range(row[1]) :
            res.append(row[0])
        
    res = ' '.join(res)
         
    return res
    
    
def main() :
    in_list = input().split()
    res = permutation(in_list)
    print(res)


if __name__ == "__main__" :
    main()