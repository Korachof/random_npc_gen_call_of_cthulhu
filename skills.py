SKILLS_NUM = 11


skills_dict = {"Accountant": ["Accounting", "Appraise", "Charm", "Fast Talk", "Law", "Library Use", "Listen", "Persuade", "Psychology", "Occult", "Spot Hidden"], 
               "Acrobat": ["Jump", "Climb", "Disguise", "Listen", "Navigate", "Occult", "Psychology", "Ride", "Slight of Hand", "Stealth", "Throw"], 
               "Agency Detective": ["Law", "Charm", "Disguise", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "Library Use", "Persuade", "Psychology", "Stealth", "Track"],
               "Ambassador": ["Reputation", "Anthropology", "Disguise", "Fast Talk", "Intimidate", "History", "Language (Own)", "Language (Other)", "Law", "Persuade", "Psychology"],
               "Antique Dealer": ["Appraise", "Accounting", "Fast Talk", "History", "Library Use", "Navigate", "Occult", "Persuade", "Reputation", "Spot Hidden", "Track"],
               "Architect": ["Art/Craft (Architecture)", "Accounting", "Fast Talk", "History", "Language (Own)", "Law", "Library Use", "Lore (Any)", "Navigate", "Persuade", "Psychology"],
               "Artist": ["Art/Craft", "Charm", "Disguise", "Fast Talk", "History", "Library Use", "Lore (Any)", "Occult", "Persuade", "Photography", "Psychology"],
               "Author": ["Art/Craft (Writing)", "Charm", "Fast Talk", "History", "Language (Own)", "Language (Other)", "Library Use", "Natural World", "Psychology", "Occult", "Science (Choose)"],
               "Bank Robber": ["Drive Auto", "Appraise", "Electrical Repair", "Electronics", "Fast Talk", "Firearms", "Intimidate", "Mechanical Repair", "Persuade", "Spot Hidden", "Stealth"],
               "Barber": [],
               "Bartender": [],
               "Bible Salesman": []}


if __name__ == "__main__": 
    def skill_dict_checker(skills_dict):
        count = 0
        for key in skills_dict:
            if len(skills_dict[key]) != SKILLS_NUM:
                count += 1
                print(f"{key} does not have {SKILLS_NUM} skills")

        if count == 0:
            print(f"All occupations have {SKILLS_NUM} skills")


    skill_dict_checker(skills_dict)