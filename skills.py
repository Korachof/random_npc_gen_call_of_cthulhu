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
               "Catholic Priest": ["Library Use", "Accounting", "History", "Intimidate", "Language (Own)", "Language (Latin)", "Listen", "Occult", "Persuade", "Psychology", "Reputation"],
               "Clergyman": ["Psychology", "Accounting", "Charm", "Drive Auto", "Fast Talk", "History", "Language (Own)", "Library Use", "Listen", "Persuade", "Reputation"],
               "Clerk": ["Accounting", "Drive Auto", "Fast Talk", "Language (Own)", "Listen", "Persuade", "Psychology", "'Reputation", "Sleight of Hand", "Spot Hidden", "Stealth"],
               "Cocktail Waitress": ["Fast Talk", "Accounting", "Charm", "First Aid", "Listen", "Persuade", "Psychology", "Read Lips", "Sleight of Hand", "Spot Hidden", "Track"],
               "Communist/Radical": ["Persuade", "Disguise", "Fast Talk", "Firearms (Handgun)", "History", "Intimidate", "Language (Own)", "Language (Other)", "Library Use", "Psychology", "Track"],
               "Company Officer/Executive": ["Reputation", "Accounting", "Appraise", "Charm", "Disguise", "Fast Talk", "Listen", "Intimidate", "Persuade", "Psychology", "Swim"],
               "Columnist": ["Reputation", "Charm", "Disguise", "Fast Talk", "Language (Own)", "Library Use", "Listen", "Occult", "Persuade", "Psychology" "Spot Hidden", "Stealth"],
               "Con Man": ["Appraise", "Charm", "Disguise", "Fast Talk", "Firearms (Handgun)", "Jump", "Listen", "Locksmith", "Persuade", "Psychology", "Spot Hidden"],
               "Deacon/Elder": ["Persuade", "Accounting", "Anthropology", "Charm", "Fast Talk", "History", "Language (Own)", "Listen", "Persuade", "Psychology", "Reputation"],
               "Deep-Sea Diver": ["Swim", "Animal Handling", "Demolitions", "Electronics", "Firearms (Rifle/Shotgun)", "Mechanical Repair", "Natural History (Marine)", "Pilot (Boat)", "Science (Marine Biology)", "Spot Hidden", "Survival"],
               "Dentist": ["Art/Craft (Dentistry)", "Accounting", "Fast Talk", "First Aid", "Library Use", "Medicine", "Persuade", "Psychology", "Reputation", "Science (Biology)", "Science (Chemistry)"],
               "Designer": ["Art/Craft (Design)", "Accounting", "Appraise", "Charm", "Electrical Repair", "History", "Library Use", "Mechanical Repair", "Persuade", "Photography", "Psychology"],
               "Dilettante": ["Appraise", "Art/Craft (Drawing)", "Art/Craft (Painting)", "Art/Craft (Sculpture)", "History", "Language (Own)", "Language (Other)", "Occult", "Photography", "Psychology", "Reputation"],
               "DJ": ["Art/Craft (DJing)", "Charm", "Disguise", "Fast Talk", "Firearms (Handgun)", "Electronics", "Jump", "Listen", "Mechanical Repair", "Persuade", "Psychology"],
               "Drifter": ["Fast Talk", "Climb", "Jump", "Firearms (Handgun)", "Listen", "Natural History", "Persuade", "Spot Hidden", "Stealth", "Survival", "Track"],
               "Editor": ["Language (Own)", "Art/Craft (Writing)", "Accounting", "Fast Talk", "Firearms (Handgun)", "History", "Intimidate", "Listen", "Persuade", "Psychology", "Reputation"],
               "Elected Official": ["Fast Talk", "Charm", "Disguise", "Intimidate", "Language (Own)", "History", "Law", "Persuade", "Psychology", "Read Lips", "Reputation"],
               "Entertainer": ["Art/Craft (Entertainment)", "Animal Handling", "Charm", "Disguise", "Fast Talk", "Jump", "Language (Own)", "Persuade", "Psychology", "Sleight of Hand", "Throw"],
               "Explorer": ["Survival", "Climb", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "History", "Jump", "Medicine", "Natural History", "Navigate", "Swim"],
               "Farmer": ["Animal Handling", "Accounting", "'Climb", "Drive Auto", "Electrical Repair", "Fighting (Axe)", "First Aid", "Mechanical Repair", "Medicine", "Natural History", "Operate Heavy Machinery"],
               "Federal Agent": ["Law", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "Intimidate", "Listen", "Persuade", "Spot Hidden", "Stealth", "Track"],
               "Fence": ["Accounting", "Appraise", "Fast Talk", "Firearms (Handgun)", "Law", "Locksmith", "Persuade", "Psychology", "Reputation", "Sleight of Hand", "Stealth"],
               "Field Researcher": ["Listen", "Animal Handling", "Anthropology", "Archaeology", "History", "Language (Own)", "Language (Other)", "Library Use", "Navigate", "Occult", "Track"],
               "Film Crew": ["Art/Craft (Film)", "Climb", "Disguise", "Drive Auto", "Electrical Repair", "Electronics", "First Aid", "Mechanical Repair", "Photography", "Psychology", "Stealth"],
               "Film Star": ["Reputation", "Art/Craft (Acting)", "Charm", "Disguise", "Fast Talk", "Firearms (Handgun)", "Intimidate", "Jump", "Library Use", "Persuade", "Psychology"],
               "Fireman": ["Climb", "Drive Auto", "Fast Talk", "Fighting (Axe)", "First Aid", "Jump", "Mechanical Repair", "Reputation", "Survival", "Throw", "Track"],
               "Foreign Correspondent": ["Language (Own)", "Accounting", "Charm", "Disguise", "Fast Talk", "History", "Language (Other)", "Persuade", "Psychology", "Reputation", "Stealth"],
               "Forger/Counterfeiter": ["Art/Craft (Forgery)", "Appraise", "Disguise", "Fast Talk", "Firearms (Handgun)", "Intimidate", "Language (Own)", "Language (Other)", "Persuade", "Psychology", "Stealth"],
               "Forester": ["Operate Heavy Machinery", "Animal Handling", "Climb", "Fighting (Axe)", "First Aid", "Jump", "Intimidate", "Listen", "Natural History", "Mechanical Repair", "Survival"], 
               "Forensic Investigator": ["Spot Hidden", "Electronics", "Fast Talk", "Firearms (Handgun)", "First Aid", "Law", "Medicine", "Photography", "Science (Biology)", "Science (Chemistry)", "Track"], 
               "Forensic Surgeon": ["Forensic Surgery", "Accounting", "First Aid", "History", "Library Use", "Listen", "Medicine", "Reputation", "Science (Biology)", "Science (Chemistry)", "Sleight of Hand"], 
               "Gambler": ["Fast Talk", "Accounting", "Charm", "Drive Auto", "Firearms (Handgun)", "Listen", "Occult", "Persuade", "Psychology", "Sleight of Hand", "Spot Hidden"],
               "Gangster": ["Intimidate", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Persuade", "Psychology", "Reputation", "Sleight of Hand", "Track"],
               "Gardener": ["Art/Craft (Gardening)", "Accounting", "Animal Handling", "First Aid", "Library Use", "Listen", "Medicine (Plants)", "Natural World", "Spot Hidden", "Swim", "Science (Botany)"],
               "Golf Pro": ["Art/Craft (Golf)", "Charm", "Fast Talk", "Intimidate", "Occult", "Persuade", "Psychology", "Reputation", "Sleight of Hand", "Spot Hidden", "Track"],
               "Gravedigger": ["Stealth", "Anthropology", "Archaeology", "History", "Intimidate", "Listen", "Locksmith", "Navigate", "Occult", "Spot Hidden", "Track"],
               "Hacker": ["Electronics", "Electrical Repair", "Fast Talk", "Language (Own)", "Language (Other)", "Library Use", "Locksmith", "Mechanical Repair", "Science (Physics)", "Science (Programming)", "Stealth"],
               "Hired Goon": ["Intimidate", "Climb", "Drive Auto", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Jump", "Listen", "Stealth", "Throw", "Track"],
               "Hit Man": ["Track", "Demolitions", "Disguise", "Fast Talk", "Firearms (Handgun)", "Firearms (Shotgun/Rifle)", "First Aid", "Intimidate", "Listen", "Psychology", "Stealth"],
               "Hobo": ["Survival", "Climb", "Fast Talk", "Firearms (Handgun)", "History", "Jump", "Listen", "Natural History", "Persuade", "Stealth", "Spot Hidden"],
               "Hooker": ["Charm", "Disguise", "First Aid", "Fast Talk", "Listen", "Occult", "Persuade", "Psychology", "Sleight of Hand", "Stealth", "Survival"],
               "Journalist": ["Art/Craft (Journalism)", "Charm", "Climb", "Disguise", "Fast Talk", "Language (Own)", "Listen", "Persuade", "Psychology", "Stealth", "Spot Hidden"],
               "Judge": ["Law", "Fast Talk", "History", "Intimidate", "Language (Own)", "Library Use", "Listen", "Occult", "Persuade", "Psychology", "Reputation"],
               "Lawyer": ["Law", "Charm", "Fast Talk", "Firearms (Handgun)", "History", "Intimidate", "Language (Own)", "Library Use", "Persuade", "Psychology", "Reputation"],
               "Librarian": ["Anthropology", "Archaeology", "Library Use", "Accounting", "History", "Intimidate", "Language (Own)", "Language (Other)", "Language (Any)", "Psychology", "Stealth"],
               "Loan Shark": ["Intimidate", "Accounting", "Appraise", "Charm", "Fast Talk", "Firearms (Handgun)", "Law", "Persuade", "Psychology", "Reputation", "Track"],
               "Lumberjack": ["Fighting (Axe)", "Animal Handling", "Climb", "First Aid", "Jump", "Intimidate", "Listen", "Natural History", "Mechanical Repair", "Operate Heavy Machinery", "Survival"],
               "Manager/Coach": ["Coaching", "Accounting", "Charm", "Fast Talk", "First Aid", "History", "Intimidate", "Medicine (Sports)", "Persuade", "Psychology", "Spot Hidden"],
               "Medical Technician": ["Medicine", "Electrical Repair", "First Aid", "Library Use", "Listen", "Mechanical Repair", "Occult", "Photography", "Science (Biology)", "Science (Chemistry)", "Spot Hidden"],
               "Mental Hospital Attendant": ["Psychology", "Accounting", "Charm", "Fast Talk", "First Aid", "History", "Intimidate", "Listen", "Persuade", "Stealth", "Track"],
               "Mercenary": ["Firearms (Rifle/Shotgun)", "Climb", "Firearms (Handgun)", "Jump", "Navigate", "Operate Heavy Machinery", "Pilot (Aircraft)", "Stealth", "Survival", "Swim", "Track"], 
               "Military Officer": ["Reputation", "Climb", "Fast Talk", "Intimiate", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Intimidate", "Navigate", "Persuade", "Psychology"]}


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