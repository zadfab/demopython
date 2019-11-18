file1=open("zad.txt","rb")

file2=open('py.bat','wb')

for j in file1:
    file2.write(j)
file3=open('py.bat',"rb")
print(file3.read())


import os
import time

class Open:
    def openfile(self):
        try:
            os.startfile('zad.txt')
        except Exception as e:
            print (e)

obj=Open()
obj.openfile()


time.sleep(2)


def closefile():
    try:
        os.system('TASKKILL /F /IM spotify.exe')
    except Exception as e:
        print(e)

closefile()





