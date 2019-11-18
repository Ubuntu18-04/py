import cmath as m
a,b,c=eval(input("Enter the numbers a,b,c separated by commas:"))
if a==0 or b==0 or c==0:
    while a==0 or b==0 or c==0:
        a,b,c=eval(input("Enter the numbers a,b,c separated by commas:"))
d=(b*b)-(4*a*c)
r1=r2=0
if d==0:
    print("Roots are real and equal:")
    r1=r2=b/(2*a)
    print("Roots=",r1,r2)
elif d<0:
    print("Roots are imaginary")
    real=-b/(2*a)
    img=m.sqrt(-d)/(2*a)
    print("Real=",real," Imaginary=",img)
elif d>0:
    print("Roots are real and unequal")
    r1=(-b+m.sqrt(d))/(2*a)
    r2=(-b-m.sqrt(d))/(2*a)
    print("R1=",r1,"R2=",r2)

