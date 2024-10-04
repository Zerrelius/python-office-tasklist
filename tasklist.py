# Dies ist ein Programm um eine Aufgabenliste zu erstellen und abzuarbeiten.

# Aufgabenliste initialisieren
tasklist = []

# Eine Funktion um eine Aufgabe der Liste hinzuzufügen
def add_task():
    task = input("Welche Aufgabe soll hinzugefügt werden?\n")

    while True:
        wantTimeLimit = input("\nMöchten Sie ein Fälligkeitsdatum hinzufügen? Bitte geben Sie 'Ja' oder 'Nein' ein.\n").capitalize()
        if wantTimeLimit == "Ja":
            due_date = input("\nBis wann ist die Aufgabe fällig?\n")
            # task_data = {
            #     'task': task,
            #     'due_date': due_date,
            #     # 'priority': priority
            # }
            task_data = [task, due_date]
            tasklist.append(task_data)
            print(f"\nSie haben {task} der Aufgabenliste hinzugefügt. Die Aufgabe ist bis {due_date} zu erledigen.\n")
            break

        elif wantTimeLimit == "Nein":
            print("\nIhrer Aufgabe wurd kein Fälligkeitsdatum hinzugefügt.")
            tasklist.append(task)
            print(f"\nSie haben {task} der Aufgabenliste hinzugefügt. Ohne Fälligkeitsdatum.\n")
            break

        else:
            print("\nBitte geben Sie nur 'Ja' oder 'Nein ein.")

def show_tasklist():
    if tasklist:
        print("Ihre Aufgabenliste lautet:\n-----")
        x = 0
        for i in tasklist:
            type_list = str(type(tasklist[x]))
            if type_list == "<class 'list'>":
                print(f"{tasklist[x][0]} ist in {tasklist[x][1]} fällig.")
            else:
                print(f"{tasklist[x]} ist noch fällig.")
            x += 1
    else:
        print("Deine Taskliste ist leer.")

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