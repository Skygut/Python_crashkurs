###############################################################

# # Ein Dictionary aus aehnlichen Objekten
# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# language = favorite_languages["sarah"].title()
# print(f"Sarah s favorite language is {language}.")

# # Output:
# Sarah s favorite language is C.

################################################################

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")


# peopel = {
#     "Segrey": "Auto",
#     "Andrey": "travel",
#     "peter": "Woodworking",
# }

# for name, hobbi in peopel.items():
#     print(f"Meine Kollege {name.title()} hat ein Hobbi {hobbi.title()}!")

# output:
# Meine Kollege Segrey hat ein Hobbi Auto!
# Meine Kollege Andrey hat ein Hobbi Travel!
# Meine Kollege Peter hat ein Hobbi Woodworking!

################################

# peopel = {
#     "Segrey": "Auto",
#     "Andrey": "travel",
#     "peter": "Woodworking",
# }

# for x in peopel.keys():
#     print(x)
# Output:
# Segrey
# Andrey
# peter

# Oder so, ohne keys()

# for x in peopel:
#     print(x)
# # Output:
# Segrey
# Andrey
# peter

################################

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# friends = ["phil", "sarah"]
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
# # Output:
# # Jen
# # Sarah
# #         Sarah, I see you love C!
# # Edward
# # Phil
# #         Phil, I see you love Python!


################################

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# if "erin" not in favorite_languages.keys():
#     print("Erin, please take out poll!")
# # Output:
# # Erin, please take out poll!

################################

# Die Schluessel in einem Dictionary geordnet durchlaufen

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll!")
# # Output:
# # Edward, thank you for taking the poll!
# # Jen, thank you for taking the poll!
# # Phil, thank you for taking the poll!
# # Sarah, thank you for taking the poll!

################################

# Alle Werte in einem Dictionary durchlaufen

# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# print("The following languages have been mentioned!")

# for language in favorite_languages.values():
#     print(language.title())

# # Output:
# # Python
# # C
# # Rust
# # Python


################################

# Um jede Sprache nur ein mal auszugeben, verwenden wir ein set()
# favorite_languages = {
#     "jen": "python",
#     "sarah": "c",
#     "edward": "rust",
#     "phil": "python",
# }
# print("The following languages have been mentioned!")

# for language in set(favorite_languages.values()):
#     print(language.title())

# Output: - Python wird nur ein mal erwaeht
# Python
# Rust
# C