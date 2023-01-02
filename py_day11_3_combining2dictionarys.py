##d1={'ten':10,'twenty':20,'thirty':30}
##d2={'thirty':30,'fourty':40,'fifty':50}
##d3={**d1,**d2}
##print(d3)

d1={'ten':10,'twenty':20,'thirty':30}
d2={'thirty':30,'fourty':40,'fifty':50}
d3=d1.copy()
d3.update(d2)
print(d3)


