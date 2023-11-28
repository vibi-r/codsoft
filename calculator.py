a=float(input("enter first number:"))
b=float(input("enter second number:"))
ch=0
while ch<5:
    print("calculator")
    print("1.add")
    print("2.difference")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    ch=int(input("enter your choice(1/2/3/4/5):"))
    if ch==1:
        c=a+b
        print("sum",c)
    elif ch==2:
        c=a-b
        print("difference",c)
    elif ch==3:
        c=a*b
        print("product",c)
    elif ch==4:    
        c=a/b
        print("quotient",c)
    elif ch==5:
        break
    else:
         print("invalid")

