import os


class View:
    '''
        Klasa View odpowiada za wyświetlenie informacji do urzytkownika
    '''
    def __init__(self):
        self.option_main_menu  = [
            "1. [💻] Wyświetl wydarzenie(a)",
            "2. [➕] Dadaj wydarzenie",
            "3. [❌] Usuń wydarzenie",
            "4. [🔧] Operacje",
            "5. [↳] Wyjście z programu"
        ]

    def show_main_menu(self):
        print("\t 📆 Program Planner 📆")
        for option in self.option_main_menu:
            print(option)

    def show_operation_menu(self):
        print("\t1. Sortuj wg daty i czasu rosnąco")
        print("\t2. Sortuj wg daty i czasu malejąco")
        print("\t3. Sortuj wg nazwy rosnąco")
        print("\t4. Sortuj wg nazwy malejąco")
        print("\t5. Wyszukaj wg słowa kluczowego")
        print("\t6. [↳]Powrót do głównego menu.")

    def show_option_main_menu(self, _id):
        print("\n",self.option_main_menu[_id])

    def delete_menu(self):
        print("Podaj numer wydarzenia które chcesz usunąć lub wpisaz NIE jeśli chcesz wrócić: ", end='')

    def input_event(self):
        print("\nPodaj informację o nowym wydarzeniu (* - dane obowiązkowe)")

    def input_data(self):
        print("\n\tPodaj datę wydarzenia (rrrr-mm-dd)*: ", end='')

    def input_time(self):
        print("\n\tPodaj godzinę(y) i minutę(y) wydarzenia (gg:mm)*: ", end='')

    def input_name(self):
        print("\n\tPodaj nazwę wydarzenia*: ", end='')

    def input_desc(self):
        print("\n\tPodaj opis wydarzenia: ", end='')

    def input_word(self):
        print("\nPodaj słowa po którym chcesz wyszukać wydarzenia: ", end='')

    def input_option(self):
        print("\nWybierz jedną z opcji: ", end='')


    def show_events(self, event_data, text):

        if event_data != []:
            print(f"\n💻 Twoje wydarzenia: {text}")
            for number, event in enumerate(event_data):
                print(f"\t{number+1}.  {event['date']} {event['time']} {event['name']} {event['desc']}")
        else:
            self.show_error("Niestety nie udało się znaleść odpowoednich wydarzeń")
        print()


    def show_error(self, error_msg):
        print(f"\t\t⛔ Błąd: {error_msg} ⛔\n")

    def show_success(self, success_msg):
        print(f"\n\t\t✅ Polecenie: {success_msg} wykonano pomyślnie\n")


    def clear_screen(self, deley=True):
        if deley: input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


