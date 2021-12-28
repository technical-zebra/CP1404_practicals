from prac6_KeZhang.guitar import Guitar

"""
Gibson L-5 CES get_age() - Expected 98. Got 98
Another Guitar get_age() - Expected 7. Got 7
Gibson L-5 CES is_vintage() - Expected True. Got True
Another Guitar is_vintage() - Expected False. Got False
50-year old guitar is_vintage() - Expected True. Got False
"""

my_guitars = []

my_guitars.append(Guitar("Gibson L-5 CES", 1923, 16035.40))
my_guitars.append(Guitar("Another Guitar", 2014, 1512.9))
my_guitars.append(Guitar("50-year old guitar", 2016, 392.1))

print(my_guitars[0].get_age())
# Expected 98. Got 98
print(my_guitars[1].get_age())
# Expected 7. Got 7
print(my_guitars[2].get_age())
# Expected 5. Got 5

print(my_guitars[0].is_vintage())
# Expected True. Got True
print(my_guitars[1].is_vintage())
# Expected False. Got False
print(my_guitars[2].is_vintage())
# Expected False. Got False