s=0
i=1
n=int(input("nhap so nguyen duong n:"))
while n<0: n=int(input("n phai la so nguyen duong:"))
else:
    while i<=n:
        s+=(1/i)
        i+=1
    print("s=1+1/2+...+1/",n,"=",s)