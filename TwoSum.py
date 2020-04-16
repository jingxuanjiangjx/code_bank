'''
data:2020/4/14
auther:jx
'''

def twoSum(nums,target):
    hash_table = {}
    for i,num in enumerate(nums):
        if target-num in hash_table:
            return ([hash_table[target-num],i])
        hash_table[num]=i
    return []

if __name__=='__main__':
    nums = [2, 4, 8, 10]
    target = 5
    res=twoSum(nums,target)
    print(res)

