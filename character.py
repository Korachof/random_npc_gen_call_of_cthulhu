import names
from random import randrange
from termcolor import colored, cprint
from occupations import occupations_list
from attributes import attributes_list
from skills import skills_dict


class NPC:
    def __init__(self):
        self._gender = self.set_gender()
        self._name = self.set_name()
        self._age = self.set_age()
        self._occupation = "Bank Robber"
        self._unique_attribute = self.set_unique_attribute()
        self._skills = {}
        self._characteristics_dict = {"Strength": None, "Constitution": None, "Size": None, "Dexterity": None, "Appearance": None, "Intelligence": None, "Power": None, "Education": None}
        self.set_characteristics()
        self._health = (self._characteristics_dict["Size"] + self._characteristics_dict["Constitution"]) // 10
        self._sanity = randrange(self._characteristics_dict["Power"] - 5, self._characteristics_dict["Power"] + 6)
        self._dodge = self._characteristics_dict["Dexterity"] // 2
        self._brawl = self.set_brawl()
        self._luck = self.set_luck()
        self.set_skills()
        self.set_skills_values()

    def get_health(self):
        """returns: health (INT)"""
        return self._health
    
    def get_sanity(self):
        """returns: sanity (INT)"""
        return self._sanity
    
    def get_dodge(self):
        """returns: dodge (INT)"""
        return self._dodge

    def set_brawl(self):
        """Set character brawl skill
        50% being str * dex // 2, 15% lower, 35% higher
        returns brawl (INT)"""
        starting_brawl = (self._characteristics_dict["Dexterity"] * self._characteristics_dict["Strength"]) // 100
        avg_check = randrange(0, 100)

        if avg_check < 51:
            return starting_brawl
        elif avg_check < 76:
            return starting_brawl - randrange(1, 21)
        elif avg_check < 100:
            brawl_increase = starting_brawl + randrange(1, 21)
            if brawl_increase > 99:
                brawl_increase = 99
            return brawl_increase

    def get_brawl(self):
        """returns: brawl (INT)"""
        return self._brawl

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
        name = names.get_full_name(gender=self._gender.lower())

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
            average_check = randrange(0, 3)
            if average_check == 0 or average_check == 3:
                self._characteristics_dict[key] = randrange(50, 76)
            elif average_check == 1:
                self._characteristics_dict[key] = randrange(26, 51)
            elif average_check == 2:
                self._characteristics_dict[key] = randrange(76, 100)

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
        temp_skills_pop_list = []
        skills_list = skills_dict[self._occupation]
        base_skill_values = [60, 60, 50, 50, 50, 40, 40, 40]
        base_index = randrange(0, 8)
        self._skills[skills_list[0]] = base_skill_values[base_index]
        skills_list.pop(0)
        base_skill_values.pop(base_index)
        for num in range(5):
            base_index = randrange(0, len(base_skill_values))
            skill_index = randrange(0, len(skills_list))
            self._skills[skills_list[skill_index]] = base_skill_values[base_index]
            popped_skill = skills_list[skill_index]
            temp_skills_pop_list.append(popped_skill)
            skills_list.pop(skill_index)
            base_skill_values.pop(base_index)
        
        for skill in temp_skills_pop_list:
            skills_list.append(skill)
            

    def set_skills_values(self):
        """sets the education based skill values for each skill
        returns: None"""
        skill_points = self._characteristics_dict["Education"]
        skill_list = []
        for key in self._skills:
            skill_list.append(key)
        while skill_points > 0:
            if skill_points >= 5:
                random_skill_index = randrange(0, 5)
                if self._skills[skill_list[random_skill_index]] < 95:
                    self._skills[skill_list[random_skill_index]] += 5
                    skill_points -= 5
            else:
                random_skill_index = randrange(0, 5)
                if self._skills[skill_list[random_skill_index]] < 100:
                    self._skills[skill_list[random_skill_index]] += 1
                    skill_points -= 1

    def set_luck(self):
        """Sets luck value based on 3d6 * 5"""
        d1 = randrange(1, 6)
        d2 = randrange(1, 6)
        d3 = randrange(1, 6)

        return (d1 + d2 + d3) * 5

    def get_luck(self):
        """returns: luck (INT)"""
        return self._luck
    
    def print_npc(self):
        print(f"Name: {colored(self.get_name(), 'light_green')}")
        print(f"Occupation: {colored(self.get_occupation(), 'light_green')}     Age: {colored(self.get_age(), 'light_green')}     Gender: {colored(self.get_gender(), 'light_green')}")
        print(f"Health: {colored(self.get_health(), 'light_green')}     Sanity: {colored(self.get_sanity(), 'light_green')}     Luck: {colored(self.get_luck(), 'light_green')}")
        print("Unique Attribute: " + colored(self.get_unique_attribute(), "light_green"))
        print(colored("Characteristics", "light_yellow"))
        for key in self._characteristics_dict:
            print(f"{key} : {colored(self.get_characteristic_value(key), 'light_green')}")
        print(colored("Skills", "yellow"))
        print(f"Dodge: {colored(self.get_dodge(), 'light_green')}")
        print(f"Fighting (Brawl): {colored(self.get_brawl(), 'light_green')}")
        for key in self.get_skills():
            print(f"{key} : {colored(self.get_skills()[key], 'light_green')}")
    
    def save_npc_txt_file(self):
        f = open(f"{self._name}-{self._occupation}-CoC-NPC.txt", "a")
        f.write(f"Name: {self.get_name()}\n")
        f.write(f"Occupation: {self.get_occupation()}     Age: {self.get_age()}     Gender: {self.get_gender()}\n")
        f.write(f"Health: {self.get_health()}     Sanity: {self.get_sanity()}     Luck: {self.get_luck()}\n")
        f.write(f"Unique Attribute: {self.get_unique_attribute()}\n")
        f.write("Characteristics\n")
        for key in self._characteristics_dict:
            f.write(f"{key} : {self.get_characteristic_value(key)}\n")
        f.write("Skills\n")
        f.write(f"Dodge: {self.get_dodge()}\n")
        f.write(f"Fighting (Brawl): {self.get_brawl()}\n")
        for key in self.get_skills():
            f.write(f"{key} : {self.get_skills()[key]}\n")
        f.close()
        print(f"Saved {self._name} as {self._name}-{self._occupation}-CoC-NPC.txt")
        

