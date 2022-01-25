import wikipedia


def main():
    title = input("Please enter a page title or search phrase: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError:
            print("Input is ambiguous, try again")
        except:
            print("Invalid input")
        else:
            print(page.title)
            print(page.url)
            print(page.summary)
        title = input("Please enter a page title or search phrase: ").strip()


if __name__ == '__main__':
    main()
