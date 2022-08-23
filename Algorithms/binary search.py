from math import ceil
def bin(list:list,item:int):
  low = 0
  high = len(list)-1
  
  while low <= high:
    mid = ceil((low +high)/2)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid -1
    else:
      low = mid + 1
  return None

my_list = [1,3,5,7,9]

print(bin(my_list, 3))
print(bin(my_list, -1))
