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
               "Barber": ["Art/Craft (Hairstyling)", "Accounting", "Charm", "Disguise", "Drive Auto", "Fast Talk", "First Aid", "Persuade", "Psychology", "Psychoanalysis", "Reputation"],
               "Bartender": ["Art/Craft (Mixology)", "Accounting", "Charm", "Electrical Repair", "Fast Talk", "First Aid", "Firearms (Shotgun/Rifle)", "Persuade", "Psychology", "Science (Chemistry)", "Sleight of Hand"],
               "Bible Salesman": ["Persuade", "Charm", "Fast Talk", "History", "Intimidate", "Language (Own)", "Library Use", "Navigate", "Occult", "Psychology", "Stealth"],
               "Big Game Hunter": ["Firearms (Shotgun/Rifle)", "Climb", "Drive Auto", "First Aid", "Jump", "Listen", "Natural World", "Navigate", "Stealth", "Survival", "Track"],
               "Book Dealer": ["Library Use", "Accounting", "Appraise", "Drive Auto", "History", "Language (Own)", "Language (Other)", "Listen", "Navigate", "Occult", "Persuade"],
               "Bookie": ["Accounting", "Appraise", "Fast Talk", "Firearms (Handgun)", "Intimidate", "Law", "Persuade", "Psychology", "Reputation", "Sleight of Hand", "Track"],
               "Boss": ["Reputation", "Accounting", "Drive Auto", "Electrical Repair", "Fast Talk", "First Aid", "Intimidate", "Law", "Mechanical Repair", "Persuade", "Psychology"],
               "Bounty Hunter": ["Track", "Accounting", "Climb", "Drive Auto", "Electrical Repair", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "Jump", "Persuade", "Survival", "Stealth"],
               "Boxer": ["Fighting (Punch)", "Charm", "Fast Talk", "First Aid", "History", "Intimidate", "Listen", "Sleight of Hand", "Spot Hidden", "Swim", "Throw"],
               "Burglar": ["Stealth", "Appraise", "Climb", "Disgiuse", "Electrical Repair", "Firearms (Handgun)", "Jump", "Listen", "Locksmith", "Spot Hidden:", "Stealth"],
               "Bus Driver": ["Drive Auto", "Electrical Repair", "History", "Intimidate", "Law", "Listen", "Mechanical Repair", "Navigate", "Occult", "Persuade", "Psychology"],
               "Catholic Priest": [],
               "Clergyman": [],
               "Clerk": [],
               "Cocktail Waitress": []}


if __name__ == "__main__": 
    def skill_dict_checker(skills_dict):
        count = 0
        for key in skills_dict:
            if len(skills_dict[key]) != SKILLS_NUM:
                count += 1
                print(f"{key} only has {len(skills_dict[key])}/{SKILLS_NUM} skills")

        if count == 0:
            print(f"All occupations have {SKILLS_NUM} skills")


    skill_dict_checker(skills_dict)