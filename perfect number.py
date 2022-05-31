num = int(input("enter a number"))
sum = 0
for i in range(1,num):
    if(num%1 == 0):
        sum = sum+i
if (sum == num):
    print("%d is not a perfect number" %num)
else:
    print("%d is a perfect number" %num)
