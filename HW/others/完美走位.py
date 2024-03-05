"""
题目:
输入一个长度为4的倍数的字符串,字符串中仅包含WASD四个字母。
将这个字符串中的连续子串用同等长度的仅包含WASD的字符串替换,如果替换后整个字符串中WASD四个字母出现的频数相同
那么我们称替换后的字符串是“完美走位”。求子串的最小长度。
如果输入字符串已经平衡则输出 0 
输入:
一行字符表示给定的字符串s 数据范围:
1<=n<=10^5且n是4的倍数,字符串中仅包含WASD四个字母。输出一个整数表示答案
样例输入输出示例
1:输入:WASDAASD 输出:1 说明:
将第二个A替换为W,即可得到完美走位。
示例2:输入:AAAA 输出:3 说明:
将其中三个连续的A替换为WSD,即可得到完美走位
"""

"""(官解看不懂)
思路: 先计算平衡时每个元素的 个数 , 记录超过平衡数的 元素 比如 'A' 与 'W'各超2个    
该问题就退化到 target_str = AAWW 的滑动窗口问题
那么就是在该字符串中找到包含target_str中所有字符的最短字符串
"""

from typing import Optional


def solve(arr : list[str], length:int, dictionary = {'W':0,'A':0,'S':0,'D':0}) :
    arr = list(arr)                 #初始化为列表
    
    #统计各字符出现次数
    for ele in arr :
        dictionary[ele] += 1
        
    #初始即为完美
    if  dictionary['W'] == dictionary['A'] == dictionary['S'] == dictionary['D'] != 0  :
        return []
    
    #需要寻找的字符及其个数
    dictionary = perfect_arr(arr)
    #移动窗口构建的字典
    dictionary2 =  {'W':0,'A':0,'S':0,'D':0}
    
        
    #双指针初始位置 
    left_pointer = 0
    right_pointer = 1                                   #[0:0]的索引将为空
    res = [['0']]                                       #储存串
    #滑动区间
    mv_wd = arr[left_pointer:right_pointer]
    
    while True :
        mv_wd = arr[left_pointer:right_pointer]         #重新构建窗口
        for ele in mv_wd :
            dictionary2[ele] += 1
        #获取需要字符 字典的键
        keys_list = dictionary.keys()
        if all(dictionary2[ele] >= dictionary[ele] for ele in keys_list):   #如果所有需要字符的数量都被满足
            if res[0] == ['0'] :
                res[0] = mv_wd
            else :
                if len(mv_wd) <= len(res[0]) :
                    res[0] = mv_wd

            left_pointer += 1           #缩小区间
        else :
            right_pointer += 1          #扩大区间    
        
        if right_pointer > length :
            break
        dictionary2 =  {'W':0,'A':0,'S':0,'D':0}
    res = res[0]
    return res
    
def perfect_arr(mv_wd = [], dictionary:Optional[dict] = None, change_num:Optional[int] = None)  :
    
    dictionary = {'W':0,'A':0,'S':0,'D':0}          #储存当前列表的次数
    dictionary2 = {'W':0,'A':0,'S':0,'D':0}         #储存需要被更改的元素
    
    #当前窗口的个元素 个数
    for ele in mv_wd :
        dictionary[ele] += 1
    
    perfect_pivot = len(mv_wd) / 4             #完美指标,即每个元素的平衡时需要的个数
    #所有出现次数大于平衡指标的需要进行调整
    for ele in ['W', 'A', 'S', 'D'] :
        if dictionary[ele] > perfect_pivot :
            dictionary2[ele] = dictionary[ele] - perfect_pivot

    return dictionary2
                

def main() :
    str_arr = list(input())             #得到每个字符组成的列表
    str_len = len(str_arr)              #获取数组长度
    str_res:list[str] = []
    str_res = solve(str_arr,str_len)  # type: ignore
    print(len(str_res))

if __name__ == "__main__" :
    main()