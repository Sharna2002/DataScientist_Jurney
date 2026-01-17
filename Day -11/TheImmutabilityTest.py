# Try to modify a tuple inside a map function 
my_tuple = (1,2,3)

try:
    my_tuple[0] = 5
    print(my_tuple)
except TypeError as e:
    print(e)

