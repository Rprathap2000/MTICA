sample_dict={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"new york"}
keys=["name","salary"]
##newdict={}
##for i in keys:
##    newdict[i]=sample_dict[i]
##print(newdict)
newdict={i:sample_dict[i] for i in keys}
print(newdict)
