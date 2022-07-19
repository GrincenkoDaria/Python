from math import ceil, floor
from ntpath import join
from posixpath import split


print(floor(3.9))
print(ceil(3.999999999999999))

hi = "hEllo"
num1="12,22"
num2="123"
jaz="JS PYTHON JAVA"
jazlist=['JS', 'PYTHON', 'JAVA']
print( "",hi, '\n',
	hi.upper(),'\n',
  hi.lower(),'\n',
   hi.count("l"),'\n',
   hi.count("l",1,3),'\n',
   hi.find('3'),'\n',
   hi.replace("l","?"),'\n',
   hi.replace("l","",1),'\n',
   num1.isdigit(),'\n' ,
    num2.isdigit(),'\n',
     num2.ljust(6,"1"),'\n',
     jaz.split(),'\n',
     num1.split(","),'\n',
     "/".join(jazlist))