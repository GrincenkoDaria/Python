def f():
  print('Hi')
  
d = lambda : 'hi'
f()
print(d())

class Cat:
  pass
bob=Cat()
print(callable(Cat))
print(callable(bob))

class Cat:
  print('may')
Cat()

