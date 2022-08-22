from typing import List
set={i for i in range(1,6)}
print(set)

set={i for i in [1,1,2,2,3,2,4,3,4,6,9,0]}
print(set)

set={i for i in "abcdabcd"}
print(set)

set={i for i in ["abcdabcd","Hi",'Hello','Python',"Hello"] if len(i) > 3}
print(set)

set={i+j+q for i in "123" for j in "123" for q in "123"}
print(set)

set=[i+j+q for i in "123" for j in "123" for q in "123"]
print(set)

set={(i,j)for i in "12" for j in "13"}
print(set)

set=[[i,j]for i in "12" for j in "23"]
print(set)
#guufyur4ugti3eruiweoiekujekd
"""kifieifre
ief3eifuj//"""
help(print)

def fun(a:int,b:int)->int:
  """Funkcia skladyvaet 
        a i b"""
  print(a+b)
  
help(fun)

class cl:
  """class
  CLASS
  cLAsS"""
  pass

help(cl)

hi:int = 100
print(hi)
hi = "abc"
print(hi)
print(fun.__annotations__)

def l(list: List[str]):
  for elem in list:
    print(elem.upper())
    
    
l(["isdid","odis"])