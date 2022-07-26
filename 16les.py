def say():
  print("HI!")
  print("<(-C_-)>")
  
say()

def square(x):
  print(x**2)
  
for i in range(1,11):
  square(i)
  
def multi(a,b):
  print(a*b)
  
multi(2,3)
  
def factor(n):
  p = 1
  for i in range(2,n+1):
    p=p*i
  print(p)
  
factor(5)