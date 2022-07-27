import os

path ='C:\\Users\\Daria\\Desktop\\Projekt'
name='Pomoc.css'
print(os.listdir(path))

def ob(path,name):
  for i in os.listdir(path):
    if i == name:
      print("content:",path+"\\"+i)
    if os.path.isdir(path+'\\'+i):
      ob(path+'\\'+i,name)
      
ob(path,name)