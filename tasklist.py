# Dies ist ein Programm um eine Aufgabenliste zu erstellen und abzuarbeiten.

# Aufgabenliste initialisieren
tasklist = []

# Eine Funktion um eine Aufgabe der Liste hinzuzufügen
def add_task():
    is_date = 0
    task = input("Welche Aufgabe soll hinzugefügt werden?\n")

    while True:
        wantTimeLimit = input("\nMöchten Sie ein Fälligkeitsdatum hinzufügen? Bitte geben Sie 'Ja' oder 'Nein' ein.\n").capitalize()
        if wantTimeLimit == "Ja":
            due_date = input("\nBis wann ist die Aufgabe fällig?\n")
            is_date = 1
            break

        elif wantTimeLimit == "Nein":
            break

        else:
            print("\nBitte geben Sie nur 'Ja' oder 'Nein ein.")

    while True:
        priority = input("\nWelche Priorität möchten Sie der Aufgabe zuweisen? Beispiele: Hoch, Mittel und Niedrig\n")

        if is_date == 1:
            task_data = [task, priority, due_date]
            tasklist.append(task_data)
            print(f"\nSie haben {task} der Aufgabenliste hinzugefügt. Die Aufgabe ist bis {due_date} zu erledigen. Sie haben der Aufgabe eine {priority} gegeben.\n")
            break
        else:
            task_data = [task, priority]
            tasklist.append(task_data)
            print(f"\nSie haben {task} der Aufgabenliste hinzugefügt. Ohne Fälligkeitsdatum. Mit der Priorität {priority} hinzugefügt.\n")
            break

def show_tasklist():
    if tasklist:
        print("Ihre Aufgabenliste lautet:\n-----")
        x = 0
        for i in tasklist:
            type_list = str(type(tasklist[x]))
            tasklist.sort(key = len([x][1]))
            if type_list == "<class 'list'>":
                listLength = len(tasklist[x])
                if listLength == 3:
                    print(f"{tasklist[x][0]} ist in {tasklist[x][1]} fällig. Die Priorität ist {tasklist[x][2]}.")
                elif listLength == 2:
                    print(f"{tasklist[x][0]} ist {tasklist[x][1]} wichtig.")
                else:
                    print(f"{tasklist[x]} ist noch zutun.")
            x += 1
        print("-----")
        print("Ihre Aufgabenliste endet hier.\n")
    else:
        print("Deine Taskliste ist leer.\n")

# add_task()
# show_tasklist()

def main():
    while True:
        print("----- Office - Taskliste -----")
        print("1. Eine Aufgabe der Liste hinzufügen")
        print("2. Aufgabenliste zeigen")
        print("3. Programm beenden")
        print("-----")
        choice = input("\nWas möchten Sie tun?\n")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasklist()
        elif choice == "3":
            print("Das Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Bitte geben Sie nur 1, 2 oder 3 ein.")

if __name__ == "__main__":
    main()