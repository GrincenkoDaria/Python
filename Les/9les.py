from random import randint


print(sum(range(10,100,2))) 
a,b,c= range(0,30,10)
print(a,b,c)

v=iter(range(5))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(next(v))
d=iter([61,"dkjskjd", True])
print(next(d))
print(next(d))
print(next(d))

m=iter("ksj")
print(next(m))
print(next(m))
print(next(m))

for i in range(4,34,3):
  print(i)
  
  
for i in range(1,11):
  print(i, i*i)
  
  
n = int(input())
c=1
for i in range(1,n+1):
  c=c*i
print(c)
for i in range(10):
  a = randint(1,100)
  print(a, end=" ")
  
  
print()
for i in range(1,20):
  print("*"*i)


a=[2,2,34,5,78,56,78,90,5]
for i in a:
  print(i)
  input()
  
n=len(a)
for i in range(n):
  print(i, a[i])
  
b=[]
for i in a:
  if not i in b:
    b.append(i)
print(b)