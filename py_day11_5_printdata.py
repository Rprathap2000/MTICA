employees=['Manohar','Prasad','Mansa']
defaults={"designation": 'Developer',"salary":80000}
data=dict.fromkeys(employees,defaults)
print(data)
#Individual data
print(data["Mansa"])
