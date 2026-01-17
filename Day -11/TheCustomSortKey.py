#Sort ["100px","20px","3px"] numerically (so 3px comes first).

data = ["100px","20px","3px"]
print(sorted(data,key = lambda x: int(x[:-2])))
