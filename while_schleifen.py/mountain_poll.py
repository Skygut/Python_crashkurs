# Ein Dictionary mit Benutzereingabe fuellen

responses = {}

# Richtet ein Flag ein, um anyugeben, dass die Umfrage aktive bleiben soll.

polling_active = True

while polling_active:
    # Bittet den Benutzer um Eingabe seines Namens und der Antwort.
    name = input("\nWhat is your name? ")
    response = input("Whaich mountain would you like to climb someday? ")
    # Speichert die Antwort im Dictionary:
    responses[name] = response

    # Frag, ob noch jemande an der Umfrage teilnehmen wird

    repeat = input("would you like to let another person respond? (yes/no)")
    if repeat == "no":
        polling_active = False

# Die Umfrage ist abgeschlossen, die Ergebnisse werden angezeigt.
print("\n--- Poll Resukts ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}. ")
