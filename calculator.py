def calculate():
    operation = input('''
Пожалуйста введите математическую операцию, какую хотите выполнить:
+ для сложения
- для вычитания
* для произведения
/ для деления
^ для возведения в степень (2е число показатель)
''')

    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))

    if operation == '+':
        print('{} + {} = {}'.format(number_1, number_2, (number_1 + number_2)))

    elif operation == '-':
        print('{} - {} = {}'.format(number_1, number_2, (number_1 - number_2)))

    elif operation == '*':
        print('{} * {} = {}'.format(number_1, number_2, (number_1 * number_2)))

    elif operation == '/':
        print('{} / {} = {}'.format(number_1, number_2, (number_1 / number_2)))

    elif operation == '^':
        print('{} ^ {} = {}'.format(number_1, number_2, (number_1 ** number_2)))

    else:
        print('Вы ввели неверную математическую операцию,\n'
              'запустите программу снова и введите корректную математическую операцию.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Вы хотите произвести вычисления снова?
Введите Y если Да или N если Нет.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('До свидания. Спасибо за использование программы.')
    else:
        again()

calculate()