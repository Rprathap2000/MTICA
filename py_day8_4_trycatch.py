n1=input("Enter the first number:")
n2=input("Enter the second number:")
try:
    res=int(n1)/int(n2)
except ZeroDivisionError:
    print("Exception handeld by Rohith")
except ValueError:
    print("Exception handeld by Prathp")
except Exception as ob:
    print(ob)
else:
    print(n1, '/' , n2, '=', res)
finally:
    print("Thanks")
print("Visit again at python class at MTICA")
