def rohith(r,p):
    rp='.'
    for i in range(0,p):
        print(rp*(p-i-1)+r*(2*i+1)+rp*(p-i-1))
    return None
            
r=input()
p=int(input())
rohith(r,p)
