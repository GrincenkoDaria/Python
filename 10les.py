import random


a =[1,0,2,3,4,1,2,2,3,0,4,5,3,2,4,2,1,5,0]
count=[0]*6
for i in a:
  count[i]+=1
print(count)

s="kdlgfxhc c gpf'hf.bgec,.DFRSGFdzfrzzzccccztgerhgrt hvtu j7iytj  hgnghj5tusfGRJFRG W'|D''s;ldao"
let=[0]*26
for i in s.lower():
  if i>='a' and i<='z':
    nomer=ord(i)-97
    let[nomer]+=1
    
for i in range(26):
  if let[i]>0:
    print(chr(i+97)*let[i],end='')
  
  
  
b=[]
for i in range(10):
  b.append(random.randint(-10,10))
count = [0]*21
for i in b:
  count[i+10]+=1
print(b)
for i in range(21):
  if count[i]>0:
    print(i-10,count[i])
    
    


for i in range(3):
  for j in range(6):
    print(i, end='')
  print()
  
k=0
for b1 in 'tykva':
  for b2 in 'tykva':
    for b3 in 'tykva':
      for b4 in 'tykva':
        for b5 in 'tykva':
          for b6 in 'tykva':
            rez =b1+b2+b3+b4+b5+b6
            if rez[0] in'tkv' and rez[-1] in'tkv':
              if rez.count('a')+rez.count('u')==2:
                print(rez)
                k+=1
print(k)
  
for i in range(1,1001):
  s=0
  x=i
  while x >0:   
    s += x%10
    x//=10
  print(i,s)