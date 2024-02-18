# Funktionen definieren


# def greet_user():
#     """display a simple greeting"""
#     print("Hello!")


# greet_user()

# # Output:
# # Hello!

################################################################


# def greet_user(username):
#     """display a simple greeting"""
#     print(f"Hello, {username.title()} ! ")


# greet_user("junos")

# # Output:

# # Hello, Junos !

################################################################

# funktionen in einer while-Schleife


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name


# Dies ist eine Endlosseschleife!

while True:
    print("\nPlease tell me your nema: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
