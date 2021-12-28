from prac6_KeZhang.guitar import Guitar

my_guitars = []
name = input("My guitars!\nName: ")
while name != "":
    year = input("Year: ")
    cost = input("Cost: $")
    my_guitars.append(Guitar(name, year, cost))
    print("\n")
    name = input("Name: ")

# my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


print(f'These are my guitars:')
for count, guitar in enumerate(my_guitars, 1):
    vintage_string = "(vintage)" if guitar.is_vintage() else ""
    print(f'Guitar {count}: {guitar.name:>20} ({guitar.year:4}), worth $ {guitar.cost:9,.2f} {vintage_string}')