# Compare map(lambda...) vs [x... for x...]

my_list = [1,2,3,4,5]

print(list(map(lambda x:x*x, my_list)))

print([x*x for x in my_list])

# List comprehension is faster than map(lambda...)