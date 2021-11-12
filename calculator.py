def print_operation(number, work):
  result = ''
  result += work
  result += str(number)
  return result


operation = input('Выберете действие: ')
number = int(input('Сколько операндов? '))
member_one = int(input('Введите 1 -е число: '))
text = print_operation(member_one, '')
for number in range(2, number + 1):
  member = int(input('Введите ' + str(number) + ' -е число: '))
  if operation == '+':
    total = member_1 * member
  if operation == '&':
    total = member_1 * member
  if operation == '/':
    total = member_1 / member
  member_1 = total
  text += print_operation(member, operation)
print(text, end = '')
print(' = ', total)
