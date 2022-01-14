"""
CP1404/CP5632 Practical - Suggested Solution
Sort files based on extension
Ke Zhang
"""
import shutil
import os


def main():
    """Move files into folders with the same name as their extension."""
    folder_names = ["xlsx", "xls", "txt", "png", "jpg", "gif", "docx", "doc"]
    try:
        for folder_name in folder_names:
            os.mkdir(f"FilesToSort\{folder_name}")
    except FileExistsError:
        pass

    # print(os.listdir('FilesToSort'))
    filenames = [filename for filename in os.listdir('FilesToSort') if len(filename) > 4]
    # print(filenames)
    #
    # print(os.getcwd())
    os.chdir('FilesToSort')
    directory = str(os.getcwd())
    for filename in filenames:
        # print(filename, f'{directory}\{filename}', f'{directory}\{filename.split(".")[1]}\{filename}')
        shutil.move(f'{directory}\{filename}', f'{directory}\{filename.split(".")[1]}\{filename}')


if __name__ == '__main__':
    main()
