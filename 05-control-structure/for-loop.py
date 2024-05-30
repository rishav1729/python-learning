for val in range(5,10+1):
    print (val)
print ("the loop has ended")


num = range(5)
for val in reversed(num):
    print(val)
print('the loop has ended')

# retun the numbers which contains onliy even digits in the range of 100-300

items = []

for i in range(100,300):

    num_str = str(i)

    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    third_digit = int(num_str[2])

    if((first_digit % 2 == 0) and (second_digit % 2 == 0) and (third_digit % 2 == 0)):
        items.append(num_str)
print(",".join(items))

