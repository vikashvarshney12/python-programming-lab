while 1:
    try:
        n=int(input("enter the integer:"))
        break
    except ValueError:
        print("enter again")
    else:
        print("congratulations..number accepted")
