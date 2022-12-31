fo1=open(r"C:\Users\User\Desktop\pythonpractice_45\day_10\py_day10_7.txt","r")
fo2=open(r"C:\Users\User\Desktop\pythonpractice_45\day_10\py_day10_8.txt","w+")


Rohith=fo1.read()
fo2.write(Rohith)

fo1.close()
fo2.close()
print("file copied")
