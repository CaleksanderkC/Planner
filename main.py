from model import Model
from view import View
from controller import Controller


class App():
    '''
        Class App wiąże opcje wybrane przez urzytkownika z funkcjami controllera
    '''
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)

    def run(self):

        while True:
            option = self.controller.main_menu()

            if option == 1:
                self.view.show_events(self.model.data(), '')
                self.view.clear_screen()
            elif option == 2: self.controller.add_event()
            elif option == 3: self.controller.delete_event()
            elif option == 4:
                while True:
                    option2 = self.controller.operation_mein()
                    if option2 == 1: self.controller.show_sort_date_time(False)
                    if option2 == 2: self.controller.show_sort_date_time(True)
                    if option2 == 3: self.controller.show_sort_name(False)
                    if option2 == 4: self.controller.show_sort_name(True)
                    if option2 == 5: self.controller.show_key_word()
                    if option2 == 6:
                        self.view.clear_screen(deley=False)
                        break

            else: self.controller.exit_program()

if __name__ == '__main__':
    app = App()
    try:
        app.run()
    except KeyboardInterrupt:
        pass