def findlcm(rohith,prathap):
    if rohith<0 or prathap<0:
        return "INVALID"
    if rohith>prathap:
        rohith,prathap=prathap,rohith
    i=prathap
    while True:
        if i%rohith==0 and i%prathap==0:
            return i
        else:
            i+=1
    return None
        
print("Enter two numbers")
rohith=int(input())
prathap=int(input())
print(findlcm(rohith,prathap))
