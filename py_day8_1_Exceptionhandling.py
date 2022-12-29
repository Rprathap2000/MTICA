##def KelvinToFahrenheit(Temperature):
##    assert (Temperature>=0),"Colder than absolute zero at MTICA"
##    res=((Temperature-273)*1.8)+32
##    return res
##try:
##    print(KelvinToFahrenheit(-50))
##except Exception as ob:
##    print(ob)
##try:
##    print(KelvinToFahrenheit(273))
##except Exception as ob:
##    print(ob)
##try:
##    print(KelvinToFahrenheit(505.78))
##except Exception as ob:
##    print(ob)
##try:
##    print(KelvinToFahrenheit(-5))
##except Exception as ob:
##    print(ob)
##print("Thank You")




def Fact(n):
    assert (n>=0),"Factioral of negitive num is not defined"
    assert (isinstance(n,int)),"Factioreal not defined for non integer"
    if n==0:
        return 1
    else:
        return n*Fact(n-1)
    
try:
    print(Fact(0.548))
except Exception as ob:
    print(ob)
try:
    print(Fact(-3))
except Exception as ob:
    print(ob)
try:
    print(Fact(45))
except Exception as ob:
    print(ob)

print("Thank You")


