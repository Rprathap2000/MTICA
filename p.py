def palindromornot(inpu):
    if inpu==inpu[::-1]:
       return 'yes'
    else:
       return 'no'
inpu=input("Enter the element:")
print(palindromornot(inpu))

