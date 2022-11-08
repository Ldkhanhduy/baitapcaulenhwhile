s=0
i=2
n=int(input("nhap so chan nguyen duong n:"))
while n<0 or n%2==1: n=int(input("n phai la so chan nguyen duong:"))
else:
    while i<=n:
        s+=i
        i+=2
    print("s=2+4+6+...+",n,"=",s)
    