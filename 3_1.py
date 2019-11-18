num1=eval(input("Enter 1 numbers "))
num2=eval(input("Enter 2 numbers " ))
ch=input("Enter the operator (+,-,*,/,**,//,%):")
if ch=="+":
    r=num1+num2
elif ch=="-":
    r=num1-num2
elif ch=="*":
    r=num1*num2
elif ch=="/":
    r=num1/num2
elif ch=="%":
    r=num1%num2
elif ch=="**":
    r=num1**num2
elif ch=="//":
    r=num1//num2
else:
    print("Operator entered is not recognized")

print(num1,ch,num2," = ",r)