f = open('1les.py','a+',encoding='utf-8')
#r"C:\Users\Daria\Desktop\Python\1les.py"
print(f.read(30))
print(f.read(30))
print(f.read(30))
f.seek(0)
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(0)
for row in f:
  print(row)
  
f.seek(0)
for row in f:
  for i in row:
    print(i)
    
f.seek(0)
s= f.readlines()
print(s)

f.write ('b=\'hi\'\n')
f.close