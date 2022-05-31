n1 = int(input("enter the first number\n"))
n2 = int(input("enter the second number\n"))
op = str(input("enter S for subtraction, A for addition, M for multiplication, R for remainder and D for division\n"))
if op=="A":
    print(n1+n2)
elif op=="s":
    print(n1-n2)
elif op=="M":
    print(n1*n2)
elif op=="D":
    print(n1/n2)
elif op=="R":
    print(n1%n2)
else:
    print("invalid operation")
