# # Alle Vorkommen eines Wertes aus einer Liste entfernen

# pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit"]
# print(pets)

# while "cat" in pets:
#     pets.remove("cat")

# print(pets)

# # Output
# # ["dog", "cat", "dog", "goldfish", "cat", "rabbit"]
# # ["dog", "dog", "goldfish", "rabbit"]


################################################################

# Praktische Uebungen

# Mein Beispiel

students = [
    "andrey",
    "sergey",
    "liza",
    "bogdan",
    "liza",
    "andrey",
    "andrey",
    "sergey",
    "liza",
]
print("Original list")
print(students)
print("Following students have to be removed: liza and andrey")

while "liza" and "andrey" in students:
    students.remove("liza")
    students.remove("andrey")


print("After removing list")
print(students)


# output:
# Original list
# ['andrey', 'sergey', 'liza', 'bogdan', 'liza', 'andrey', 'andrey', 'sergey', 'liza']
# Following students have to be removed: liza and andrey
# After removing list
# ['sergey', 'bogdan', 'sergey']
