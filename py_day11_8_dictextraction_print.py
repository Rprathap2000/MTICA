sample_d={
    "name":"kelly",
    "age":25,
    "salary":8000,
    "city":"new york"
    }
#keys to remove
keys=["name","salary"]
d=dict()
for i in sample_d.keys()-keys:
    d[i]=sample_d[i]
print(d)
