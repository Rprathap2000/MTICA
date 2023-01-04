a=-5
b=9
try:
    if a<0 or b<0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print("Please enter valid integer value")
