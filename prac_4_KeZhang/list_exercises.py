"""
CP1404 Practices
Ke Zhang
"""
numbers = []
for number in range(5):
    number = int(input('Number: '))
    numbers.append(number)
print(f'The first number is {numbers[0]}\nThe last number is {numbers[-1]}\nThe smallest number is {min(numbers)}\nThe '
      f'largest number is {max(numbers)}\nThe average of the numbers is {sum(numbers)/5}')
