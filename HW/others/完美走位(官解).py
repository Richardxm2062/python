# coding:utf-8
#JSRUN引擎2.0，支持多达30种语言在线运行，全仿真在线交互输入输出。 
import functools
import copy
 
#处理输入
input_str = input()
 
char_count = {'W':0,'A':0,'S':0,'D':0}
 
#频次统计
for single_char in input_str:
    char_count[single_char] += 1
 
#特殊情况
if char_count['W'] == char_count['A'] and \
    char_count['W'] == char_count['S'] and \
    char_count['W'] == char_count['D'] :
        print (0)
else:
    # 左右区间位置 
    left = 0;
    right = 0;
    length = 0;
    
    # 替换的最小长度
    res = len(input_str);
    # 出现次数最多的字母
    max_char_num = 0;
    # 可替换字母个数, 随着指针移动，如果free_char_num 大于0且能被4整除，当前范围满足条件，左指针右移一格，否则右指针右移
    free_char_num = 0;
    
    char_count[input_str[0]] -= 1
    while (True):
        max_char_num = max(max((max(char_count['W'], char_count['S'])), char_count['A']), char_count['D']);
        length = right - left + 1;
        free_char_num = length - ((max_char_num - char_count['W']) + (max_char_num - char_count['S']) + (max_char_num - char_count['A']) + (max_char_num - char_count['D']));
        if (free_char_num >= 0 and free_char_num % 4 == 0):
            if(length<res) :
                res = length
            
            char_count[input_str[left]] += 1
            left += 1
 
        else:
            right += 1
            if (right>= len(input_str)):
                break
            char_count[input_str[right]] -= 1
        
 
        if (right >= len(input_str)):# 越界即结束
            break;
 
 
    print (res)
 
 