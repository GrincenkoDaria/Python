a={1,2,3,455,}
print(list(enumerate(a)))
s="hello"
t=("apple","mango","banana")
d={"a":1,"b":2,"c":3}
for index,value in enumerate(a):
  print(index,value)
  
for index,value in enumerate(d):
  print(index,value)
  
for index,value in enumerate(t):
  print(index,value)
  
for index,value in enumerate(s):
  print(index,value)
  
for index,value in enumerate(range(10,20)):
  print(index,value)
  
for index,value in enumerate(a,1):
  print(index,value)