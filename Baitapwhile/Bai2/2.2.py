p=1
i=1
n=int(input("nhap so nguyen duong n:"))
while n<0: n=int(input("n phai la so nguyen duong:"))
else:
    while i<=n:
        p*=(1/i)
        i+=1
    print("P=1x1/2x...x1/",n,"=",p)