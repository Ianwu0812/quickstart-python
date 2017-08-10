def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a < b:
        print(b, 'is maximum')
    else:
        print('a equals b')

a = input('Please enter a number\n')
b = input('Please enter the other number\n')

print_max(a, b)
