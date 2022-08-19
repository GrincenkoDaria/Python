def header(func):
  def inn(*args, **kwargs):
    print('<h1>')
    func(*args, **kwargs)
    print('</h1>')
  return inn

def table(func):
  def inn(*args, **kwargs):
    print('<table>')
    func(*args, **kwargs)
    print('</table>')
  return inn
@table
@header
def say(name,surname,age):
  print('hello ',name,surname,age)


print(say)
say("Vasya","Ivanov", 30)