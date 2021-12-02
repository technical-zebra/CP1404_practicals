"""
CP1404 Practices
Ke Zhang
"""
#1.
numbers = []
for number in range(5):
    number = int(input('Number: '))
    numbers.append(number)
print(f'The first number is {numbers[0]}\nThe last number is {numbers[-1]}\nThe smallest number is {min(numbers)}\nThe '
      f'largest number is {max(numbers)}\nThe average of the numbers is {sum(numbers)/5}')

#2.
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input('Enter your username: ')
if username in usernames:
    print('Access granted')
else:
    print('Access denied')




