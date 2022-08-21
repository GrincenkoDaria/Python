import os
path ='C:\\Users\\Daria\\Desktop\\Projekt'
print(os.listdir(path))
def ob(path, level=1):
  print('level=',level,"content",os.listdir(path))
  for i in os.listdir(path):
    if os.path.isdir(path+'\\'+i):
      print('Down',path+'\\'+i)
      ob(path+'\\'+i,level+1)
      print('Up',path)
      
ob(path)