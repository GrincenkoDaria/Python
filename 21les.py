a,*b,c=[3,5,6,"hello",32]
print(a,b,c)

s=[2,14,2]
print(list(range(1,5)))
print(list(range(*s)))

def f(a,b,c,d):
  print(a,b,c,d)

f(1,2,3,4)
a=("hi",True, 34, [1,2232,3])
f(*a)

def f(*args):
  print(args)
  s=0
  for i in args:
    s+=1
  return s
  
print(f(1,2,32,312,1,3))
f(1,2,32,312,1,3)
def f(*args,**kwargs):
  print(args,kwargs)
f(1,2,3,a=3,d=1,e=30)

def outPrint(*args,sep="#",end="&"):
  print(args,sep,end)
  
outPrint(1,2,3,4,sep="90")

a=[1,2,3,34]
print(*a)