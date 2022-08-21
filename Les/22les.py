def rec(x):
	if x<10:
		print(x)
		rec(x+1)
		print(x)
  	
  
rec(1)

def fib(n):
  if n==1:
    return 0
  if n==2:
    return 1
  return fib(n-1)+fib(n-2)
print(fib(9))

def pal(s):
  if len(s)<=1:
    return True
  if s[0] != s[-1]:
    return False
  return pal(s[1:-1])

print(pal("qwerrewq"))
print(pal("qwersewq"))