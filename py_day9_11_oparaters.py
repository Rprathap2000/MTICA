X1=5
Y1=5
X2='Hello'
y2='Hello'
x3=[1,2,3]
y3=[1,2,3]
print(X1 is not Y1)
print(X2 is y2)
print(x3 is y3)

#check if 'H' is present in message string 
message='Hello World'#prints True
dict1={1:'a',2:'b'}

#check if 'hello' is present in message string
print('hello' not in message)#prints True

#check if '1' is present in dict1
print(1 in dict1)#prints True

#check if 'a' key is present in dict1
print('a' in dict1)#prints False


lst1=[10,20,30,'c','Java','Python']
print('Java' in lst1)
print('R' in lst1)
print('R' not in lst1)

#logical AND
print(True and True)#True
print(True and False)#False

#logical OR
print(True or False)#True


#logical NOT
print(not True)#False

a=5
b=6
print((a>2) and (b>=6))#True

x=10
y=4
print('x=',x,'y=',y,'x&y=',x&y)
print('x=',x,'y=',y,'x|y=',x|y)
print('x=',x,'~x=',~x)
print('x=',x,'y=',y,'x^y=',x^y)
print('x=',x,'x>>2=',x>>2)
print('x=',x,'x<<2=',x<<2)
