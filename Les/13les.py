a=set('asdasdasdfgfgdsdasd')
print(a)
s= set(range(5))
print(s)
q=set()
print(q,type(q))
b=[1,2,3,1,2,2,4,4,3,2,1,3,1,3,3,3,4,5,6]
b=list(set(b))
print(b)
c={1,2,3,4}
c.add(6)
c.add(3)
c.update([5,6,7,8,9])
c.discard(1)
print(3 in c,100 in c)
print(c)
a={1,2,3,4,5}
b={3,4,5,6,7}
print(a&b)
print(a|b)
print(a^b)
print(a==b)
text = input()
a=set()
while text!='':
  slova = text.split()
  a.update(slova)
  print(a)
  text=input()
