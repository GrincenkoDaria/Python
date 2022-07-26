def sq(x):
  return x**2
a = sq(210)
print(a)

def even(x):
  return x%2==0
   

for i in range(1,22,3):
  print(i,even(i))
  
  
def factor(n):
  p = 1
  for i in range(2,n+1):
    p=p*i
  return p

def sochet(n,k):
  return factor(n)/(factor(k)*factor(n-k))

print(sochet(10,3))
  