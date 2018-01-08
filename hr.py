import sys
import math

# if __name__ == '__main__':
#     n = int(input())
#     arr = input().split()
#     print (arr)
#     if arr:
#         s = max(arr)
#         print(list(filter(lambda a: a != s, arr)))

# if __name__ == '__main__':
#     slist=[]
#     scorelist=[]
#     record=[]
#     for _ in range(int(input())):
#         name = input()
#         record.append(name)
#         score = float(input())
#         record.append(score)
#         scorelist.append(score)
#         slist.append(record)
#     scorelist.sort()
#     ms = scorelist[0]
#     for i in slist:
#         if i[1]== ms:
#             slist.remove(i)
#             scorelist.remove(ms)
#     slist.sort()
#     ms = scorelist[0]
#     for i in slist:
#         if i[1] == ms:
#             print (i[0])

# import sys


# s,t = input().strip().split(' ')
# s,t = [int(s),int(t)]
# a,b = input().strip().split(' ')
# a,b = [int(a),int(b)]
# m,n = input().strip().split(' ')
# m,n = [int(m),int(n)]
# apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
# orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
# ac,oc=0,0
# for i in apple:
#     if s <= a+i and a+i <= t:
#         ac+=1
# for j in orange:
#     if b >= b+j and b+j >= s:
#         oc+=1
# print (ac)
# print (oc)


# import sys
# v = int(sys.stdin.readline())
# n = int(sys.stdin.readline())
# ar = list(map(int,sys.stdin.readline().split()))
# print(ar.index(v))

# import sys
# n=int(sys.stdin.readline())
# ar=list(map(int,sys.stdin.readline().split()))
# s=ar[n-1]
# for i in range(n-1,0,-1):
#     if s<ar[i-1]: 
#         ar[i]=ar[i-1]

#     else:
#         ar[i]=s
#         break
    
#     sys.stdout.write(" ".join(str(x) for x in ar))
#     print()
#     if i==1:
#         ar[i-1]=s
#         # sys.stdout.write(" ".join(str(x) for x in ar))
#         # print()
# sys.stdout.write(" ".join(str(x) for x in ar))

# import sys


# s,t = input().strip().split(' ')
# s,t = [int(s),int(t)]
# a,b = input().strip().split(' ')
# a,b = [int(a),int(b)]
# m,n = input().strip().split(' ')
# m,n = [int(m),int(n)]
# apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
# orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
# ac,oc=0,0
# l,m=[],[]
# for i in apple:
#     l.append(a+i)
# for j in orange:
#     m.append(j+b)
# for k in l:
#     if k in range(s,t+1):
#         ac+=1
# for n in m:
#     if n in range(s,t+1):
#         oc+=1
# print (ac)
# print (oc)

# my_dict = {i:MyList.count(i) for i in MyList}

# import sys

# def funnyString(s):
#     r=s[::-1]
#     c=0
#     # print("inside function", s, r)
#     for i in range(1,len(s)):
#         print(i)
#         # print ("ascii of char",s[i],ord(s[i]))
#         print(ord(s[i])-ord(s[i-1]),ord(r[i-1])-ord(r[i]))
#         if abs(ord(s[i])-ord(s[i-1])) == abs(ord(r[i-1])-ord(r[i])):
#             print(ord(s[i])-ord(s[i-1]),ord(r[i-1])-ord(r[i]))
#             c+=1
#         else:
#             return "Not Funny"
#     if c==len(s)-1:
#         return "Funny"

    
# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     # print("inside for loop",s)
#     result = funnyString(s)
#     print(result)


# import sys

# def gemstones(arr):
#     a=tuple(list(arr[0]))
#     for i in range(1,len(arr)):
#         a = (set(a).intersection(list(arr[i])))
#     return a

# n = int(input().strip())
# arr = []
# arr_i = 0
# for arr_i in range(n):
#     arr_t = str(input().strip())
#     arr.append(arr_t)
# result = gemstones(arr)
# print(result)



#######@@@@@@@ Stock Maximize @@@@@@@@@@@########## 
# import sys

# if __name__ == "__main__":
#     t = int(input().strip())
#     for a0 in range(t):
#         n = int(input().strip())
#         arr = list(map(int, input().strip().split(' ')))
#         # print (arr)
#         profit=0
#         m = max(arr)
#         # print(m)
#         buy = 0
#         length=len(arr)
#         i=0
#         sa = 0 
#         while i<length :
#             # print ("length", length)
#             # print ("for loop", i)
#             if arr[i] == m:
#                 profit=profit+(arr[i]*buy)
#                 buy=0
#                 del arr[0:i+1]
#                 # print ("array after deletion",arr)
#                 if arr:
#                     m=max(arr)
#                 length=length-i-1
#                 i=0
#                 # print("length after profit",length)
#                 print("inside if profit",profit)
#                 continue
#             else:
#                 buy = buy + 1
#                 sa = sa+arr[i]
#                 print ("sum = ",sa)
#                 # print("buy", buy)
#             i+=1
#             # print ("i",i)
#         profit = profit-sa
#         print(profit)



