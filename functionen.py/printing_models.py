# """Eine Liste mithilfe einer Funktion aendern"""

# """Erstellt eine Liste der zu druckenden Entwurfe. """

# unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# """Simuliert den Druck der einzelnen Entwurfe, bis keiner mehr uebrig ist. """
# """Verschiebt jeden Entwurf nach dem Druck in completed_models."""
# while unprinted_design:
#     current_design = unprinted_design.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# """Zeigt die Liste der fertigen Modelle an."""

# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(f"\n{completed_model}")

# # Output:
# # The following models have been printed:

# # dodecahedron

# # robot pendant

# # phone case

################################

"""Eine Liste mithilfe einer Funktion aendern"""

"""Erstellt eine Liste der zu druckenden Entwurfe. """


"""Simuliert den Druck der einzelnen Entwurfe, bis keiner mehr uebrig ist. """
"""Verschiebt jeden Entwurf nach dem Druck in completed_models."""


def print_models(unprinted_designs, cpmpleted_models):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


"""Zeigt die Liste der fertigen Modelle an."""


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(f"\n{completed_model}")


unprinted_design = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)

# # Output:
# # Printing model: dodecahedron
# # Printing model: robot pendant
# # Printing model: phone case

# # The following models have been printed:

# # dodecahedron

# # robot pendant

# phone case
