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

#uložené údaje
users = {"bob":"123",
         "ann":"pass123",
         "mike":"password123",
         "liz":"pass123"
         }
print("-" * 12)

##zadání uživatelských údajů
zadane_jmeno = input("Please enter your username: ")
zadane_heslo = input("Please enter your password: ")

print("-" * 12)

###podmínky pokud nejsou správné uživatelské údaje

if zadane_jmeno in users and users[zadane_jmeno] == zadane_heslo:
    print("Welcome to the app," + zadane_jmeno + "\nWe have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program...")
    exit()

print("-" * 12)

####vybrání čísla + analýza
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

print("-" * 12)

try:
    cislo = int(vyber_textu)
except ValueError:
    print("It's not a number, terminating program...")
    exit()

if not 1<= cislo <=3:
    print("It's not a number between 1-3, terminating program... ")
    exit()

##### vypsání možností

pocet_slov1 = len(TEXTS[0].split())
pocet_slov2 = len(TEXTS[1].split())
pocet_slov3 = len(TEXTS[2].split())




velka_pismena1 = 0
for slovo in TEXTS[0].split():
    for znak in slovo:
        if znak.istitle() and not slovo.isupper():
            velka_pismena1 +=1
            break

velka_pismena2 = 0
for slovo in TEXTS[1].split():
    for znak in slovo:
        if znak.istitle() and not slovo.isupper():
            velka_pismena2 +=1
            break

velka_pismena3 = 0
for slovo in TEXTS[2].split():
    for znak in slovo:
        if znak.istitle() and not slovo.isupper():
            velka_pismena3 +=1
            break




slova_velkymi1 = 0
for slovo in TEXTS[0].split():
    if slovo.isupper():
        slova_velkymi1 += 1

slova_velkymi2 = 0
for slovo in TEXTS[1].split():
    if slovo.isupper():
        slova_velkymi2 += 1

slova_velkymi3 = 0
for slovo in TEXTS[2].split():
    if slovo.isupper():
        slova_velkymi3 += 1




slova_malymi1 = 0
for slovo in TEXTS[0].split():
    if slovo.islower():
        slova_malymi1 += 1

slova_malymi2 = 0
for slovo in TEXTS[1].split():
    if slovo.islower():
        slova_malymi2 += 1

slova_malymi3 = 0
for slovo in TEXTS[2].split():
    if slovo.islower():
        slova_malymi3 += 1




pocet_cisel1 = 0
for cislo in TEXTS[0].split():
    if cislo.isnumeric():
        pocet_cisel1 += 1

pocet_cisel2 = 0
for cislo in TEXTS[1].split():
    if cislo.isnumeric():
        pocet_cisel2 += 1

pocet_cisel3 = 0
for cislo in TEXTS[2].split():
    if cislo.isnumeric():
        pocet_cisel3 += 1




slova_1 = TEXTS[0].split()
cislo_1 = [int(slovo) for slovo in slova_1 if slovo.isdigit()]
suma_cisel1 = sum(cislo_1)

slova_2 = TEXTS[1].split()
cislo_2 = [int(slovo) for slovo in slova_2 if slovo.isdigit()]
suma_cisel2 = sum(cislo_2)

slova_3 = TEXTS[2].split()
cislo_3 = [int(slovo) for slovo in slova_3 if slovo.isdigit()]
suma_cisel3 = sum(cislo_3)



######tisk odpovědí
if int(vyber_textu) == 1:
    print(f"There are {pocet_slov1} words in the selected text.")
    print(f"There are {velka_pismena1} tittlecase words.")
    print(f"There are {slova_velkymi1} uppercase words.")
    print (f"There are {slova_malymi1} lowercase words.")
    print(f"There are {pocet_cisel1} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel1}")


elif int(vyber_textu) == 2:
    print(f"There are {pocet_slov2} words in the selected text.")
    print(f"There are {velka_pismena2} tittlecase words.")
    print(f"There are {slova_velkymi2} uppercase words.")
    print (f"There are {slova_malymi2} lowercase words.")
    print(f"There are {pocet_cisel2} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel2}")

elif int(vyber_textu) == 3:
    print(f"There are {pocet_slov3} words in the selected text.")
    print(f"There are {velka_pismena3} tittlecase words.")
    print(f"There are {slova_velkymi3} uppercase words.")
    print (f"There are {slova_malymi3} lowercase words.")
    print(f"There are {pocet_cisel3} numeric strings.")
    print(f"The sum of all the numbers {suma_cisel3}")

print("-" * 12)

#######grafické znázornění

print("LEN|  OCURRENCES |NR.")

print("-" * 12)

delky_slov1 = {}
delky_slov2 = {}
delky_slov3 = {}


for slovo in slova_1:
    delka_1 = len(slovo)
    if delka_1 not in delky_slov1:
        delky_slov1[delka_1] = 0
    delky_slov1[delka_1] += 1


for delka_1, pocet in sorted(delky_slov1.items()):
    graf_1 = (f"{delka_1} | {"*" * pocet} | {pocet}")
    if int(vyber_textu) == 1:
        print(graf_1)


for slovo in slova_2:
    delka_2 = len(slovo)
    if delka_2 not in delky_slov2:
        delky_slov2[delka_2] = 0
    delky_slov2[delka_2] += 1


for delka_2, pocet in sorted(delky_slov2.items()):
    graf_2  = (f"{delka_2} | {"*" * pocet} | {pocet}")
    if int(vyber_textu) == 2:
        print(graf_2)



for slovo in slova_3:
    delka_3 = len(slovo)
    if delka_3 not in delky_slov3:
        delky_slov3[delka_3] = 0
    delky_slov3[delka_3] += 1


for delka_3, pocet in sorted(delky_slov3.items()):
    graf_3 = (f"{delka_3} | {"*" * pocet} | {pocet}")
    if int(vyber_textu) == 3:
        print(graf_3)



#konec projektu
