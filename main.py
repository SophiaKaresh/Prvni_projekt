"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Sophia Karešová
email: karesovasophia@seznam.cz
"""
#Zadání textu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#část první - ověření uživatele

registrovani_uzivatele = dict(
bob = "123", 
ann = "pass123", 
mike = "password123", 
liz = "pass123")
user = input("username: ")
password = input("password: ")
if user in registrovani_uzivatele and registrovani_uzivatele[user] == password:
    print(
    "----------------------------------------",
    f"Welcome to the app, {user} ",
    "We have 3 texts to be analyzed.",
    "----------------------------------------",
    sep = "\n"
    )
else:
    print("unregistred user, terminating the program...")
    exit()

#část druhá - analýza textu

vyber = input("Enter a number btw. 1 and 3 to select: ")
if vyber.isdigit():
    cislo = int(vyber)
    if 1 <= cislo <= 3:
        vybrany_text = TEXTS[cislo - 1]
        slova = vybrany_text.split()

        word_count = 0
        titlecase = 0
        uppercase = 0
        lowercase = 0
        numeric_strings= 0
        suma = 0

        for slovo in slova:
            word_count += 1
            if slovo.istitle():
                titlecase += 1
            elif slovo.isupper():
                uppercase += 1
            elif slovo.islower():
                lowercase += 1
            elif slovo.isnumeric():
                numeric_strings += 1
                suma += int(slovo)

        print(
        "----------------------------------------",
        f"There are {word_count} words in the selected text.",
        f"There are {titlecase} titlecase words.",
        f"There are {uppercase} uppercase words.",
        f"There are {lowercase} lowercase words.",
        f"There are {numeric_strings} numeric strings.",
        f"The sum of all the numbers {suma}",
        "----------------------------------------",
        "LEN|   OCCURRENCES      |NR.",
        "----------------------------------------",
        sep = "\n"
        )      

        delky_slov = dict()
        for slovo in slova:
            slovo_bez_interpunkce = slovo.strip(".,")
            delka = len(slovo_bez_interpunkce)
            if delka > 0:
                 delky_slov[delka] = delky_slov.get(delka, 0) + 1
        
        for delka in sorted(delky_slov):
            pocet_pismen = delky_slov[delka]
            hvezdicky = "*" * pocet_pismen
            print(f"{delka:>3}| {hvezdicky:<18} | {pocet_pismen:<3}")

    else:
        print("invalid number, terminating the program...")
        exit()
else:
    print("invalid choice, terminating the program...")
    exit()
