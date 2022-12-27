def extract_vowel(s):
    temp_vowel=' '
    temp_digits=' '
    temp_specialcharecters=' '
    temp_consonents=' '
    for i in s:
        if i in 'AEIOUaeiou':
            temp_vowel+=i
        elif i in '0123456789':
            temp_digits+=i
        elif i in '!@#$%^&*':
            temp_specialcharecters+=i
        else if i in abcdefghio:
           temp_consonents=i
           print("i:",i,"temp_consonents:",temp_consonents)
        l=[]
        l.append(temp_vowel)
        l.append(temp_digits)
        l.append(temp_specialcharecters)
        l.append(temp_specialcharecters)
    return temp_vowel
    return temp_digits
    return temp_specialcharecters
    return temp_specialcharecters
str1=input("Enter the string:")
a=extract_vowel(str1)
print("vowels:",a)
print("etemp_vowel",len(a))
print("temp_digits",len(a))
print("temp_specialcharecters",len(a) )
print("temp_consonents",len(a))

