# 'Listen'

# 'Elemente in einer Liste ansprechen
# autos = ["BMW", "audi", "volvo", "Ford"]
# print(autos)
# 'Output: ["BMW", "audi", "volvo", "Ford"]'
# print(autos[0])
# Output BMW

# print(autos[1].title())
# Output Audi

# print(autos[1])
# print(autos[2])
# Output
# audi
# volvo

# Letztes Element in der Liste
# print(autos[-1])
# Output Ford

# print(autos[-2])
# Output volvo

# Element ändern

# autos[0] = "Ferrari"
# print(autos)
# Output: ["Ferrari", "audi", "volvo", "Ford"]

########################################################
# Element am Ende der Liste hinzufügen

# autos = ["BMW", "audi", "volvo", "Ford"]
# print(autos)
# # ["BMW", "audi", "volvo", "Ford"]
# autos.append("ducati")
# print(autos)
# ["BMW", "audi", "volvo", "Ford", "ducati"]

#################################################
# Liste dynamisch erstellen

# autos = []

# autos.append("BMW")
# autos.append("audi")
# autos.append("volvo")

# print(autos)
# # Output: ["BMW", "audi", "volvo"]

#################################################

# Element in eine <Liste einfügen

# autos = ["BMW", "audi", "volvo", "Ford"]
# autos.insert(0, "Ferrari")
# print(autos)
# Output: ["Ferrari", "BMW", "audi", "volvo", "Ford"]

#################################################
# autos = ["BMW", "audi", "volvo", "Ford"]
# print(autos)

# del autos[0]
# print(autos)
# output: ["audi", "volvo", "Ford"]

####################################################

# autos = ["BMW", "audi", "volvo", "Ford"]
# print(autos)
# Output: ["BMW", "audi", "volvo", "Ford"]

# del autos[1]
# print(autos)
# output: ["BMW", "volvo", "Ford"]

#########################################################

# Elemente mit der Methode pop() entfernen

# autos = ["BMW", "audi", "volvo", "Ford"]
# popped_auto = autos.pop()
# print(popped_auto)
# Output: Ford

##########################################################

# autos = ["BMW", "audi", "volvo", "ford"]
# last_owned = autos.pop()
# print("The last auto I owned was a " + last_owned.title() + ".")
# Output: The last auto I owned was a Ford.


##########################################################

# Element mit pop() von belibigen Stellen einer Liste entfernen
# autos = ["bmw", "audi", "volvo", "ford"]

# first_owned = autos.pop(0)
# print("The first auto I owned was a " + first_owned.title() + ".")
# Output: The first auto I owned was a Bmw.

################################################################

# Element anhand ihres Wertes entfernrn

# autos = ["bmw", "audi", "volvo", "ford"]
# print(autos)

# autos.remove("bmw")

# print(autos)
# Output: ["audi", "volvo", "ford"]

################################################################

# Element mit Grund und remove() entfernrn

# autos = ["bmw", "audi", "volvo", "ford"]
# print(autos)

# too_expensive = "bmw"
# autos.remove(too_expensive)
# print(autos)
# # Output: ["audi", "volvo", "ford"]
# print(f"\nA {too_expensive.title()} is too expensive for me.")
# # Output: A Bmw is too expensive for me.


################################################################

# Listen ordnen

# Listen mit sort() dauerhaft sortieren

# autos = ["BMW", "audi", "volvo", "ford"]

# autos.sort()

# print(autos)
# Output: ["BMW", "audi", "ford", "volvo"]

################################################################


# autos = ["BMW", "audi", "volvo", "ford"]
# autos.sort(reverse=True)

# print(autos)

# Output: ['volvo', 'ford', 'audi', 'BMW']


################################################################

# Listen Ausgeben in Listen ohne Klammern 1.

"""Dieser Code erstellt einen String autos_str, der die Elemente der 
Liste autos enthält, getrennt durch ein Komma und ein Leerzeichen. 
Anschließend wird dieser String ausgegeben, was zu einer Ausgabe ohne Klammern führt."""

# autos = ["BMW", "audi", "volvo", "ford"]
# autos_str = ", ".join(autos)
# print(autos_str)

# Output: BMW, audi, volvo, ford

################################################################

# # Listen Ausgeben in Listen ohne Klammern 2.

"""Hier wird jedes Element der Liste einzeln ausgegeben. 
Das end=' ' am Ende von print sorgt dafür, dass jedes 
Element in einer Zeile mit einem Leerzeichen getrennt wird."""

# autos = ["BMW", "audi", "volvo", "ford"]
# for auto in autos:
#     print(auto, end=" ")

# # Output: BMW audi volvo ford

################################################################

# # Listen Ausgeben in Listen ohne Klammern 3.
# Verwendung der *-Operator mit print:
#
"""Der *-Operator entpackt die Liste, so dass jedes Element als 
separater Parameter an print übergeben wird. Standardmäßig 
werden diese dann durch Leerzeichen getrennt."""

# autos = ["BMW", "audi", "volvo", "ford"]
# print(*autos)
# # Output: BMW audi volvo ford

################################################################

# #  Listen Ausgeben in Listen ohne Klammern 4.
# Verwendung von map und str.join

"""Hier wird map verwendet, um sicherzustellen, dass jedes Element der 
Liste in einen String umgewandelt wird (was in diesem Fall nicht 
notwendig ist, da alle Elemente bereits Strings sind), 
und dann werden diese Strings mit join zusammengefügt."""

# autos = ["BMW", "audi", "volvo", "ford"]
# print(" ".join(map(str, autos)))
# # # Output: BMW audi volvo ford

################################################################

# #  Listen Ausgeben in Listen ohne Klammern 5.
# Einfache Schleife mit manueller String-Konkatenation

"""In dieser Methode wird ein leerer String erstellt und jedes Element 
der Liste wird mit einem Leerzeichen hinzugefügt. strip() wird verwendet, 
um zusätzliche Leerzeichen am Ende des Strings zu entfernen"""

# autos = ["BMW", "audi", "volvo", "ford"]
# autos_str = ""
# for auto in autos:
#     autos_str += auto + " "
# print(autos_str.strip())
# # Output: BMW audi volvo ford

################################################################
