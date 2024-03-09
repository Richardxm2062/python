"""题目
XX市机场停放了多架飞机,每架飞机都有自己的航班号CA3385,CZ6678,SC6508等,航班号的前2个大写字母(或数字）
代表航空公司的缩写,后面4个数字代表航班信息。但是XX市机场只有一条起飞用跑道
调度人员需要安排目前停留在机场的航班有序起飞。为保障航班的有序起飞,调度员首先按照航空公司的缩写(航班号前2个字母)对所有航班进行排序
同一航空公司的航班再按照航班号的后4个数字进行排序最终获得安排好的航班的起飞顺序。请编写一段代码根据输入的航班号信息帮助调度员输出航班的起飞顺序。
说明：
1、航空公司缩写排序按照从特殊符号$ & *, 0~9,A~Z排序;
"""




def main() :
    #输入航班列表
    in_list = input().split(',')
    
    in_arr = [['None'] for _ in range(len(in_list))]
    #处理输入
    for i,ele in enumerate(in_list) : 
        cm = ele[0:2]       #航空公司
        num = ele[2:]       #航班编号
        in_arr[i] = [cm, num]                               
    
    #按要求排序好了
    in_arr = sorted(in_arr ,key= lambda x : (x[0],x[1]))
    
    #再将公司信息和航班信息合并
    out_arr = ['0' for _ in range(len(in_arr))]
    for i,ele in enumerate(in_arr) :
        out_arr[i] = in_arr[i][0]+in_arr[i][1]
    
    print(','.join(out_arr))
    
    
if __name__ == "__main__" :
    main()