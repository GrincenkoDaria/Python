#zip
a =[1,2,3,4]
b=[12,23,34,45]
c='abcd'
rez= zip(a,b,c)

print(list(rez))
rez= zip(a,b,c)
for i in rez:
  print(i)
rez= zip(a,b,c)
t,t1,t2 = zip(*rez)
print(t,t1,t2)