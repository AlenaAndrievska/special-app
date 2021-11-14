while True:
    operation = input('Выберете операцию: ')
    number_a = int(input('Введите первое число: '))
    number_b = int(input('Введите второе число: '))
    if operation == '+':
      number_c = number_a + number_b
    elif operation == '-':
      number_c = number_a - number_b
    elif operation == '*':
      number_c = number_a * number_b
    elif operation == '/':
      number_c = number_a / number_b
    elif operation == '%':
      number_c = number_a % number_b
    else:
      print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
      break
    print(number_a, operation, number_b, '=', number_c)
    break
