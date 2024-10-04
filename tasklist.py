# Dies ist ein Programm um eine Aufgabenliste zu erstellen und abzuarbeiten.

# Aufgabenliste initialisieren
tasklist = []

# Eine Funktion um eine Aufgabe der Liste hinzuzufügen
def add_task():
    task = input("Welche Aufgabe soll hinzugefügt werden?\n")
    tasklist.append(task)
    while 1 == 1:
        wantTimeLimit = input("\nMöchten Sie ein Fälligkeitsdatum hinzufügen? Bitte geben Sie 'Ja' oder 'Nein' ein.\n")
        if wantTimeLimit == ("Ja" or "ja"):
            timeLimit = input("\nBis wann ist die Aufgabe fällig?\n")
            tasklist.append(timeLimit)
            break
        elif wantTimeLimit == ("Nein" or "nein"):
            print("\nIhrer Aufgabe wurd kein Fälligkeitsdatum hinzugefügt.")
            break
        else:
            print("\nBitte geben Sie nur 'Ja' oder 'Nein ein.")
    print(f"\nSie haben {task} der Aufgabenliste hinzugefügt. Die Aufgabe ist bis {timeLimit} zu erledigen.\n")

# add_task()