# Calculate the product of a list (1*2*3*4) using functool.reduce 

from functools import reduce
my_list = [1,2,3,4]

print(reduce(lambda a,b: a*b, my_list))
