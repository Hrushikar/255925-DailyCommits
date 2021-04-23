# # Day 1
# print('Hello Python!! This is your programmer!!\n')
# a = int(input("Enter a number to display: "))
# print('Entered number (a): ', end='')
# print(a)
# print('\nGood Bye!!')
#
# # Day 2
# sum_of_numbers = 0
# print('Enter the number of numbers to find their sum:')
# n = int(input())
# print('Enter the numbers to find their sum:')
# for i in range(n):
#     sum_of_numbers += int(input())
# print('Sum: ' + str(sum_of_numbers))
#
# # Day 3
# secret_num = 777
# n = 0
# while True:
#     n = int(input("Enter the number you guessed: "))
#     if secret_num == n:
#         break
# print("You guessed correctly. Guessed number: ", n)
#
#
# # Day 4
# def factorial(number):
#     if number == 0 or number == 1:
#         return 1
#     return number * factorial(number - 1)
#
#
# n = int(input("Enter the number to find it's factorial: "))
# print(factorial(n))
#
# # Day 5
# print('Enter the elements of the array in a single line, space separated, to reverse and print their sum:')
# arr = list(map(int, input().split()))
# print(arr[::-1])
# print(sum(arr))


# Day 6
def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, (x // 2) + 1):
        if x % i == 0:
            print(i)
    print(x)


num = 100
print_factors(num)
