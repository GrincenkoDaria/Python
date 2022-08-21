g ='gray'
def colors(param = 'r'):
  y = 'yellow'
  def print_red():
    nonlocal y
    r ='red'
    print(r,y,g)
    y ='changed'
    
  def print_blue():
    g = 'green'
    b ='blue'
    print(b,y,g)
  if param =='r':
    print_red()
  elif param=='b':
    print_blue()
  else:
    print('I dont know this color')
  
colors()
colors("b")
colors(99)