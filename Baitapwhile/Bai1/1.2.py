s=0
i=1
n=int(input("nhap so le nguyen duong n:"))
while n<0 or n%2==0: n=int(input("n phai la so le nguyen duong:"))
else:
    while i<=n:
        s+=i
        i+=2
    else:
        print("s=1+3+5+...+",n,"=",s)
        