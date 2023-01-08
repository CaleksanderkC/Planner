import sys


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def main_menu(self):
        '''
            wyświetla główne meni i pobiera opcje od urzytkownika
        '''
        option = 5
        self.view.show_main_menu()

        while True:
            try:
                self.view.input_option()
                option = int(input())
            except ValueError:
                self.view.show_error("Musisz podać liczbę")
            else:
                if option < 1 or option > 5:
                    self.view.show_error("Liczba musi być z zakresu 1 do 5")
                else:
                    break
        return option


    def operation_mein(self):
        '''
            wyświetla meni Operacje i pobiera opcje od urzytkownika
        '''
        option = 6
        self.view.clear_screen(deley=False)
        self.view.show_main_menu()
        self.view.show_option_main_menu(3)
        self.view.show_operation_menu()
        while True:
            try:
                self.view.input_option()
                option = int(input())
            except ValueError:
                self.view.show_error("Musisz podać liczbę")
            else:
                if option < 1 or option > 6:
                    self.view.show_error("Liczba musi być z zakresu 1 do 6")
                else:
                    break
        return option


    def add_event(self):
        '''
            opcja 2 dodaje wydarzenie
        '''
        self.view.show_option_main_menu(1)
        self.view.input_event()

        option = False
        while not option:
            self.view.input_data()
            date = input()
            option = self.model.check_date(date)
            if not option: self.view.show_error("nieprawidłowy format daty musi być (rrrr-mm-dd)")

        option = False
        while not option:
            self.view.input_time()
            time = input()
            option = self.model.check_time(time)
            if not option: self.view.show_error("nieprawidłowy format czasu musi być (gg:mm)")

        option = False
        while not option:
            self.view.input_name()
            name = input()
            option = self.model.check_name(name)
            if not option: self.view.show_error("Musisz podać nazwę wydarzenia")

        self.view.input_desc()
        desc = input()

        self.model.add(date, time, name, desc)
        self.view.show_success("Dadaj wydarzenie")
        self.view.clear_screen()


    def delete_event(self):
        '''
            opcja 3 usuwa wydarzenie
        '''
        data = self.model.data()
        self.view.show_option_main_menu(2)
        self.view.show_events(data, "Ktore z nich chcesz usunąć")
        
        if data != []:
            delete_id = 0
            while True:
                self.view.delete_menu()
                delete_id = input()
                if delete_id.lower() == "nie":
                    self.view.clear_screen(deley=False)
                    return
                try:
                    delete_id = int(delete_id)
                except ValueError:
                    self.view.show_error("Musisz podać liczbę")
                else:

                    if ( delete_id < 1 or delete_id > len(data) ):
                        self.view.show_error(f"Liczba musi być z zakresu 1 do {len(data)}")
                    else:
                        break

            self.model.delete(delete_id-1)
            self.view.show_success("Usuń wydarzenie")
        self.view.clear_screen()


    def show_sort_date_time(self, rev=False):
        '''
            opcja 1,2 w Operacjach
        '''
        data = self.model.data()
        data.sort(reverse=rev, key=lambda event: f"{event['date']}/{event['time']}")
        msg = "malejąco" if rev else "rosnąco"
        self.view.show_events(data, f"Posotrowane Według daty i czasu {msg}")
        self.view.clear_screen()


    def show_sort_name(self, rev=False):
        '''
            opcja 3,4 w Operacjach
        '''
        data = self.model.data()
        data.sort(reverse=rev, key=lambda event: event['name'])
        msg = "malejąco" if rev else "rosnąco"
        self.view.show_events(data, f"Posotrowane Według nazwy {msg}")
        self.view.clear_screen()


    def show_key_word(self):
        '''
            opcja 5 w Operacjach
        '''
        data = self.model.data()
        self.view.input_word()
        str_input = input()
        words = str_input.split(' ')

        data_with_word = []
        for word in words:
            for event in data:
                if word.lower() in event['name'].lower() and event not in data_with_word:
                    data_with_word.append(event)
                if word.lower() in event['desc'].lower() and event not in data_with_word:
                    data_with_word.append(event)    


        self.view.show_events(data_with_word, "Zawierające słowa kluczowe")
        self.view.clear_screen()


    def exit_program(self):
        sys.exit() 
