
x=int(input())
a = x//10000
b = x//1000%10
c = x//100%10
d = x//10%10
e = x%10
print(a,b,c,d,e)

time=int(input())
res=time%1440
h=time//60%24
min=time%60
day=time//60//24+1
print(day,"day",h,":",min)

day2=int(input())
km=int(input())
print(round(km/day2))