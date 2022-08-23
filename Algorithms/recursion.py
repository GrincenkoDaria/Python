def look_for_key(box):
  for i in box:
    if i.is_abox():
      look_for_key(i)
    elif i.is_a_key():
      print("found the key!")
      
def countdown(i):
  print(i, end="...")
  if i <= 1:
    return 
  else:
    countdown(i-1)
  print()
countdown(3)
def greet2(name):
  print('how are you, ' + name + '?')
  
def bye():
  print('ok bye!')

def greet(name):
  print("hello, "+ name + "!")
  greet2(name)
  print('getting ready to say bye...')
  bye()
 
greet("Daria")

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)
  
print(fact(3))