a, b = 4,6
print(a,b)
a, b = b, a 
print(a,b)

a,b,c= map(float,input().split())

a=int(input())
while 0>a or a>10 :
  print('ERROR')
  a=int(input())
b = 9-a
num = a*100 + 90 + b
print(num)