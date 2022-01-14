"""
CP1404/CP5632 Practical
Cleanup inconsistent song lyrics file names
Ke Zhang
"""
import os
import re


def main():
    """Cleanup inconsistent song lyrics file names."""

    # Change to desired directory
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, new_name)
            # os.rename(full_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # No solution is provided, but you may want to consider the patterns to look out for and fix
    # E.g. a lowercase letter followed by a capital, like "tN" should become "t_N"
    # Try doing this on paper first and then see if you can systematise it
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt").replace(".txt", "")
    words = re.findall('[A-Z][^A-Z]*', new_name)
    for index, word in enumerate(words):
        words[index] = word.title()
    new_name = "_".join(words)
    words = new_name.split("_")
    for index, word in enumerate(words):
        words[index] = word.title()
    new_name = "_".join(words)
    new_name = new_name.replace("__", "_").replace("(_", "(").replace("_(", "(")
    new_name = new_name + ".txt"

    return new_name


main()
