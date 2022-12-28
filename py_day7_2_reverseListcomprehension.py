# use dictionary comprehension
#to count the length of each word in a sentence.





string='''
Practice problems for list com per hension in Python.
'''


wordsLst=string.split(' ')
print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst ]
print(wordsLst)
#ans={word:len(word) for word in wordLst }
ans={i:i[::-1]  for i in wordsLst }
print(ans)

