"""题目
部门组织绿岛骑行团建活动。租用公共双人自行车,每辆自行车最多坐两人,最大载重M。
给出部门每个人的体重,请问 「最少」 需要租用多少双人自行车。

输入描述：
第一行两个数字m、n,分别代表自行车限重,部门总人数。
第二行,n个数字,代表每个人的体重w[i],体重都 小于等于 自行车限重m。
0<m<=200 
0<n<=1000000 

输出描述：
最小需要的双人自行车数量。

3 4
3 2 2 1
输出
3
"""
"""思路
求最小的租车数量,那么需要尽可能保证每辆车的载重最大
贪心算法:体重升序排列,使用两个指针指向头部与尾部
1.如果w[0] + w[-1] > m 或者仅剩一人 则r只能一个人坐
2.在贪心前 判断是否 左指针达到了边界
3.没有达到边界则 左指针+1
3.当两指针和开始 > 则  w[l-1] + w[r] 为最佳方案 删除这两个元素(先删除l-1 pop删除末尾)
4.指针重新指向头尾 循环
5.w为空时不再有人 跳出循环
"""


def greedy_solve(m, n, w_list) :
    ct = 0                                                      #计数器
    left_pointer = 0 
    right_pointer = n-1
    res = []                                                    #储存排列方式
    """(事实上w_list的删除操作直接移动指针就行了)"""
    while True :
        #终止条件:不再有人
        if w_list == [] :
            break
        
        #先判断是否需要单人骑行(仅剩一人也成立)
        if w_list[0] + w_list[-1] > m or len(w_list) == 1 :                           
            res.append([w_list.pop()])                            #删除最重一人
            ct += 1                                             #计数
            #指针重置
            left_pointer = 0
            right_pointer = len(w_list) - 1
            continue
            
        #开始贪心
        else :          
            left_pointer += 1 
        
        #是否达到寻找边界,直接载重两个最重的
        if left_pointer == right_pointer :                       
            ct += 1
            #删除最重的两个
            res.append([w_list.pop(),w_list.pop()])
            #指针重置
            left_pointer = 0
            right_pointer = len(w_list) - 1 
            continue
        
        
        #贪心结果判断
        if  w_list[left_pointer] + w_list[right_pointer] > m :          
            ct += 1
            res.append([w_list.pop(left_pointer-1),w_list.pop()])
            #指针重置
            left_pointer = 0
            right_pointer = len(w_list) - 1    
            continue
        
    return res
        
        
def main() :
    m_n =list(map(int,input().split()))                         #限重与人数
    w_list =list(map(int,input().split()))                      #重量列表
    w_list.sort()                                               #升序
    res = greedy_solve(m_n[0], m_n[1] ,w_list)
    print(f"一共需要{len(res)}辆车,其组合方式为:")
    for row in res :
        print(row,end=" ")

if __name__ == "__main__" :
    main()