# Die if-elif-else-Kette

# age = 12

# if age < 4:
#     print("Your admission cost is 0 USD")
# elif age < 18:
#     print("Your admission cost is 25 USD")
# else:
#     print("Your admission cost is 40 USD")

# # output: Your admission cost is 25 USD

################################################################

# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40
# print(f"Your admission cost is {price} USD")

# output: Your admission cost is 25 USD

################################################################
# Mehrere elif-Bloecke

# age = 65

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f"Your admission cost is {price} USD")

# # output: Your admission cost is 20 USD

################################################################

# Den else-Block weglassen
# age = 12

# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20
# print(f"Your admission cost is {price} USD")

# # output: Your admission cost is 25 USD
