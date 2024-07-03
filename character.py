import names
from random import randrange
from occupations import occupations_list
from attributes import attributes_list
from skills import skills_dict

class NPC:
    def __init__(self):
        self._gender = self.set_gender()
        self._name = self.set_name(self._gender)
        self._age = self.set_age()
        self._occupation = self.set_occupation()
        self._unique_attribute = self.set_unique_attribute()
        self._skills = []
        self._characteristics_dict = {"Strength": None, "Constitution": None, "Size": None, "Dexterity": None, "Appearance": None, "Intelligence": None, "Power": None, "Education": None}
        self.set_characteristics()
        self.set_skills()

    def get_gender(self):
        """returns: gender (STR)"""
        return self._gender
    
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
    
    def get_age(self):
        """returns: age (INT)"""
        return self._age
    
    def set_age(self):
        """Set character age
        returns: age (INT)"""
        age = randrange(18, 100)

        return age

    def get_name(self):
        """returns: name (STR)"""
        return self._name

    def set_name(self):
        """Set character name
        parameter: npc_gender (STR)
        returns: name (STR)"""
        name = names.get_full_name(gender = self._gender)

        return name
    
    def get_characteristic_value(self, characteristic):
        """returns the chosen characteristic value
        parameter: characteristic (STR)
        returns: characteristic value (INT)"""
        return self._characteristics_dict[characteristic]

    def set_characteristics(self):
        """Set character characteristics
        random between 10 and 99
        returns: None (updates self._characteristics_dict)"""
        for key in self._characteristics_dict:
            self._characteristics_dict[key] = randrange(10, 100)

    def get_occupation(self):
        """returns: occupation (STR)"""
        return self._occupation

    def set_occupation(self):
        """Set character occupation
        random between 0 and 131
        returns: occupation (STR)"""
        occupation_index = randrange(0, len(attributes_list))
        occupation = occupations_list[occupation_index]

        return occupation
    
    def get_unique_attribute(self):
        """returns: unique attribute (STR)"""
        return self._unique_attribute
    
    def set_unique_attribute(self):
        """Set character unique attribute
        random based on list length
        returns: unique attribute"""
        attribute_index = randrange(0, len(attributes_list))
        attribute = attributes_list[attribute_index]

        return attribute
    
    def get_skills(self):
        """returns: skill list (LIST)"""
        return self._skills
    
    def set_skills(self):
        """Set character skills list
        Based on character occupation - 1 base skill, 5 random out of 9 others
        returns: character skill list (LIST)"""
        skills_list = skills_dict[self._occupation]

        self._skills.append(skills_list[0])
        skills_list.pop(0)
        skill_index = randrange(0, len(skills_list))
        self._skills.append(skills_list[skill_index])
        skills_list.pop(skill_index)
        skill_index = randrange(0, len(skills_list))
        self._skills.append(skills_list[skill_index])
        skills_list.pop(skill_index)
        skill_index = randrange(0, len(skills_list))
        self._skills.append(skills_list[skill_index])
        skills_list.pop(skill_index)
        skill_index = randrange(0, len(skills_list))
        self._skills.append(skills_list[skill_index])
        skills_list.pop(skill_index)
        skill_index = randrange(0, len(skills_list))
        self._skills.append(skills_list[skill_index])
        skills_list.pop(skill_index)
        