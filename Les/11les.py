a=[[1,2,4,50],[1,5,9,13],[1,5,777,[2,3,4],65]]
b =['hi','hello','Python']
print(len(a))
print(a[0])
print(a[1][-1])
print(a[2][3][2])
print(b[2][-1])
a=[[3,2,4,40],[1,5,9,13],[1,5,7,65]]
for i in a:
  for j in i:
    print(j,end=' ')
  print()

q=[]
n=int(input())
m=int(input())

for i in range(n):
  b=[]
  for i in range(m):
    b.append(int(input()))
  q.append(b)
for i in q:
  print(i)
  
  
a=[]
n=int(input())
for i in range(n):
  a.append([0]*n)

for i in range(n):
  for j in range(n):
    if i==j:
      a[i][j]=10
    elif i>j:
      a[i][j]=3
    else:
      a[i][j]=5
for i in a:
  print(i)
  