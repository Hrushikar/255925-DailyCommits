num = [1987298, 298, 3767, 4232, 545, 667, 77675, 12232, 232398, 39945, 651, 89989]
print('Before changing positions:')
for i, n in enumerate(num):
    print('index: ' + str(i) + ' number: ' + str(n))
num.insert(0, None)
print('\n\nAfter changing positions:')
for i, n in enumerate(num):
    if i > 0:
        print('index: ' + str(i) + ' number: ' + str(n))
