def f(a,b):
  a=100
  b=200
  s.append(100)
  print(a,b, "local")
  
c,d=20,50
s=[1,2,354,3,54,3]
f(c,d)
print(c,d,"global")
print(s)

def f(a,b,c=None):
  print(a,b,c)
  
f(1,2,3)
f(1,2)
f(b=10,c=20,a=40)