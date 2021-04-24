slices = int(input('Enter the number of slices you want: '))
price = 0
if slices%2 == 0:
    price += slices*120.00
else:
    price += slices*123.00
print('Number of slices: {}\nPrice you have to pay: {}'.format(slices, price))
