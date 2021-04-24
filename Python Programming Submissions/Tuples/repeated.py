num = [1987298, 298, 3767, 4232, 545, 667, 77675, 12232, 232398, 39945, 651, 667, 89989, 12232, 232398, 667]
n_tuple = tuple(num)
n_set = set(num)
for i in n_set:
    c = n_tuple.count(i)
    if c > 1:
        print('number: {} count: {}'.format(i, c))
