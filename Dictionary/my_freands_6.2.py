person_1 = {
    "vorname": "Sergey",
    "nachname": "Fred",
    "alter": 25,
    "hobbi": "Auto",
}
person_2 = {
    "vorname": "Andrey",
    "nachname": "gero",
    "alter": 35,
    "hobbi": "Werken",
}
person_3 = {
    "vorname": "Pavel",
    "nachname": "Kolon",
    "alter": 35,
    "hobbi": "Travel",
}
men_1 = person_1.get("city", "Diesen Wert gibt es nicht!")
print(men_1)
men_1_vorname = person_1.get("nachname", "no excist").title()
print(men_1_vorname)


for key, value in person_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
