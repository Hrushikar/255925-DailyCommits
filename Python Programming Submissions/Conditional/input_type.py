number = input('Enter a value: ')

alpha = [chr(i) for i in range(65, 91)]
alpha.extend([chr(i) for i in range(97, 123)])
n_list = list(number)
print(n_list)
flag_p = False
flag_n = False
flag = False

if number == '0':
    print('Zero')
    flag = True

elif '.' in n_list:
    print('Float number')
    flag = True

elif '+' in n_list:
    for i in range(n_list.index('+')):
        if n_list[i].isnumeric():
            flag_p = True
        else:
            flag_p = False
            break
    if flag_p:
        for i in range(n_list.index('+')+1, len(n_list)-1):
            if n_list[i].isnumeric():
                flag_p = True
            else:
                flag_p = False
                break
    if flag_p and n_list[-1] == 'j':
        print('Complex number')
        flag = True

elif '-' in n_list:
    for i in range(n_list.index('-')):
        if n_list[i].isnumeric():
            flag_n = True
        else:
            flag_n = False
            break
    if flag_n:
        for i in range(n_list.index('-')+1, len(n_list)-1):
            if n_list[i].isnumeric():
                flag_n = True
            else:
                flag_n = False
                break
    if flag_n and n_list[-1] == 'j':
        print('Complex number')
        flag = True

elif not flag_p and not flag_n and not flag:
    for i in number:
        if i in alpha:
            flag = True
            break
    if flag:
        print('String')
    else:
        print('Real number')
