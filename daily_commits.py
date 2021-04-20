# Day 1
print('Hello Python!! This is your programmer!!\n')
a = int(input("Enter a number to display: "))
print('Entered number (a): ', end='')
print(a)
print('\nGood Bye!!')

# Day 2
sum_of_numbers = 0
print('Enter the number of numbers to find their sum:')
n = int(input())
print('Enter the numbers to find their sum:')
for i in range(n):
    sum_of_numbers += int(input())
print('Sum: ' + str(sum_of_numbers))

# Day 3
secret_num = 777
n = 0
while True:
    n = int(input("Enter the number you guessed: "))
    if secret_num == n:
        break
print("You guessed correctly. Guessed number: ", n)
