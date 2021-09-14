dict_commands = {
    '+': lambda number, second_number: number + second_number,
    '-': lambda number, second_number: number - second_number,
    '*': lambda number, second_number: number * second_number,
    '/': lambda number, second_number: number / second_number,
    '//': lambda number, second_number: number // second_number,
    '%': lambda number, second_number: number % second_number,
    }

number = float(input())
command = input()
second_number = float(input())

if command == '/' and second_number == '0':
    print('Деление на 0!')
else:
    print(dict_commands[command](number, second_number))



