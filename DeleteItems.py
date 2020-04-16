'''
data:2020/4/14
auther:jx
'''

#主元素问题（返回出现次数最多的元素）
# nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]  # 主元素问题  3   k:V

#思路：原序列中去除两个不同的元素，在新的序列中  多数元素不变。
#count标记主元素的个数，假设第一个是主元素，从第二个开始比较。
#count加减的过程模拟去掉两个不同的元素的过程
def majorityNumber(nums):
    key, count = nums[0], 1
    for i in range(0,len(nums)):
        if key==nums[i]:
            count+=1
        else:
            count-=1
            if count==0:
                if i<len(nums)-1:
                    key=nums[i+1]
    return key

if __name__=='__main__':
    nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]

    res=majorityNumber(nums)
    print(res)

#删除操作实现
# list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]

#  思路1：复制一个list，在源list上做删除操作。使用for循环，remove实现。
# 切片list[:]会产生一个新的对象，占用一块新的内存，list所指向的对象的值改变时，list[:]不变。
# 数组赋值不能用切片来达到相同的目的。
# for i in list[:]:
#     list.remove(i)

# 思路2：逆序遍历，使用pop实现删除操作
# for i in range(len(list)-1,-1,-1):
#     print(i)
#     list.pop(i)

# 作业1 迭代器遍历 实现删除
#思路：迭代器，使用next()遍历
listit = iter(list[:])
try:
    while True:
        li = next(listit)
        list.remove(li)
except StopIteration:
    pass


# 作业2  出现 nums.length/4次 的值返回为 list 可以用字典解决
# nums1 = [1, 1, 2, 2, 3, 3, 4, 4] # 1 2 3 4

# #思路1：利用字典完成统计,数据多时运行太慢。
nums1 = [1, 1, 2, 2, 3, 3, 4, 4]
dict={}
for key in nums1:
    dict[key]=dict.get(key,0)+1
list=[]
for num in dict:
    if dict[num]==len(nums1)/4:
        list.append(num)
print(list)

# # 思路2：利用Python的collection的Counter统计
nums1 = [1, 1, 2, 2, 3, 3, 4, 4]
from collections import Counter
result = Counter(nums1)
count_dict = dict(result)
list=[]
for num in count_dict:
    if count_dict[num]==len(nums1)/4:
        list.append(num)
print(list)


