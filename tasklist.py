# Dies ist ein Programm um eine Aufgabenliste zu erstellen und abzuarbeiten.
from operator import itemgetter, attrgetter
import csv
from datetime import *

# Aufgabenliste initialisieren
tasklist = []

# Eine Funktion um eine Aufgabe der Liste hinzuzufügen
def add_task():
    is_date = 0
    task = input("Welche Aufgabe soll hinzugefügt werden?\n")

    while True:
        wantTimeLimit = input("\nMöchten Sie ein Fälligkeitsdatum hinzufügen? Bitte geben Sie 'Ja' oder 'Nein' ein.\n").capitalize()
        if wantTimeLimit == "Ja":
            due_date = input("\nBis wann ist die Aufgabe fällig?\nBitte geben Sie ein Datum ein. Format: Year-Month-Day Stunde:Minute:Sekunde\n")
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
        sortedList = sorted(tasklist, key = itemgetter(1))

        for i in tasklist:
            type_list = str(type(tasklist[x]))

            if type_list == "<class 'list'>":
                listLength = len(sortedList[x])

                if listLength == 3:
                    print(f"{sortedList[x][0]} ist {sortedList[x][1]} wichtig. Die Aufgabe ist am {sortedList[x][2]} fällig.")

                elif listLength == 2:
                    print(f"{sortedList[x][0]} ist {sortedList[x][1]} wichtig.")

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
        print("\n----- Office - Taskliste -----")
        print("1. Eine Aufgabe der Liste hinzufügen")
        print("2. Aufgabenliste zeigen")
        print("3. Aufgabenliste Exportieren")
        print("4. Programm beenden")
        print("-----")

        if tasklist:
            sortedList = sorted(tasklist, key = itemgetter(1))
            current_date = datetime.now()
            y = 0
            for i in sortedList:
                check_date = datetime.strptime(sortedList[y][2], '%Y-%m-%d %H:%M:%S')
                if check_date <= current_date:
                    activeTask = sortedList[y]
                    print(f"{activeTask[0]} ist {activeTask[1]} wichtig. Die Aufgabe war am {activeTask[2]} fällig.")
                y += 1

        choice = input("\nWas möchten Sie tun?\n")

        if choice == "1":
            add_task()

        elif choice == "2":
            show_tasklist()

        elif choice == "3":
            with open('Task-List-Export', 'w') as f:
                # using csv.writer method from CSV Package
                write = csv.writer(f)
                fields = ['Tasks', 'Prioritys', 'Due-Time']
                write.writerow(fields)
                sortedList = sorted(tasklist, key = itemgetter(1))
                write.writerows(sortedList)

        elif choice == "4":
            print("Das Programm wird beendet. Auf Wiedersehen!")
            break

        else:
            print("Bitte geben Sie nur 1, 2, 3 oder 4 ein.")

if __name__ == "__main__":
    main()