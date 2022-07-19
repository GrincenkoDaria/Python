x=int(input())
b=200
if x>=b:
  print(True)
else:
  print(False)
  
a=int(input())
b=int(input())
c=a
if a<b:
  c=b
print(c)
if a>b:
  a,b=b,a
print(a,b)

x=int(input())
y=int(input())
if x>0:
  if y>0:
    print(1)
  else:
    print(4)
else:
  if y>0:
    print(2)
  else:
    print(3)
    

a=int(input())
if a<0 or a>=100000:
  print('ERROR!!!')
elif a<10:
  print('1 digit')
elif a<100:
  print('2 digit')
elif a<1000:
  print('3 digit')
elif a<10000:
  print('4 digit')
elif a<100000:
  print('5 digit')
