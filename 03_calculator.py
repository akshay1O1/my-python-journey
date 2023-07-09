a=0
a=input("enter a number")
op=input("choose an operator(+,-,*,/,%)")
b=input("enter a number")
a=int(a)
b=int(b)
if op=="+":
    print("sum=",a+b)
elif op=="-":
    print("difference=",a-b)
elif op=="*":
    print("product=",a*b)
elif op=="/":
    print("quotient=",a/b)
elif op=="%":
    print("remainder=",a%b)
else:
    print("wrong operator")

