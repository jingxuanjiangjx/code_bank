'''
data:2020/4/9
auther:jx

'''

'''
方法一：将数字转换为字符串，并检查字符串是否为回文。
'''
# class Solution:
#
#     def isPalindrome(self,x):
#         a=str(x)
#         n=len(a)
#         # print(n)
#         i=0
#         # print(n//2)
#         while i<(n//2):
#             if a[i]!=a[n-1-i]:
#                 return False
#             else:
#                 return True

# if __name__=='__main__':
#     s=Solution()
#     res=s.isPalindrome(-121)
#     print(res)

'''
方法二：字符串反转
'''
class Solution:
    def isPalindrome(self,x):
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False

if __name__=='__main__':
    s=Solution()
    res=s.isPalindrome(121)
    print(res)





