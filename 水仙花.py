"""
data:2020/4/9
auther:jx

"""

'''
寻找三位数中满足条件的水仙花数。
方法一：基于循环。
'''
# start = 101
# end = 999
# for i in range(start,end+1):
#     # print(i)
#     bai=i//100
#     shi,ge=(i-bai*100)//10,i%10
#     if ge**3+shi**3+bai**3==i:
#         print(i)

'''
计算一定范围的水仙花数
方法二：基于循环，求自幂数。
'''
end=int(input('找寻范围： '))
for i in range(1,end+1):
    length=len(str(i))
    sum=0
    temp=i
    for j in range(length):
        sum+=(temp%10)**length
        temp//=10

    if sum==i:
        print(i)


