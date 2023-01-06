rohith=input().split()
prathap=input().split()
print(*[(int(i)+int(j)) for i,j in zip(rohith,prathap)])
