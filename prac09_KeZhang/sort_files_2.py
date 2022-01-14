"""
CP1404/CP5632 Practical
Sort files based on extension and user categorisation
Ke Zhang
"""
import shutil
import os


def main():
    """Move files into where user wants to store them based on extension."""

    filenames = []
    extension_names = []
    extension_to_folder_dict = {}
    directory = str(os.getcwd())
    for filename in os.listdir('FilesToSort'):
        if filename.find(".") != -1:
            filenames.append(filename)
            extension_name = filename.split(".")[-1]
            if extension_name not in extension_names:
                extension_names.append(extension_name)
                folder_name = input(f"What category would you like to sort {extension_name} files into? ")
                extension_to_folder_dict[f"{extension_name}"] = f"{folder_name}"
                try:
                    os.mkdir(f"FilesToSort\{folder_name}")
                except FileExistsError:
                    print(f"Folder {folder_name} existed! Now try moving files")
            # print(extension_to_folder_dict)
            # print(f'{directory}\FilesToSort\{filename}')
            # print(f'{directory}\FilesToSort\{extension_to_folder_dict[f"{extension_name}"]}\{filename}')
            shutil.move(f'{directory}\FilesToSort\{filename}',
                        f'{directory}\FilesToSort\{extension_to_folder_dict[f"{extension_name}"]}\{filename}')

    # Version 2
    # filenames = [filename for filename in os.listdir('FilesToSort') if filename.find(".") != -1]
    # extension_names = []
    # for extension_name in filenames:
    #     extension_name = extension_name.split(".")[-1]
    #     if extension_name not in extension_names:
    #         extension_names.append(extension_name)
    #
    # print(filenames)
    # print(extension_names)
    #
    # os.chdir('FilesToSort')
    # directory = str(os.getcwd())
    # print(directory)
    #
    # for n in range(len(extension_names)):
    #     folder_name = input(f"What category would you like to sort {extension_names[n]} files into?")
    #     try:
    #         os.mkdir(f"{folder_name}")
    #     except FileExistsError:
    #         print(f"Folder {folder_name} existed! Now try moving files")
    #     for filename in filenames:
    #         if filename.split(".")[-1] == extension_names[n]:
    #             shutil.move(f'{directory}\{filename}', f'{directory}\{folder_name}\{filename}')


main()
