# Ein einfaches Dictionary


# alien_0 = {"color": "green", "points": 5}

# print(alien_0["color"])
# print(alien_0["points"])

# # output:
# # green
# # 5


################################################################

# alien_0 = {"color": "green", "points": 5}
# new_points = alien_0["points"]
# print(f"You just earned {new_points} points!")

# output:
# You just earned 5 points!


###############################################################


# alien_0 = {"color": "green", "points": 5, "y-position": 25, "x-position": 0}
# print(alien_0["y-position"])
# # output:
# # 25

###############################################################

# alien_0 = {}
# alien_0["color"] = "green"
# alien_0["points"] = 5
# print(alien_0)
# # Output:
# # {'color': 'green', 'points': 5}


###############################################################

# Werte in einem Dictionary aendern

# alien_0 = {"color": "green"}
# print(f"The alien is {alien_0["color"]}.")

# alien_0["color"] = "yellow"
# print(f"The alien is now {alien_0["color"]}.")

# # output:
# # The alien is green.
# # The alien is now yellow.


###############################################################

# alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
# print(f"Original position: {alien_0["x_position"]}")
# # Bewegt das Raumschif nach rechts.
# # Bestimmt, wie weit das Schiff bei der seiner aktuellen Geschwindigkeit
# #verschoben werden muss

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     #Dies muss ein schnelles Schiff sein.
#     x_increment = 3

# #Die neue Position errechnet sich aus der alten plus Inkrement.
# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print(f"New position: {alien_0["x_position"]}")

#  output:
# Original position: 0
# New position: 2


###############################################################

# alien_0 = {"x_position": 0, "y_position": 25, "speed": "fast"}
# print(f"Original position: {alien_0["x_position"]}")
# # Bewegt das Raumschif nach rechts.
# # Bestimmt, wie weit das Schiff bei der seiner aktuellen Geschwindigkeit
# #verschoben werden muss

# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# else:
#     #Dies muss ein schnelles Schiff sein.
#     x_increment = 3

# #Die neue Position errechnet sich aus der alten plus Inkrement.
# alien_0["x_position"] = alien_0["x_position"] + x_increment

# print(f"New position: {alien_0["x_position"]}")

# #  output:
# # Original position: 0
# # New position: 3


###############################################################

"""Schnluessel-Wert-Paare entfehnen"""
# alien_0 = {"color": "green", "points": 5}
# print(alien_0)
# Output: {"color": "green", "points": 5}

# del alien_0["points"]
# print(alien_0)
# Output: {"color": "green"}

###############################################################

"""Dictionaries in einer Liste"""
#
# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "points": 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# output:
# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}

###############################################################
"""Erstelle eine leere Liste zum Speichern der Schiffe"""

# aliens = []

# # Erstelle 30 gruene Schiffe

# for aliens_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)

# # Zeige die ersten 5 Schiffe am:
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Gibt an, wie viele Schiffe erstellt wurden.
# print(f"Total number of aliens: {len(aliens)}")

# # # output:
# # {'color': 'green', 'points': 5}
# # {'color': 'green', 'points': 5}
# # {'color': 'green', 'points': 5}
# # {'color': 'green', 'points': 5}
# # {'color': 'green', 'points': 5}
# # ...
# # Total number of aliens: 30


###############################################################

"""Erstelle eine leere Liste zum Speichern der Schiffe"""

# aliens = []

# # Erstelle 30 gruene Schiffe

# for aliens_number in range(30):
#     new_alien = {"color": "green", "points": 5, "speed": "slow"}
#     aliens.append(new_alien)


# for alien in aliens[:3]:
#     if alien["color"] == "green":
#         alien["color"] = "yellow"
#         alien["speed"] = "medium"
#         alien["points"] = 10

# # Zeige die ersten 5 Schiffe am:
# for alien in aliens[:5]:
#     print(alien)
# print("...")

# # Gibt an, wie viele Schiffe erstellt wurden.
# print(f"Total number of aliens: {len(aliens)}")

# # # output:
# # {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# # {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# # {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# # {'color': 'green', 'points': 5, 'speed': 'slow'}
# # {'color': 'green', 'points': 5, 'speed': 'slow'}
# # ...
# # Total number of aliens: 30
