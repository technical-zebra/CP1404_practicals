import random

MAXIMUM = 45
MINIMUM = 1
NUMBERS_PER_LINE = 6

def main():
    number_of_quick_picks = int(input('How many quick picks? '))
    while number_of_quick_picks <= 0:
        print('Invalid number!')
        number_of_quick_picks = int(input('How many quick picks? '))

    for x in range(number_of_quick_picks):
        quick_pick = []
        string = ''
        for y in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
            string = string + f' {number:>2}'
        quick_pick.sort()
        print(string)


if __name__ == '__main__':
    main()
