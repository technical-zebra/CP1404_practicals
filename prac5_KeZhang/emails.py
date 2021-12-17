def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = separate_name_from_email(email)
        choice = input(f'Is your name {name}? (Y/n) ').lower()

        if choice == 'y' or choice == '':
            email_to_name[name] = email
        else:
            name = input('Name: ')
            email_to_name[name] = email
        email = input("Email: ")

    [print(f"{n} ({e})") for (n, e) in email_to_name.items()]


def separate_name_from_email(email):
    """Separate name from email."""
    name = email.split("@")[0]
    try:
        names = name.split(".")
        names = [name.title() for name in names]
        name = " ".join(names)
    except:
        name = name.title()
    return name


if __name__ == '__main__':
    main()
