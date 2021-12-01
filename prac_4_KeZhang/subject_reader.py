"""
CP1404/CP5632 Practical
Data file -> lists program
KeZhang
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject(subjects):
    """Read each subject details from lists of subjects, and display all subject details"""
    for subject in subjects:
        print(f'{subject[0]} is taught by {subject[1]} and has {subject[2]} students')


main()
