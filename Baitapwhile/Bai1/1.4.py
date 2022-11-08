from math import log

s=0
i=1
n=int(input("nhap so nguyen duong n:"))
while n<0: n=int(input("n phai la so nguyen duong:"))
else:
    while i<=n:
        s+=log(i)
        i+=1
    print("s=ln(1)+ln(2)+...+ln(",n,")=",s)