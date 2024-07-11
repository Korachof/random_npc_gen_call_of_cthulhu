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
               "Military Officer": ["Reputation", "Climb", "Fast Talk", "Intimiate", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Intimidate", "Navigate", "Persuade", "Psychology"],
               "Miner": ["Operate Heavy Machinery", "Appraise", "Climb", "First Aid", "Intimidate", "Jump", "Listen", "Natural World", "Science (Chemistry)", "Science (Geology)", "Spot Hidden"], 
               "Missionary": ["Fast Talk", "Anthropology", "Charm", "Drive Auto", "Language (Own)", "Language (Other)", "Library Use", "Occult", "Persuade", "Psychology", "Track"], 
               "Mountain Climber": ["Climb", "First Aid", "Jump", "Listen", "Natural World", "Navigate", "Photography", "Science (Geology)", "Throw", "Track", "Spot Hidden"], 
               "Museum Curator": ["History", "Accounting", "Appraise", "Fast Talk", "Language (Own)", "Language (Other)", "Law", "Library Use", "Occult", "Persuade", "Reputation"],
               "Musician": ["Art/Craft (Instrument)", "Accounting", "Charm", "Disguise", "Fast Talk", "Listen", "Persuade", "Psychology",  "Read Lips", "Reputation", "Sleight of Hand"], 
               "News Chopper Pilot": ["Pilot (Helicopter)", "Climb", "Drive Auto", "First Aid", "Jump", "Language (Own)", "Listen", "Mechanical Repair", "Persuade", "Science (Meteorology)", "Spot Hidden"], 
               "Nurse": ["First Aid", "Charm", "Fast Talk", "Intimidate", "Library Use", "Medicine", "Persuade", "Psychology", "Reputation", "Science (Biology)", "Stealth"], 
               "Occultist": ["Occult", "Anthropology", "Cthulhu Mythos", "Firearms (Handgun)", "History", "Intimidate", "Language (Own)", "Language (Other)", "Library Use", "Stealth", "Survival"],
               "Painter/Sculptor": ["Art/Craft (Specialization)", "Appraise", "History", "Language (Other)", "Library Use", "Natural World", "Occult", "Persuade", "Photography", "Psychology", "Sleight of Hand"], 
               "Parapsychologist": ["Psychoanalysis", "Anthropology", "Fast Talk", "First Aid", "Hypnosis", "Library Use", "Medicine", "Occult", "Persuade", "Photography", "Psychology"], 
               "Pharmacist": ["Medicine", "Accounting", "First Aid", "Language (Own)", "Language (Other)", "Library Use", "Persuade", "Psychology", "Reputation", "Science (Biology)", "Science (Chemistry)"],
               "Photographer": ["Photography", "Accounting", "History", "Listen", "Natural World", "Persuade", "Psychology", "Read Lips", "Science (Chemistry)", "Science (Physics)", "Spot Hidden"],
               "Photojournalist": ["Photography", "Charm", "Climb", "Fast Talk", "Jump", "Langauge (Other)", "Persuade", "Psychology", "Spot Hidden", "Survival", "Track"],
               "Physician": ["Medicine", "Charm", "First Aid", "Library Use", "Medicine", "Persuade", "Psychoanalysis", "Psychology", "Reputation", "Science (Biology)", "Science (Chemistry)"],
               "Pick Pocket": ["Sleight of Hand", "Charm", "Disguise", "Fast Talk", "Firearms (Handgun)", "Listen", "Locksmith", "Psychology", "Spot Hidden", "Stealth", "Track"],
               "Pilot": ["Pilot (Specialization)", "Charm", "Electrical Repair", "Electronics", "Firearms (Handgun)", "Mechanical Repair", "Navigate", "Operate Heavy Machinery", "Science (Astronomy)", "Science (Physics)", "Survival"],
               "Plastic Surgeon": ["Medicine", "Accounting", "First Aid", "Language (Other)", "Library USe", "Persuade", "Psychology", "Reputation", "Science (Biology)", "Science (Chemistry)", "Sleight of Hand"],
               "Police Detective": ["Track", "Disguise", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "Law", "Listen", "Persuade", "Psychology", "Spot Hidden"],
               "Policeman": ["Law", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "Intimidate", "Listen", "Occult", "Persuade", "Psychology", "Track"],
               "Practising Attorney": ["Law", "Accounting", "Fast Talk", "Intimidate", "Language (Own)", "Language (Other)", "Law", "'Library Use", "Persuade", "Psychology", "Reputation"],
               "Preacher": ["Accounting", "Fast Talk", "History", "Intimidate", "Language (Own)", "Library Use", "Occult", "Persuade", "Psychology", "Reputation", "Stealth"],
               "Private Investigator": ["Track", "Climb", "Disguise", "Drive Auto", "Fast Talk", "Jump", "Law", "Library Use", "Persuade", "Photography", "Stealth"], 
               "Professional Athlete": ["Art/Craft (Sport)", "Charm", "Disguise", "Fast Talk", "First Aid", "Jump", "Listen", "Psychology", "Spot Hidden", "Throw", "Swim"], 
               "Professor/Teacher": ["Persuade", "Charm", "Fast Talk", "History", "Intimidate", "Language (Own)", "Language (Other)", "Library Use", "Natural World", "Reputation", "Science (Any)"],
               "Programmer": ["Electronics", "Accounting", "Electrical Repair", "Fast Talk", "First Aid", "Library Use", "Language (Other)", "Mechanical Repair", "Occult", "Sleight of Hand", "Spot Hidden"], 
               "Prosecuting Attorney": ["Persuade", "Fast Talk", "History", "Intimidate", "Language (Own)", "Language (Other)", "Law", "Library Use", "Occult", "Psychology", "Reputation"], 
               "Protestant Minister": ["Persuade", "Accounting", "Fast Talk", "Firearms (Handgun)", "Intimidate", "History", "Language (Own)", "Library Use", "Occult", "Psychology", "Reputation"], 
               "Psychologist": ["Psychology", "Accounting", "Charm", "Fast Talk", "Intimidate", "First Aid", "Library Use", "Medicine", "Persuade", "Psychoanalysis", "Science (Chemistry)"],
               "Punk": ["Intimidate", "Fast Talk", "Firearms (Handgun)", "Listen", "Occult", "Persuade", "Psychology", "Spot Hidden", "Survival", "Throw", "Track"],
               "Rabbi": ["Language (Hebrew)", "Fast Talk", "History", "Intimidate", "Language (English)", "Language (Other)", "Library Use", "Occult", "Persuade", "Psychology", "Reputation"],
               "Racecar Driver": ["Drive Auto", "Charm", "Fast Talk", "First Aid", "Electrical Repair", "History", "Listen", "Mechanical Repair", "Pilot (Boat)", "Psychology", "Spot Hidden"],
               "Ranch Hand/Cowboy": ["Natural World", "Accounting", "Drive Auto", "Firearms (Rifle/Shotgun)", "First Aid", "Jump", "Listen", "Medicine (Veterinary)", "Operate Heavy Machinery", "Reputation", "Ride"],
               "Reporter": ["Fast Talk", "Charm", "Climb", "Disguise", "Jump", "Listen", "Persuade", "Psychology",  "Reputation", "Stealth", "Spot Hidden"],
               "Researcher": ["Library Use", "Anthropology", "Archaeology", "History", "Language (Own)", "Language (Other)", "Occult", "Psychology", "Reputation", "Science (Any)", "Spot Hidden"],
               "Sailor": ["Climb", "Artillery", "Electrical Repair", "Firearms (Handgun)", "Firearms (Rifle/Shotgun", "First Aid", "Jump", "Mechanical Repair", "Navigate", "Operate Heavy Machinery", "Swim"],
               "Salesman": ["Fast Talk", "Accounting", "Appraise", "Charm", "Drive Auto", "Firearms (Handgun)", "Language (Own)", "Occult", "Persuade", "Psychology", "Reputation"],
               "Secretary": ["Accounting", "Charm", "Drive Auto", "Fast Talk", "First Aid", "Language (Own)", "Language (Other)", "Library Use", "Persuade", "Psychology", "Spot Hidden"],
               "Shifty Accountant/Lawyer": ["Fast Talk", "Accounting", "Charm", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Law", "Occult", "Persuade", "Psychology", "Reputation"],
               "Small Business Owner": ["Accounting", "Animal Handling", "Charm", "Fast Talk", "Electrical Repair", "Fast Talk", "Listen", "Mechanical Repair", "Persuade", "Psychology", "Reputation"],
               "Smuggler": ["Stealth", "Charm", "Fast Talk", "Firearms (Handgun)", "Language (Other)", "Listen", "Navigate", "Persuade", "Pilot (Aircraft/Boat)", "Psychology", "Spot Hidden"],
               "Soldier/Marine": ["Firearms (Rifle/Shotgun)", "Artillery", "Drive Auto", "Electrical Repair", "Firearms (Handgun)", "First Aid", "Mechanical Repair", "Medicine", "Operate Heavy Machinery", "Spot Hidden", "Survival"],
               "Spy": ["Stealth", "Charm", "Demolitions", "Disguise", "Fast Talk", "Firearms (Handgun)", "Listen", "Language (Other)", "Persuade", "Psychology", "Spot Hidden"], 
               "Stage Actor": ["Art/Craft (Acting)", "Charm", "Disguise", "Fast Talk", "History", "Language (Own)", "Language (Other)", "Library Use", "Listen", "Persuade", "Psychology"], 
               "Stage Hand": ["Art/Craft (Theater)", "Art/Craft (Acting)", "Charm", "Disguise", "Fast Talk", "Electrical Repair", "Mechanical Repair", "Persuade", "Psychology", "Sleight of Hand", "Stealth"],
               "Stock Broker": ["Appraise", "Accounting", "Electronics", "Fast Talk", "History", "Language (Own)", "Library Use", "Occult", "Persuade", "Psychology", "Reputation"], 
               "Student/Intern": ["Library Use", "Accounting", "Anthropology", "Charm", "Fast Talk", "History", "Language (Own)", "Language (Other)", "Listen", "Psychology", "Science (Any)"], 
               "Stunt Man": ["Disguise", "Climb", "Drive Auto", "Elecrical Repair", "First Aid", "Jump", "Mechanical Repair", "Pilot (Aircraft/Boat)", "Ride", "Swim", "Throw"], 
               "Surveyor": ["Natural World", "Accounting", "First Aid", "History", "Law", "Library Use", "Listen", "Navigate", "Spot Hidden", "Survival", "Track"],
               "Swimmer/Diver": ["Swim", "Appraise", "Demolitions", "Electrical Repair", "Firearms (Rifle/Shotgun)", "Mechanical Repair", "Navigate", "Persuade", "Pilot (Boat)", "Spot Hidden", "Track"],
               "Talent Agent": ["Psychology", "Accounting", "Appraise", "Charm", "Fast Talk", "Law", "Listen", "Persuade", "Psychology", "Reputation", "Spot Hidden"],
               "Taxi Driver": ["Drive Auto", "Accounting", "Electrical Repair", "Fast Talk", "Firearms (Handgun)", "History", "Language (Own)", "Mechanical Repair", "Navigate", "Persuade", "Psychology"],
               "Telephone Operator": ["Listen", "Accounting", "Charm", "Electrical Repair", "Fast Talk", "Language (Own)", "Language (Other)", "Library Use", "Occult", "Persuade", "Psychology"],
               "Tennis Pro": ["Art/Craft (Tennis)", "Charm", "Disguise", "Fast Talk", "Intimidate", "Jump", "Occult", "Persuade", "Psychology", "Reputation", "Spot Hidden"],
               "Tribal Member": ["Natural World", "First Aid", "Language (Own)", "Language (Other)", "Listen", "Medicine", "Occult", "Spot Hidden", "Swim", "Throw", "Track"],
               "Undertaker": ["Science (Biology)", "Accounting", "Fast Talk", "'First Aid", "History", "Intimidate", "Library Use", "Persuade", "Psychology", "Reputation", "Stealth"],
               "Uniformed Police Officer": ["Law", "Drive Auto", "Fast Talk", "Firearms (Handgun)", "Firearms (Rifle/Shotgun)", "First Aid", "Intimidate", "Occult", "Persuade", "Psychology", "Track"],
               "Union Activist": ["Psychology", "Accounting", "Fast Talk", "Firearms (Handgun)", "Language (Own)", "Language (Other)", "Law", "Mechanical Repair", "Operate Heavy Machinery", "Persuade", "Psychology"],
               "Writer": ["Art/Craft (Writing)", "Charm", "Fast Talk", "History", "Language (Own)", "Language (Other)", "Listen", "Natural World", "Occult", "Persuade", "Psychology"],
               "Wrestler": ["Fighting (Grapple)", "Charm", "Disguise", "Fast Talk", "First Aid", "History", "Intimidate", "Listen", "Sleight of Hand", "Spot Hidden", "Throw"],
               "Zookeeper": ["Animal Handling", "Accounting", "First Aid", "Charm", "Firearms (Rifle/Shotgun)", "Library Use", "Natural World", "Medicine (Veterinary)", "Psychology", "Science (Biology)", "Survival"]}


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