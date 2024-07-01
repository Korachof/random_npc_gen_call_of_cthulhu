import names
from random import randrange
import occupations

class NPC:
    def __init__(self, occupation, unique_attribute, skills):
        self._gender = self.set_gender()
        self._name = self.set_name(self._gender)
        self._age = self.set_age()
        self._occupation = self.set_occupation()
        self._unique_attribute = unique_attribute
        self._skills = skills
        self._characteristics_dict = {"Strength": None, "Constitution": None, "Size": None, "Dexterity": None, "Appearance": None, "Intelligence": None, "Power": None, "Education": None}

    def set_gender(self):
        """Set character gender
        0 = Male, 1 = Female
        returns: gender (STR)"""
        num = randrange(0, 2)

        if num == 0:
            gender = "Male"
        elif num == 1: 
            gender = "Female"

        return gender
    
    def set_age(self):
        """Set character age
        returns: age (INT)"""
        age = randrange(18, 100)

        return age

    def set_name(self, npc_gender):
        """Set character name
        parameter: npc_gender (STR)
        returns: name (STR)"""
        name = names.get_full_name(gender = npc_gender)

        return name

    def set_characteristics(self):
        """Set character characteristics
        random between 10 and 99
        returns: None (updates self._characteristics_dict)"""
        for key in self._characteristics_dict:
            self._characteristics_dict[key] = randrange(10, 100)

    def set_occupation(self):
        """Set character occupation
        random between 0 and 131
        returns: occupation (STR)"""
        occupation_index = randrange(0, 132)
        occupation = occupations.occupations_list[occupation_index]

        return occupation
    





        



    