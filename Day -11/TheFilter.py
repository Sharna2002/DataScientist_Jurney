# Remove all negatives number from a list using filter()
my_list = [1,6,-4,8,-2,-1,7,-3,0]
def positive_number(a):
    return a>=0
print(list(filter(positive_number,my_list)))