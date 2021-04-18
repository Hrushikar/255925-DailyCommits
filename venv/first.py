# Day 1
print('Hello Python!! This is your programmer!!\n')
a = int(input("Enter a number to display: "))
print('Entered number (a): ', end='')
print(a, end='\n\n')
print('Good Bye!!')

# Day 2
sum = 0
print('Enter the number of numbers to find their sum:')
n = int(input())
print('Enter the numbers to find their sum:')
for i in range(n):
    sum += int(input())
print('Sum: '+str(sum))