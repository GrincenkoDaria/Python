#generator
a = [i*2 for i in range(1,10)]
print(a)
a = (i*2 for i in range(1,10))

for i in a:
  print(i)
  
  
c = (i for i in range(100))

print(list(c))
print(list(c))


def f():
  return [43,54,32]

def genf():
  s =7
  for i in [43,65,32]:
    yield i
    print(s)
    s = s*10+7
    
g = genf()
print(next(g))
print(next(g))
print(next(g))

def fact (n):
  pr=1
  for i in range(1, n+1 ):
    pr =pr*i
    yield pr
s=fact(10)
for i in fact(20):
  print(i,end=" ")

