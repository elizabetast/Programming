from notes_applic import NotesApp
import sys
from errors import *


class NotesHandler:
    def __init__(self, notes_func):
        self.notes_func: NotesApp = notes_func
        self.menu = (("Notebook Menu: ", None),
                     ("1. Show all notes", self.notes_func.show_notes),
                     ("2. Search notes", self.notes_func.search_notes),
                     ("3. Add note", self.notes_func.add_note),
                     ("4. Modify note", self.notes_func.modify_note),
                     ("5. Min-time note", self.notes_func.min),
                     ("6. Quit", self.completion))

    def completion(self):
        print("Thank you for using your Notebook today.")
        sys.exit(0)

    def handler_app(self):
        try:
            while True:
                for choice in self.menu:
                    print(choice[0])
                choose_option = input("Enter an option: ")
                if choose_option.isnumeric() and 0 < int(choose_option) < 7:
                    action = self.menu[int(choose_option)][1]
                    print(80 * "=")
                    action()
                else:
                    print(f"{choose_option} is not a valid choice")
        except InvalidOptionError as error:
            print(str(error))
