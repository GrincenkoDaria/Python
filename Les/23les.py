def rec(s):
  if len(s)==1 or len(s)==2:
    return s
  return s[0]+'('+rec(s[1:-1]) + ')' +s[-1]

s=input()
print(rec(s))

def rec(s):
  if len(s)==0:
    return s
  if s[0] =="(": 
    return s[0]+rec(s[1:])+")"
  return s[0]+rec(s[1:])+s[0]
 
s=input()
print(rec(s))

def power(x,n):
  if n==0:
    return 1
  if n<0:
    return 1/power(x,-n)
  if n%2==0:
    return power(x,n//2)*power(x,n//2)
  else:
    return power (x,n-1)*x
  
x=int(input())
n=int(input())

print(power(x,n))

a=[1,23,31,[1,2],[1,2,1,2,[1,3,[34,5,78,[34,434]]]]]

def rec (sp,level=1):
  print(*sp,"level=",level)
  for i in sp:
    if type(i)==list:
      rec(i,level+1)
      
rec(a)