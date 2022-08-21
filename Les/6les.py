dariaznamky=[1,2,1,1,2,1,3,1,1,1]
pavelznamky=[1,1,2,1,3]
a=[True, "hello!", 1.2,[1,6]]
b=[]
print(dariaznamky,'\n',
  len(dariaznamky),'\n',
  dariaznamky+pavelznamky,'\n',
  a,'\n',
  len(a),'\n',
  b,'\n',
  b+[4],'\n',
  type(b),'\n',
  [0]*8,'\n',
  1.2 in a,'\n',
  min(dariaznamky),'\n',
  sum(pavelznamky),'\n',
  sorted(dariaznamky),'\n',
  sorted(pavelznamky,reverse=True),'\n',
  pavelznamky>dariaznamky,'\n',
  sum(dariaznamky)/len(dariaznamky),'\n',
  sum(pavelznamky)/len(pavelznamky))

a=[46,5,6,777,3]
print(a[3:])
print(a[::2])
print(a[::-1])
a[3:5]=100,76,4,46
print(a)
print(a[3:])
del a[1]
print(a)

a.append(46)
b=a.copy()
a.clear()
print(a)
print(b.count(46))
print(b.index(100))
print(b.index(46,2,-1))
b.insert(3,8)
print(b)
last=b.pop()
print(last)
b.remove(100)
print(b)
b.sort()
print(b)
b.sort(reverse=True)
print(b)