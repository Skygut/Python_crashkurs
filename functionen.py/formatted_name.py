# Rueckgabewerte


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

# # Output:
# # Jimi Hendrix

################################################################

# Optionele Argumente


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "lee", "hendrix")
# print(musician)

# # output:
# # Jimi Lee Hendrix

################################################################

# Optionele Argumente


# def get_formatted_name(first_name, last_name, middle_name=""):
#     """Return a full name, neatly formatted"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:

#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)

# musician = get_formatted_name("jimi", "lee", "hendrix")
# print(f"\n{musician}")

# # # output:
# # Jimi Hendrix

# # Jimi Hendrix Lee
