print("sum")
a=input("enter a number")
a=int(a)
b=input("enter a number")
b=int(b)#number should be converted to integer otherwise when added sum will be ab
sum=a+b
print("sum=",sum)

print("REMAINDER WHEN NUMBER IS DIVIDED BY 2")
a=input("enter a number")
a=int(a)
print("reminder is=",a%2)

print("Checking datatype")
a=input("enter something  ")
print("dataype is ",type(a))

print("GREATEST NUMBER")
a=input("enter a number")
a=int(a)
b=input("enter a number")
b=int(b)

if a>b:
    print("greatest number is ",a)
else:
    print("greatest number is ",b)

print("AVERAGE OF 2 NUMBERS")
a=input("enter a number")
a=int(a)
b=input("enter a number")
b=int(b)
avg=(a+b)/2 #here bracket is imp 
print("average is ",avg)

print("SQUARE OF A NUMBER")
a=input("enter a number")
a=int(a)
sq=a*a
print("square is ",sq)
