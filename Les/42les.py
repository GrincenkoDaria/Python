import pprint
import calendar
import math as m
def say(name):
  print(f"Hello, {name}")
  
def summa(*args):
  return sum(args)

def factorial(n):
  pr=1
  for i in range(1, n +1):
    pr *= i
  return pr
my_str = "YOU'RE BREATHTAKING!"
my_num1 = 2
my_num2 = 3

pprint.pprint(locals())
c = calendar.TextCalendar()
print(c.formatyear(2022))

pprint.pprint(dir(m))
