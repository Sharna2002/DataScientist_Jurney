# Check if any number in list is negative. Check if all are positive

my_list = [1,6,4,-2,3,-1,5,-8]

print(any(x < 0 for x in my_list))

print(all(x > 0 for x in my_list))