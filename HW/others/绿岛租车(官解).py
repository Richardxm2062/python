# coding:utf-8
import functools
 
 
#处理输入
input_param = [int(x) for x in input().split(" ")]
m = input_param[0]
n = input_param[0]
weights = [int(x) for x in input().split(" ")]
 
#第一步，单词内部调整
weights = sorted(weights, reverse=False)
 
#第二步，左右指针向中间移动
left=0;
right = len(weights)-1
 
#结果
min_bikes = 0
 
#当前重量
temp_weight = weights[right] + weights[left]
 
#题目中有两个隐含的条件
# 1: 一辆车最多骑两个人
#2：人的重量不可能大于车的载重
 
while(left<right):
    if (temp_weight > m):
        right -= 1
        min_bikes += 1
        temp_weight = weights[right] + weights[left]
    else:
        right -= 1
        left += 1
        min_bikes += 1
        temp_weight = weights[right] + weights[left]
 
 
#感谢评论区老铁点拨
if (left == right):
    min_bikes += 1
 
 
print (min_bikes)