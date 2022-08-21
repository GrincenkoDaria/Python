a=int(input("Первый взнос = "))
year=int(input("Через сколько лет вы заберете свои деньги? "))
while year >= 0:
  a = a/100*110
  print(a)
  year = year - 1 
  
b = int(input("Введите число от 0 до 1000: "))
k = 0
while b>1000 or b<0:
  print("Это число не попадает в диапазон от 0 до 1000")
  b = int(input("Введите число ещё раз: "))


  
for i in range(2, b // 2+1):
  if (b % i == 0):
      k = k+1
if (k <= 0):
  print("Число простое")
else:
  print("Число не является простым")
