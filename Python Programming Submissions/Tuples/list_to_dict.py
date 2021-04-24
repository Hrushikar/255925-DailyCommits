list_of_tuples = [("x", 1), ("x", 2), ("x", 3), ("y", 3), ("y", 4), ("z", 5), ("key", None)]
print('List of tuple: ', list_of_tuples)
list_to_dict = {}
for a, b in list_of_tuples:
    list_to_dict.setdefault(a, []).append(b)
print('Dict: ',list_to_dict)
