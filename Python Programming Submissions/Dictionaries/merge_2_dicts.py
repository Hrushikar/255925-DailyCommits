def merge(d1, d2):
    res = d1 | d2
    return res


dict1 = {'element1': 1, 'element2': 2}
dict2 = {'element3': 3, 'element4': 4}
dict3 = merge(dict1, dict2)
print(dict3)
