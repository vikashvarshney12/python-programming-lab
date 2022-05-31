try:
    fp = open("a.txt","r")
    try:
        fp.write("this is my test file")
    finally:
        print("closing the file")
        fp.close()
except IOError as e:
    print("Error:",e)