# import sys

# def getTotalX(a, b):
#     # Complete this function
#     i=max(a)
#     k=1
#     c=a+b
#     count=0
#     l=len(a)+len(b)
#     print ("@@@@",len(a),len(b),l)
#     while i<min(b)+1:
#         print("i@##@#@#:",i)
#         j=0
#         while j < l:

#             print("j:",j)
#             if j<len(a):
#                 if i%c[j] != 0:
#                     break
#             else :
#                 if c[j]%i != 0:
#                     break
#             if j==l-1:
#                 count+=1
#                print("count",count)
#             j+=1
#         k+=1
#         i=max(a)*k
        
#     return count

# if __name__ == "__main__":
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     a = list(map(int, input().strip().split(' ')))
#     b = list(map(int, input().strip().split(' ')))
#     total = getTotalX(a, b)
#     print(total)

# r=[]
# for l in open("test.file").read().split("\n"):
#     if l.startswith("error: "):
#         r.append(l)
# print(r)

# r=[l for l in open("test.file") if l.startswith("error: ")]
# print(r)
# r=filter(lambda l: l.startswith("error:"),open ("test.file").readlines())
# print(r)

# re="python"
# r="True!" when re=="python" else "false"
# print (r)

# import re
# s="ha"
# s1="ha haha ha ha "
# s2="ha ha ha ha ha "
# a = re.match("ha *",s1)
# print (a)

# for n in range(2,10):
#     for i in range(2,n):
#         if n%i==0:
#             break
#     else:
#         print (n)

# v=[[1,2],[3,4],[5,6],[7,8],[9,10]]
# d=(x for y in v for x in y if x%2 ==0 )

# import sys
# import math
# def andProduct(a,b):
#     a = ar[0]
#     i=0
#     if a == 0:
#         return 0
#     if not int(math.log(ar[0],2)) == int(math.log(ar[1],2)):
#         return 0
#     while a+2**i <= b:
#         a = a & a+(2**i)
#         i+=1
#     return a
    
# n=int(sys.stdin.readline())
# for i in range(n):
#     ar = list(map(int, sys.stdin.readline().split()))
#     print(andProduct(ar[0],ar[1]))
    
# import math
# def getXOR(l,r):
#     v = int(math.log(l,2))
#     sl=0

#     # if l>4:
#     #     seq = 2**v
#     #     for i in range((2**v)-1,r+1):
#     #         seq = seq^(i)
#     #         if i >= l:
#     #             sl = sl^seq
#     #     return sl
#     # else:
#     seq=0
#     for i in range(r+1):
#         seq = seq^(i)
#         if i >= l:
#             sl = sl^seq
#     return sl
# Q = int(input().strip())
# for a0 in range(Q):
#     L,R = input().strip().split(' ')
#     L,R = [int(L),int(R)]
#     result = getXOR(L,R)
#     print(result)


# import math
# def getXOR(l,r):
#     sl=0
#     seq=0
#     if l>3:
#         p=int(math.log(l,2))

#         for i in range(2**p,r+1):
#             seq = seq^(i)
#             if i>=l:
#                 sl = sl^seq
#     else:
#         for i in range(r+1):
#             seq = seq^(i)
#             if i>=l:
#                 sl = sl^seq
#     return sl
# Q = int(input().strip())
# for a0 in range(Q):
#     L,R = input().strip().split(' ')
#     L,R = [int(L),int(R)]
#     result = getXOR(L,R)
#     print(result)

# arr = []
# a=[]
# for arr_i in range(6):
#     arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#     arr.append(arr_t)
# for i in range(4):
#     for j in range(4):
#         hourglass=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][i+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
#         print(arr[i][j],arr[i][j+1],arr[i][j+2])
#         print(" ",arr[i+1][j+1])
#         print(arr[i+2][j],arr[i+2][j+1],arr[i+2][j+2])
#         print()
#         a.append(hourglass)
#         print (hourglass)
# print(max(a))


# import itertools
# s_len = int(input().strip())
# s = input().strip()
# print(s)
# new_s = ''
# set_s = ''.join(set(s))
# l = len(set_s)
# count=0
# max_l = 0
# if l>1:
#     print("inside first if")
#     pair=list(itertools.combinations(set_s, l-2))
#     for i in pair:
#         print (len(i))
#         new_s = s
#         for k in range(len(i)):
#             print("inside for lopp ", i)
#             new_s = new_s.replace(i[k] ,"")
#         j=0
#         while j<(len(new_s)-1):
#             print("inside while loop ",j)
#             if new_s[j]==new_s[j+1]:
#                 print("inside while if ")
#                 break
#             else:
#                 j+=1
#                 if j==len(new_s)-1:
#                     if max_l<len(new_s):
#                        max_l = len(new_s)
#                     print ("lenght",max_l)
# else:
#     max_l=0

