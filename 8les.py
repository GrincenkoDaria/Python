i=1
while i<7:
  print(i)
  i=i+1

a=int(input())
while a!=0:
  print("ERROR")
  a=int(input())
  
b=[1,2,3]*10
print(b)
while 3 in b:
  b.remove(3)
  print(b)
  
  
s="lkdoeikl;fiJLKJLe3w3jfkud9 io"
while len(s)>0:
  buk=s[0]
  if buk>='a' and buk<='z':
    print(buk,"small")
  elif buk.isdigit():
    print(buk,"digit")
  elif buk>='A' and buk<='Z':
    print(buk,"BIG")
  else: 
    print(buk,"znak")
  s=s[1:]
  
x=int(input())
k=0
while x>0:
  print(x%10)
  k=k+1
  x=x//10
print("all",k,"digit")


x=int(input())
while x>0:
  l=x%2
  print(l)
  x=x//2
  
  
a=int(input())
b=int(input())
while a!=b:
  if a>b:
    a=a-b
  else:
    b=b-a
print(a)
while b>0:
  a,b = b,a%b
print(a)

n=int(input())
i=1
a=[]
while i*i<=n:
  if n%i==0:
    a.append(i)
    if i!=n//i:
      a.append(n//i)
 
  i+=1
a.sort()
print(a)

i=1
while i>0:
  print(i)
  i+=1
  if i==10:
    break
  
while True:
  a=input()
  if a=='break':
    break
  print(a, len(a))
  
  
a=[2,2,34,56,78,90]
while len(a)>0:
    last=a.pop()
    if last%2!=0:
      print('NO')
      break
else:
  print('Yes')