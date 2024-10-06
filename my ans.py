
#how to reverse a string
'''txt="hello world"[::-1]
print(txt)'''

# by using function
'''def myfn(x):
    return x[::-1]
a=myfn('hello')
print(a)
b=myfn('12345')
print(b)'''
'''x=100
def rev():
    return x[::-1

print(rev())'''
s1="listen"
s2="silent"
def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("string is anangram", s1,"=", s2)
    else:
        print("non anagram")
check(s1,s2)
















#sum of n natural no
"""n= int(input("enter your no"))
sum=0
initial=0
while initial <=n:
    sum =sum +initial
    initial=initial+1
print(n,sum)"""

#how to reverse the no
'''n=int(input("enter your no"))
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("reverse of no ",rev)'''

#check whether string is palindrome
'''st=int(input("enter ur sring"))
if(st==st[::-1]):
    print("string is palindrome")
else:
    print("string is not polindrome")'''
'''lis=[1,1,2,3,3,3,4,4,4,4]
print(list(set(lis)))'''

#sum of digits in number
'''num=int(input("enter ur no"))
sum=0
while num>0:
    sum+=num%10
    num=num//10
print("sum of digits",sum)'''



'''n= int(input("enter ur  no"))
num=[x for x in range(1, n+1)]
add=sum(num)
print("sum of no is", add)'''



# find the dupliucates in list
'''from collections import counter
a=[1,1,1,2,2,2,3,4,5,6]
b=counter(a)
print(b)
for i in b:
    if i>=2:
        print("duplicate",i)
    else :
    print("not duplicate",i)'''

# find no of digits in number
'''num=int(input("ent ur no"))
count=0
while (num>0):
    count=count+1
    num=num//10
print("no of digits in str",count)'''
# how to find duplicates from string
'''s="hi hlo hi hhey,hello hlo"
t=s.split()
print(t)
import collections
def counter(t):
    pass 
u=counter(t)
for i in  u:
    if i>=2:
        print("duplicate ", i) 
    else:
        print("not duplicate")'''
'''m='ranjana is good girl rnt u ranjana'
a=[]
b=[]
for i in m.split():
    if i not in a:
        a.append(i)
    else:
        b.append(i)
print(b)'''
'''l1=[1,1,2,3,3,4,4,5,5,5,6,7]
for i in l1:
    if i not in l1:
        l2.append(i)
    else:
        l3.append(i)
print(l3)
print(l2)'''





#unique records
'''s="hi hlo hi hhey,hello hlo"
t=s.split()
print(t)
print(set(t))'''

#factorial of no
'''n=int(input("enter ur no"))
fact=1
i=1
while i <=n:
    fact=fact*i
    i+=1
print("factorial of ", n,"is", fact)'''

#prime no
'''for num in range(1,100):
    if all (num%i!=0 for i in range(2,num)):
        print(num)'''

#sort asc or desc
#l=[1,2,5,4,3]
#l.sort(reverse=True)
#print(l[1])

#fibonacci series
def f(n):
    if n==0: return 0
    elif n==1: return 1
    else : return f(n-1)+f(n-2)
for i in range(0,12):
    print(f(i))




















