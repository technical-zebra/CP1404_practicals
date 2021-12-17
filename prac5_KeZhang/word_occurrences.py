"""
CP1404/CP5632 Practical
Word Occurrences: A program to count the occurrences of words in a string.
KeZhang
"""

from operator import itemgetter


def main():
    # version 1
    text = input("Text: ")
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    [print(f'{w} : {n}') for w, n in word_count.items()]

    # version 2
    print('-' * 10)
    words_list = [(w, n) for w, n in word_count.items()]
    words_list.sort(key=itemgetter(0))
    length = 0
    for word in words_list:
        if len(word[0]) > length:
            length = len(word[0])
    for word in words_list:
        print(f'{word[0]:{length}} : {word[1]}')


if __name__ == '__main__':
    main()
