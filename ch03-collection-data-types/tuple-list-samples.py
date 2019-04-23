import collections
import string
import sys

# named tuple samples
Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

sales = list()  # OR sales = [] -- which one is the standard convention???
sales.append(Sale(432, 921, "2008-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2008-09-15", 1, 18.49))

total = 0
for sale in sales:
    total += sale.quantity * sale.price
print("Total ${0:.2f}".format(total)) # prints: Total $42.46

Aircraft = collections.namedtuple("Aircraft", "manufacturer model seating")
Seating = collections.namedtuple("Seating", "minimum maximum")
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220))
print(aircraft.seating.maximum)
print("{0} {1}".format(aircraft.manufacturer, aircraft.model))
print("{0.manufacturer} {0.model}".format(aircraft))
print("{manufacturer} {model}".format(**aircraft._asdict()))

# list samples - yikes!!! list are mutable - NOT COOL
first, *rest = [9, 2, -4, 8, 7]
print(first)
print(rest)

first, *mid, last = "Charles Philip Arthur George Windsor".split()
print(first)
print(mid)
print(last)


# implementing head & tail recursion, similar to Haskell & Scala
def print_head(list_of_strings):
    head, *tail = list_of_strings
    if head:
        print(head)
        if tail:
            print_head(tail)


print_head("the quick brown fox jumps over the lazy dog".split())

# list comprehension samples
# [expression for item in iterable]
# [expression for item in iterable if condition]
leaps = [y for y in range(1900, 1940) if y % 4 == 0]
print(leaps)

codes = []
for sex in "MF":  # Male, Female
    for size in "SMLX":  # Small, Medium, Large, eXtra large
        if sex == "F" and size == "X":
            continue
        for color in "BGW": # Black, Gray, White
            codes.append(sex + size + color)
print(codes)

codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW" if not (s == "F" and z == "X")]
print(codes)

# set samples
union = set("pecan") | set("pie") == {'p', 'e', 'c', 'a', 'n', 'i'}  # Union
intersection = set("pecan") & set("pie") == {'p', 'e'}  # Intersection
difference = set("pecan") - set("pie") == {'c', 'a', 'n'}  # Difference
symmetric_difference = set("pecan") ^ set("pie") == {'c', 'a', 'n', 'i'}  # Symmetric difference
print(union, intersection, difference, symmetric_difference)

# set comprehension
# {expression for item in iterable}
# {expression for item in iterable if condition}

# dictionary samples
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = dict(zip(("id", "name", "size"), (1948, "Washer", 3)))
d5 = {"id": 1948, "name": "Washer", "size": 3}
print(d1, d2, d3, d4, d5)

d = {}.fromkeys("ABCD", 3)  # d == {'A': 3, 'B': 3, 'C': 3, 'D': 3}
s = set("ACX")  # s == {'A', 'C', 'X'}
matches = d.keys() & s  # matches == {'A', 'C'}
print(d, s, matches)

# dictionary comprehension
# {keyexpression: valueexpression for key, value in iterable}
# {keyexpression: valueexpression for key, value in iterable if condition}

# counting unique words
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1

for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))






