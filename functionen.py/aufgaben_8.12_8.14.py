# Aufgabe 8-12

"""Schreiben Sie eine Funktion, die eine Liste von Sandwichefuellungen
aufnimmt. Sie soll nur einen Parameter aufweisen, in dem alle im Funktionsaufruf 
angegeben Fuellungen gesammelt werden, und einen Ueberblick ueber das bestellte 
Sandwich ausgeben. Rufen Sie dei Funktion dreimal auf, wobei Sie jeweils 
eine unterschieliche Anzahl von Argumenten uebergeben.
"""


# def sandwichfuellungen_liste(*toppings):
#     print(f"Hier ist ihre Pizza mit folgenden Fuellungen:")
#     for topping in toppings:
#         print(f"- {topping}")


# liste1 = ("salami", "cheese", "tomaten")
# liste2 = ("paprika", "gurke", "bacon", "cheese")
# liste3 = ("cheese", "tomaten")

# sandwichfuellungen_liste(*liste1)
# sandwichfuellungen_liste(*liste2)
# sandwichfuellungen_liste(*liste3)


"""
Output:

Hier ist ihre Pizza mit folgenden Fuellungen:
- salami
- cheese
- tomaten
Hier ist ihre Pizza mit folgenden Fuellungen:
- paprika
- gurke
- bacon
- cheese
Hier ist ihre Pizza mit folgenden Fuellungen:
- cheese
- tomaten
"""
##############################################################

# Aufgabe 8-13


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "Volodymyr",
    "Chub",
    location="Vechta",
    field="Data Science",
)

print(user_profile)

# # Output:
{
    "location": "Vechta",
    "field": "Data Science",
    "first_name": "Volodymyr",
    "last_name": "Chub",
}

##############################################################

# Aufgabe 8-14


# def myauto(marke, modell, **other_info):
#     """Schpeichere Daten in Dictionary ab"""
#     other_info["marke"] = marke
#     other_info["modell"] = modell
#     return other_info


# car = myauto(
#     "BMW",
#     "M1",
#     color="black",
#     ausstattung="voll",
# )

# print(car)

# """
# Output

# {
#     "color": "black",
#     "ausstattung": "voll",
#     "marke": "BMW",
#     "modell": "M1",
# }
# """
