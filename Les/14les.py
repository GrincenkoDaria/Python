a={
  'moskva': 495,
  'piter': 812,
  'penza': 8412
}
b= [['moskva', 495],['piter', 812], ['penza', 8412]]
c = dict(moskva=495, piter=812,penza=8412)
d = dict(b)
q = dict.fromkeys(['a','b','c'],100)
print(a)
print(c)
print(d)
print(q)
print(a['moskva'])
a[4]='four'
print(a)
a[4]='štyri'
print(a)
del a[4]
print(a)

s = input()
d ={}
for i in s:
  if i.isalpha():
    d[i]=d.get(i,0)+1
for i in sorted(d):
  print(i,d[i])
  
words={}
while True:
  s =input()
  if s in words:
    print('slovo',s,'perevoditca kak',words[s])
  else:
    print('vvedite perevod slova',s)
    words[s] =input()