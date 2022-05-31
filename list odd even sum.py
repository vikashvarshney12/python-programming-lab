num_list = []
even_sum = 0
odd_sum = 0
num = int(input("enter the num of elements"))
for i in range(1,num+1):
    value = int(input("enter the value of %d elements:"%i))
    num_list.append(value)
for j in range(num):
    if (num_list[j]%2 == 0):
        even_sum = even_sum + num_list[j]
    else:
        odd_sum = odd_sum + num_list[j]
print(even_sum)
print(odd_sum)
