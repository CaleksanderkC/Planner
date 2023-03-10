import os


class View:
    '''
        Klasa View odpowiada za wy艣wietlenie informacji do urzytkownika
    '''
    def __init__(self):
        self.option_main_menu  = [
            "1. [馃捇] Wy艣wietl wydarzenie(a)",
            "2. [鉃昡 Dadaj wydarzenie",
            "3. [鉂宂 Usu艅 wydarzenie",
            "4. [馃敡] Operacje",
            "5. [鈫砞 Wyj艣cie z programu"
        ]

    def show_main_menu(self):
        print("\t 馃搯 Program Planner 馃搯")
        for option in self.option_main_menu:
            print(option)

    def show_operation_menu(self):
        print("\t1. Sortuj wg daty i czasu rosn膮co")
        print("\t2. Sortuj wg daty i czasu malej膮co")
        print("\t3. Sortuj wg nazwy rosn膮co")
        print("\t4. Sortuj wg nazwy malej膮co")
        print("\t5. Wyszukaj wg s艂owa kluczowego")
        print("\t6. [鈫砞Powr贸t do g艂贸wnego menu.")

    def show_option_main_menu(self, _id):
        print("\n",self.option_main_menu[_id])

    def delete_menu(self):
        print("Podaj numer wydarzenia kt贸re chcesz usun膮膰 lub wpisaz NIE je艣li chcesz wr贸ci膰: ", end='')

    def input_event(self):
        print("\nPodaj informacj臋 o nowym wydarzeniu (* - dane obowi膮zkowe)")

    def input_data(self):
        print("\n\tPodaj dat臋 wydarzenia (rrrr-mm-dd)*: ", end='')

    def input_time(self):
        print("\n\tPodaj godzin臋(y) i minut臋(y) wydarzenia (gg:mm)*: ", end='')

    def input_name(self):
        print("\n\tPodaj nazw臋 wydarzenia*: ", end='')

    def input_desc(self):
        print("\n\tPodaj opis wydarzenia: ", end='')

    def input_word(self):
        print("\nPodaj s艂owa po kt贸rym chcesz wyszuka膰 wydarzenia: ", end='')

    def input_option(self):
        print("\nWybierz jedn膮 z opcji: ", end='')


    def show_events(self, event_data, text):

        if event_data != []:
            print(f"\n馃捇 Twoje wydarzenia: {text}")
            for number, event in enumerate(event_data):
                print(f"\t{number+1}.  {event['date']} {event['time']} {event['name']} {event['desc']}")
        else:
            self.show_error("Niestety nie uda艂o si臋 znale艣膰 odpowoednich wydarze艅")
        print()


    def show_error(self, error_msg):
        print(f"\t\t鉀? B艂膮d: {error_msg} 鉀擻n")

    def show_success(self, success_msg):
        print(f"\n\t\t鉁? Polecenie: {success_msg} wykonano pomy艣lnie\n")


    def clear_screen(self, deley=True):
        if deley: input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')


