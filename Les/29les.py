a = [
  ("Sidorov", 1995),
  ("Lukov", 1985),
  ("Jahodka", 1970),
  ("Isaev", 2000),
  ("Kozlov", 1996),
  ("Eliseev", 1995),
  ("Chleban", 2008),
  ("Adamec", 2007),
  ("Zubikova", 2008),
  ("Blashko", 2008)
  
]
d =[elem[0] for elem in a]
print(d)
d =[elem[0] for elem in a if elem[1]>2000]
print(d)

a = {
  "Sidorov": {"age":1995, "hobby": "music"},
  "Lukov":{"age": 1985, "hobby": "tennis"},
  "Jahodka":{"age":1970, "hobby": "chess"},

}

b =[(elem,a[elem]['hobby']) for elem in a if a[elem]['age']<1995]
print(b)


s='lsjfklidfkj3j5jwk383u5ihti398u'
b=[i for i in s if i.isdigit()]
print(b)
b=[i for i in s if i.isalpha()]
print(b)

n = 5

a = [[i*j for i in range(1,n)] for j in range(1,n)]
for i in a:
  print(i)





