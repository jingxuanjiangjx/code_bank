'''
data:2020/4/9
auther:jx
'''
class Solution:
    def Fibonacci(self,n):
        if n<=0:
            return 0
        elif n==1:
            return 1
        else:
            return self.Fibonacci(n-1)+self.Fibonacci(n-2)

    def Fibonacci_list(self,n):
        result_list=[]
        for i in range(1,n+1):
            result_list.append(self.Fibonacci(i))
        return result_list


if __name__=='__main__':
    s=Solution()
    res=s.Fibonacci_list(10)
    print(res)





