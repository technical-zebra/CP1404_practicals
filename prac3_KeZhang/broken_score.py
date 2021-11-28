"""
CP1404 Practices
Ke Zhang
broken score: a program that take a score and prints the grade of the score.
"""


def main():
    """Program start."""
    score = float(input("Enter score: "))
    print(determine_grade(score))


def determine_grade(score):
    """Input score and determine grade based on score then return grade."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
