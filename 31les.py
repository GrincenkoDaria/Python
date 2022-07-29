#map
def f(x):
  return x**3

a = [-1,2,3,-4,5]
b = list(map(abs,a))
c = list(map(f,a))
print(b)
print(c)

a = ["js","python", "c++"]
b = list(map(str.upper,a))
print(b)

b = list(map(lambda x: x[::-1],a))
print(b)
c = list(map(sorted,b))
print(c)

s = input().split()
print(s)