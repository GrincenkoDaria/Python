from typing import Counter


print(19/5)
print(19//5)
print(-19//5)
print(19//-5)
print(-19//-5)
print(19//5)
print(-19%5)
print(19%-5)
print(-19% -5)

a = list(map(int,input().split()))

print(a)

def append_to_list(value, my_list=None):
  if my_list  is None:
    my_list=[]
  my_list.append(value)
  print(my_list)
  
append_to_list(77,[3,4])
append_to_list(34)
append_to_list(794 )
