a = [4,-2,44,32,32,1,-32,132,-3232]
b='hello'
c =('hi','hello', 'Python')

a.sort()
print(a)
print(sorted(b))
print(sorted(c))
c =sorted(c,reverse=True)
print(c)
a = [4,-2,44,32,32,1,-32,132,-3232]
print(sorted(a,key =abs))

def f(x):
  return -(x%10), x//10%10
print(sorted(a,key =f))
a =["a 2","Q 13","S 55","z 1","Y 16","x 10","A 2","aAA 32"]
print(sorted(a,key =str.lower))

print(sorted(a, key = lambda x: (int(x.split()[1]), x.split()[0].lower())))
print(sorted(a, key = lambda x: (int(x.split()[1]), x.split()[0].lower()),reverse= True))
 