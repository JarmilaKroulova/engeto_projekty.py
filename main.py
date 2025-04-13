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

print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jarmila Kroulová
email: jarmilxxx@seznam.cz
""")

registrovani_uzivatele = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123" }

ODDELOVAC = "-" *40 

pocet_textu = len(TEXTS)

uzivatel = input("username: ")
heslo = input("password: ")

if uzivatel in registrovani_uzivatele and heslo == registrovani_uzivatele[uzivatel]:
    print(f'{ODDELOVAC}\n Welcome to the app, {uzivatel}\n We have {pocet_textu} texts to be analyzed.\n{ODDELOVAC}')
else:
    print("Unregistered user, terminating the program..")
    quit()

vyber_textu = int(input(f"Enter a number btw. 1 and {pocet_textu} to select: "))

print(ODDELOVAC)

if vyber_textu == 1:
    text = TEXTS[0]
elif vyber_textu == 2:
    text = TEXTS[1]
elif vyber_textu == 3:
    text = TEXTS[2]
else:
    print("Select number is not in the offer.")


ciste_slovo = list()

for slovo in text.split():
    jen_slovo = slovo.strip(",.:?!")
    ciste_slovo.append(jen_slovo)

pocet_slov = len(ciste_slovo)

titlecase = []
    
for slovo in ciste_slovo: 
    if slovo.istitle():
        zacina_velkym = slovo
        titlecase.append(zacina_velkym)

zacinajici_velkym = len(titlecase)

uppercase = []
    
for slovo in ciste_slovo: 
    if slovo.isupper():
        je_velkym = slovo
        uppercase.append(je_velkym)

je_velke = len(uppercase)

lowercase = []
    
for slovo in ciste_slovo: 
    if slovo.islower():
        je_malym = slovo
        lowercase.append(je_malym)

je_male = len(lowercase)

cisla = []
    
for cifra in ciste_slovo: 
    if cifra.isnumeric():
        je_cislem = cifra
        cisla.append(je_cislem)

je_cislo = len(cisla)

realna_cisla = []

for cislo in cisla:
    je_realne = cislo
    realna_cisla.append(int(je_realne))

soucet = sum(realna_cisla)

delka_slov = [len(slovo) for slovo in ciste_slovo]

slovo_1 = delka_slov.count(1)
slovo_2 = delka_slov.count(2)
slovo_3 = delka_slov.count(3)
slovo_4 = delka_slov.count(4)
slovo_5 = delka_slov.count(5)
slovo_6 = delka_slov.count(6)
slovo_7 = delka_slov.count(7)
slovo_8 = delka_slov.count(8)
slovo_9 = delka_slov.count(9)
slovo_10 = delka_slov.count(10)
slovo_11 = delka_slov.count(11)
slovo_12 = delka_slov.count(12)
slovo_13 = delka_slov.count(13)


slovnik_delky = {
    "1" : slovo_1,
    "2" : slovo_2,
    "3" : slovo_3,
    "4" : slovo_4,
    "5" : slovo_5,
    "6" : slovo_6,
    "7" : slovo_7,
    "8" : slovo_8,
    "9" : slovo_9,
    "10" : slovo_10,
    "11" : slovo_11,
    "12" : slovo_12,
    "13" : slovo_13    
}

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {zacinajici_velkym} titlecase words.")
print(f"There are {je_velke} uppercase words.")
print(f"There are {je_male} lowercase words.")
print(f"There are {je_cislo} numeric strings.")
print(f"The sum of all the numbers {soucet}.")

print(f"{ODDELOVAC}\nLEN|  OCCURENCES          |NR\n{ODDELOVAC}")

for radek in slovnik_delky.items():
    delka, vyskyt = radek
    if vyskyt == 0:
            continue
    else:
        print(f"{delka:<2} | {'*' * int(vyskyt):<30} | {vyskyt}")
