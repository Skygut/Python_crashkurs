# Eine Variante mit while True und break
# prompt = "\nGeben Sie eine Komponente fuer ihre Pizza ein: "
# prompt += "\nFuer Beaenden geben Sie q ein! "

# while True:

#     componente = input(prompt)

#     if componente == "q":
#         print("Programma wird beaendet!")
#         break

#     else:
#         print(f"Ihre Pizza mit der Komponente '{componente.title()}' wird zubereitet!")

# Zweite Variante mit active = True
# while active:

prompt = "\nIhre Komponente bitte: "

active = True

while active:

    componente = input(prompt)

    if componente == "q":
        active = False
        print("\nDas Programma wird beaendet")
    else:
        print("Ihre Komponente ist {componente.title()} und wird zubereitet")
