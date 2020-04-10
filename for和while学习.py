
# 1、for和while学习。
# for i in range(len(list)-1):
#     print(list[i])
#
# for strs in list:
#     print(strs)
#
# i=0
# while(i<len(list)-1):
#     print(list[i])
#     i=i+1


#2、关于list的操作
#
# list = ["python", "java", "c", "c++"] #索引从0开始。

#s1 输出list中所有元素
# for i in range(len(list)):
#     print(list[i])

#s2 输出list中所有元素
# for strs in list:
#     print(strs)

#s3 输出list中所有元素
# i=0
# while(i<len(list)):
#     print(list[i])
#     i=i+1

#s4 continue的使用:跳过索引为1的元素
# for i in range(len(list)):
#     if (i==1):
#         continue
#     print(list[i])

# 3、字符串的压缩问题解决
# chars="ssssssssssrrrrrrrrrrrrttttttttt"
# tempRes="s10r12t9"

# print(temp.startswith("s")) #判断开始元素
# print(chars)

# chars=str(chars)

def compress(chars):
    # print(chars)
    cur=0 #记录当前的索引
    i=0
    result=[]
    while i<len(chars):
        j=i
        # print(j)
        while j < len(chars)-1 and chars[j]==chars[j+1]:
            j+=1
        chars[cur]=chars[i]
        cur+=1
        if i!=j:
            times=str(j-i+1) #将字符的次数写入原串中
            result.append(chars[cur] + str(times))
            # print(chars[cur])
            # print(times)
        i=j+1 #处理下一个字符
    print(result)

    return result

if __name__=='__main__':
    chars=["a","a","b","b","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c","c"]

    res=compress(chars)
    # print(res)

# 4、作业习题：逆序实现

#reverse实现

# L=["python", "java", "c", "c++"]

# L.reverse()
#
# print(L) #['c++', 'c', 'java', 'python']


#for循环实现

def reverse0(L):
    result=[]
    for i in range(len(L)-1,-1,-1):
        # print(i) #倒叙
        result.append(L[i])
    return result


#while循环实现

def reverse1(L):
    result=[]
    n=len(L)-1
    while n>=0:
        result.append(L[n])
        n-=1
    return result

if __name__=='__main__':
    L=["python", "java", "c", "c++"]
    res0=reverse0(L)
    res1=reverse1(L)

    print(res0)
    print(res1)


