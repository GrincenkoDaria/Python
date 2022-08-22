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
    
    
l(["isdid","odis "])




#file = open('passwords.txt', 'w')
# file.write([1,2,3])
#file.close


#list = []
# for i in range(10000):
#   file = open('passwords.txt', 'w')
#   list.append(file)
#   file. close

#with poen('passwords.txt', 'w')as f:
#   f.write("1223")
#   f.write("hello")
#print(f.writ("22222"))

#import os

#with os.scandir('..') as entries:
#   for i in entries:
#   print(i.name, "->", entry.stat().st_size. "bytes")

#with balance_lock:
#   pass

#import aiohttp
#import asyncio

#async def main():
#  async with aiohttp.ClientSession() as session:
#    async with session.get("http://python.org") as response:

#      print("Status", response.status)
#      print("Content-type", response.headers['content-type'])
 
#      html = await response.text()
#      print('Body', html[:15]. -...-)

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())

