# print (max_l)

# n = int(input().strip())
# s = input().strip()
# k = int(input().strip())
# a=""
# for i in s:
#     if i.isalpha() and i.islower():
#         if ord(i)+k%26 >122:
#             print(ord(i)+k%26-26)
#             a+=chr(ord(i)+(k%26)-26)
#         else:
#             a+=chr(ord(i)+k%26)
#     elif i.isalpha() and i.isupper():
#         if ord(i)+k%26 >90:
#             a+=chr(ord(i)+(k%26)-26)
#         else:
#             a+=chr(ord(i)+k%26)
#     else:
#         a+=i
# print(a)


# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     h = "hackerrank"
#     j=0
#     a=""
#     flag=False
#     for i in s:
#         if h[j]==i:
#             j+=1
#             a+=i
#         if a==h:
#             flag=True
#             print("YES")
#             break
#     if not flag:
#         print("NO")


# q = input()
# count=0
# c = [i for i in range(97,123)]
# for i in q:
#     if ord(i.lower()) in c:
#         count+=1
#         c.remove(ord(i))
# if count == 25:
#     print("pangram")
# else:
#     print("not pangram")

# t = int(input().strip())
# initial = 3
# counter = 4
# for i in range(1,t+1):
#     counter-=1
#     if i==t:
#         print(counter)
#     if counter == 1 :
#         counter = 2*initial+1
#         initial = 2*initial

# s = input().strip()
# n = int(input().strip())
# l=[]
# for i in range(n):
#     if s[i] != s[i+1]:
#         l.append(ord(s[i]-96))
# for a0 in range(n):
#     x = int(input().strip())


# def getXOR(l):
#     a=(l)%8
#     if a==0 or a==1:
#         return l
#     elif a==2 or a==3:
#         return 2
#     elif a==4 or a==5:
#         return l+2
#     else:
#         return 0
#
# Q = int(input().strip())
# for a0 in range(Q):
#     L,R = input().strip().split(' ')
#     L,R = [int(L),int(R)]
#     result = getXOR(L-1)^getXOR(R)
#     print(result)


# def theLoveLetterMystery(s):
#     re = s[::-1]
#     c=0
#     if s == re:
#         return 0
#     else:
#         for i in range(len(s)//2):
#             if ord(s[i]) != ord(s[len(s)-1-i]):
#                 c+=abs(ord(s[len(s)-1-i])-ord(s[i]))
#         return c
#
# q = int(input().strip())
# for a0 in range(q):
#     s = input().strip()
#     result = theLoveLetterMystery(s)
#     print(result)



# q=int(input())
# for q0 in range(q):
#     m=int(input())
#     n=int(input())
#     c=input().split()
#     for i in range(n):
#         for j in range(n):
#             if (int(c[i])+int(c[j])) == m and i!=join7:
#             	print(i,j)


# def gameOfThrones(s):
# 	count=0
# 	a = [0 for i in range(26)]
# 	for i in s:
# 		a[ord(i)%97]+=1
# 	for j in a:
# 		if j%2!=0:
# 			count+=1
		
# 	if count>1:
# 		return "NO"
# 	else:
# 		return "YES"
# s = input().strip()
# result = gameOfThrones(s)
# print(result)


# from collections import Counter

# def isValid(s):
# 	l=[]
# 	a=Counter(s)
# 	print(a)
# 	for k,v in a.items():
# 		l.append(v)
# 	l.sort()
# 	print(l)
# 	if Counter(l)[1]>1 or len(Counter(l))>2:
# 		return "NO" 
# 	else:
# 		for i in range(len(l)-1):
# 			if l[i+1]-l[i]>1:
# 				return "NO"
# 		return "YES"

# s = input().strip()
# result = isValid(s)
# print(result)

# i, j, k = input().strip().split(' ')
# i, j, k = int(i), int(j), int(k)
# count = 0
# for n in range(i,j+1):
# 	rev = 0
# 	no = n
# 	while(n > 0):
# 		rem = n %10
# 		rev = (rev *10) + rem
# 		n = n //10
# 	if abs(no-rev)%k == 0:
# 		count += 1
# print(count)


# n = int(input())
# while n > 0:
#     string = input().strip()
#     k = int(input())
#     s = sorted(list(set([string[i:j] for i in range(len(string)+1) for j in range(n+1) if i < j])))
#     joined_string = "".join(s)
#     print(joined_string[k])
#     n-=1

# for _ in range(int(input())):
#     Str = input().strip()
#     n = len(Str)
#     k = int(input())
#     subStrings = sorted(list(set([Str[start:stop] for start in range(n + 1) for stop in range(n + 1) if start < stop])))
#     result = "".join(subStrings)

#     print (result[k-1])



n ,m = input().strip().split()
a = input().strip().split()

for i in range(int(n)-1,0,-1):
    if int(a[i]) == int(m):
        print(i)
    else:
        print('-1')

#####@@@@@@@@@@@HEllo #####
