from datetime import datetime
def m(name):
  def i():
    print("hello!",name)
  return i
r = m("Rita")
v = m("Vas\'a")
r()
v()

def add(value):
  def inn(a):
    return value+a
  return inn

a = add(5)
print(a(6))

def counter():
  count=0
  def inn():
    nonlocal count
    count +=1
    print(count)
    return count
  return inn
q = counter()
q()
q()
q()

def num():
  numbers = []
  def inn(number):
    numbers.append(number)
    return sum(numbers)/len(numbers)
  return inn

r1 = num()
r1(9)
r1(1)
r1(4)
r1(2)

def time():
  start = datetime.now()
  def inn():
    print(datetime.now() - start)
  inn()
  
r=time()