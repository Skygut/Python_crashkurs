################################################

# Aufgabe 8-12

# def sandwiches(*fuellungs):
#     print(f"\nHier sind die fuellungen: {fuellungs}")


# sandwiches("Paprika")
# sandwiches("Salami", "Cheese", "Salat")


# # Output:

# # Hier sind die fuellungen: ('Paprika',)

# # Hier sind die fuellungen: ('Salami', 'Cheese', 'Salat')

################################################

# Aufgabe 8-13


# Beliebig viele Schlusselwortargumente uebegeben


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# user_profile = build_profile(
#     "Volodymyr",
#     "Chub",
#     location="Vechta",
#     field="IT",
#     age=42,
# )

# print(user_profile)

# Output:
# {
#     "location": "Vechta",
#     "field": "IT",
#     "age": 42,
#     "first_name": "Volodymyr",
#     "last_name": "Chub",
# }


################################################

# Aufgabe 8-14


# def car_description(marke, modell, **further_info):
#     """Build a dictionary containing everything we know about a car."""
#     further_info["car_marke"] = marke
#     further_info["car_model"] = modell
#     return further_info


# car_profile = car_description(
#     "BMW",
#     "X3",
#     color="black",
#     motor="disel",
#     number_ps=200,
#     furnishing="full",
# )

# print(f"\nI bought my new car: \n {car_profile}")

# # Output:
# # I bought my new car:

# # {'color': 'black', 'motor': 'disel', 'number_ps': 200, 'furnishing': 'full', 'car_marke': 'BMW', 'car_model': 'X3',}
