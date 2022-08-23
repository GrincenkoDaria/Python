from array import array


def find(arr):
  sm = arr[0]
  sm_index = 0
  for i in range(1, len(arr)):
    if arr[i] < sm:
      sm = arr[i]
      sm_index = i
  return sm_index

print(find([2,3,2,112,-9]))

def sort(arr):
  newArr = []
  for i in range(len(arr)):
    sm =find(arr)
    newArr.append(arr.pop(sm))
  return newArr

print(sort([34,5451,43,53,-1,2,30,-867]))