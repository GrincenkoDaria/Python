import random
a =[i *5 for i in "hello"]
print(a)

a =[i *5 for i in range(10,20)]
print(a)

a =[random.randint(-10,10)  for i in range(10)]
print(a)

a =[ord(i) for i in "hello"]
print(a)

a =[i *5 for i in "hello"]
print(a)

a = input().split()
a = [int(i) for i in a]
print(a)
n=5
m=30
a=[[0]*m for i in range(n)]
for i in a :
  print(i)
  
a = [i*j for i in [2,3,4,5,6] for j in [1,1,2,3] if i*j>=10]
print(a)
a = [i**3 for i in range(10)]

print(a)