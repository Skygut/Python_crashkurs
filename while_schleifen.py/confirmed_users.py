# Elemente von einer Liste in eine andere verschieben

# # Beginnt mit einer Liste der zu ueberpruefengen mehr vorhanden sind.
# # und einer leeren Liste der bereits bestaetigten Benutzer
# unconfirmed_users = ["alise", "brian", "candace"]
# confirmed_users = []

# # Pruef alle Benutzer, bis keine unbestaetigten mehr vorhanden sind.
# # Verschiebt jeden bestaetigten Benutzer in die ensprechendende Liste.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Zeigt alle bestaetigten Benutzer an.
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# # Output:
# # Verifying user: Candace
# # Verifying user: Brian
# # Verifying user: Alise

# # The following users have been confirmed:
# # Candace
# # Brian
# # Alise
