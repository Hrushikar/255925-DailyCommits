n_list = [1, 2, 3, 4]
new_dict = current = {}
for name in n_list:
    current[name] = {}
    current = current[name]
print(new_dict)
