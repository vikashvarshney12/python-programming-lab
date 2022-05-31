num_list1 = []
num_list2 = []
n1 = int(input("enter the num of elements"))
for i in range(1,n1+1):
    value = int(input("enter the value of %d elements:"%i))
    num_list1.append(value)
n2 = int(input("enter the num of elements"))
for j in range(1,1+n2):
    value2 = int(input("enter the value of %d elements:"%j))
    num_list1.append(value2)
lst = num_list1 + num_list2
print(lst) 
    
