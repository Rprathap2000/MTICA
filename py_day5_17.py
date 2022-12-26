def remove_duplicate(s):
    s1=' '
    for i in s:
        if i not in s1:
            s1 +=i
            #print(s1)
    return s1
a=input("Enter your text:")
print("without duplicate: ",remove_duplicate(a))
