# Mehrere Bedingungen pruefen

# request_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in request_toppings:
#     print("Adding mushrooms")
# if "pepperoni" in request_toppings:
#     print("Adding pepperoni")
# if "extra cheese" in request_toppings:
#     print("Adding extra cheese")
# print("\nFinished making your pizza!")
# #  output:
# # Adding mushrooms
# # Adding extra cheese

# # Finished making your pizza!

################################

# mit if-else kann man diseses nicht realisiere, weil if-Anweisung prueft die
# Bedingung ein mal und wird die anderen nicht ausfuehren.

# request_toppings = ["mushrooms", "extra cheese"]

# if "mushrooms" in request_toppings:
#     print("Adding mushrooms")
# elif "pepperoni" in request_toppings:
#     print("Adding pepperoni")
# elif "extra cheese" in request_toppings:
#     print("Adding extra cheese")
# print("\nFinished making your pizza!")
# # #  output:
# Adding mushrooms

# Finished making your pizza!


################################

# Pruefung auf besondere Elemente
# request_toppings = ["mushrooms", "green peppers", "extra cheese"]
# for request_topping in request_toppings:
#     print(f"Adding {request_topping}.")

# print("\nFinished making your pizza!")

# output:
# Adding mushrooms.
# Adding green peppers.
# Adding extra cheese.

# Finished making your pizza!

################################

# request_toppings = ["mushrooms", "green peppers", "extra cheese"]
# for request_topping in request_toppings:
#     if request_topping == "green peppers":
#         print("Sorry, we are out of green peppers right now")
#     else:
#         print(f"Adding {request_topping}.")

# print("\nFinished making your pizza!")

# output:
# Adding mushrooms.
# Sorry, we are out of green peppers right now
# Adding extra cheese.

# Finished making your pizza!

################################

# Pruefung auf nicht leere Liste
# request_toppings = []
# if request_toppings:
#     for request_topping in request_toppings:
#         print(f"Adding {request_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

# # output:
# # Are you sure you want a plain pizza?

# Hier wird die Bedingung else ausgefuehrt, weil die Liste leer ist.

################################

# Mehrere Listen verwenden

available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "extra cheese",
    "pepperoni",
    "pineapple",
]

request_toppings = ["mushrooms", "french fries", "extra cheese"]

for request_topping in request_toppings:
    if request_topping in available_toppings:
        print(f"Adding {request_topping}.")
    else:
        print(f"Sorry, we don't have {request_topping}.")
print("\nFinished making your pizza!")

# output:
# Adding mushrooms.
# Sorry, we don't have french fries.
# Adding extra cheese.

# Finished making your pizza!
