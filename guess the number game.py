import random
count=0
value=random.randrange(0,1001)
while 1:
    count+=1
    user=int(input('enter the number\t'))
    if user==value:
        print('YOU WON!!')
        print(f'your number of counts are {count}')
        break
    elif user>value:
        print('the value is too large')
    elif user<value:
        print('the value is too small')
