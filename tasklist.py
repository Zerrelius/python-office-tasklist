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
        type_list = str(type(tasklist[x]))
        for i in tasklist:
            if type_list == "<class 'list'>":
                print(f"{tasklist[x][x]} ist in {tasklist[x][(x+1)]} fällig.")
            else:
                print(f"{tasklist[x]} ist noch fällig.")
            x += 1
    else:
        print("Deine Taskliste ist leer.")

# add_task()
# show_tasklist()