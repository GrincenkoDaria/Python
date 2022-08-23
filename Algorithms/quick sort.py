
def sum(arr):
  total = 0
  for x in arr:
    total += x
  return total

print(sum([1,2,3,4]))

def sum(l):
  if l ==[]:
    return 0
  return l[0] + sum(l[1:])

print(sum([1,2,3,4]))

def n(l):
  if l ==[]:
    return 0
  return 1 + n(l[1:])

print(n([1,2,3,4]))

def max(l):
  if len(l) ==2:
    return l[0] if l[0] > l[1] else l[1]
  s = max(l[1:])
  return l[0] if l [0] > s else s 

print(max([1,2,3,4]))


def quicksort(array):
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    
    greater = [i for i in array[1:] if i > pivot]
    
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10,2,45,2,456,9]))

def print_i(l):
  for i in l:
    print(i)
    
print_i([1,2,3])

from time import sleep
def print_i2(l):
  for i in l:
    sleep(1)
    print(i)

print('....'*50)
print_i2([1,2,3])