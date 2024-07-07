from consolemenu import *
from consolemenu.items import *
import character
import sys


class MenuOptions():
    def __init__(self):
        self._menu = ConsoleMenu("Welcome to the Unofficial Random NPC Generator!", "Please select an option below", None, None, None, None, False, False)
        self._create_character = FunctionItem("Create NPC", self.call_character_class)
        self._exit_program = FunctionItem("Exit", sys.exit)
        self._menu.append_item(self._create_character)
        self._menu.append_item(self._exit_program)
        self._npc = None
        self._show = self._menu.show()
        

    def call_character_class(self):
        self._npc = character.NPC()
        self._npc.print_npc()
        self.new_menu()

    def new_menu(self):
        self._menu = ConsoleMenu(f"You created {self._npc.get_name()}! (scroll up for details)", "Please select an option below", None, None, None, None, False, False)
        self._menu.append_item(self._create_character)
        self._menu.append_item(FunctionItem("Save NPC", self._npc.save_npc_txt_file))
        self._menu.append_item(self._exit_program)
        self._show = self._menu.show()

def menu_options():
    menu = ConsoleMenu("Welcome to the Unofficial Call of Cthulhu Random NPC Generator!", "Please select an option below", None, None, None, None, False, False)

    # Create some items

    # MenuItem is the base class for all items, it doesn't do anything when selected
    create_character = FunctionItem("Create NPC", call_character_class)
    exit_program = FunctionItem("Exit", sys.exit)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(create_character)
    menu.append_item(exit_program)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()

def call_character_class():
    npc = character.NPC()
    npc.print_npc()


if __name__ == "__main__":
    menu = MenuOptions()