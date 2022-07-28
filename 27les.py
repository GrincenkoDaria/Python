def f(x):
  return x**2

r=lambda x: x**2
print(r(7))
print(f(4))

t = lambda x: "positive" if x>0 else "negative"
print(t(2))
print(t(-2))

def f(x):
  return x%10

a=[78,76,53,543,676,32,553,1,3,11333,888880]
a.sort(key=f)
print(a)

a.sort(key=lambda x: x//10%10)
print(a)

def linear(k,b):
  return lambda x: x*k+b

graf1 =linear(2,5)
print(graf1(5))