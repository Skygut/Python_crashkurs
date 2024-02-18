# # Argumente uebergeben

# # Positionabhaengige Argumente


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}s name is  {pet_name.title()}.")


# describe_pet("hamster", "harry")

# # output:
# # I have a hamster.
# # My hamsters name is  Harry.

################################################################
# Schlusselwortagrumente


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}s name is  {pet_name.title()}.")


# describe_pet(animal_type="hamster", pet_name="harry")

# # output:
# # I have a hamster.
# # My hamsters name is  Harry.

################################################################

# Standardwerte

# def describe_pet(pet_name, animal_type="dog"):
#     """Display information about a pet"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}s name is  {pet_name.title()}.")


# describe_pet(pet_name="harry")

# # Output:
# # I have a dog.
# # My dogs name is  Harry.
