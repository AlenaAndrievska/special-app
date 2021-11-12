

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print('Наибольший общий делитель:', a + b)

number_a = int(input('Введите первое число: '))
number_b = int(input('Введите второе число: '))
gcd(number_a, number_b)