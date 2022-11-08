p=1
i=1
n=int(input("nhap so le nguyen duong n:"))
while n<0 or n%2==0: n=int(input("n phai la so le nguyen duong:"))
else:
    while i<=n:
        p*=i
        i+=2
    print("P=1x3x...x",n,"=",p)