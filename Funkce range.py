# Program zobrazí čísla od 1 do 10

# funkce range(hodnota) - vygeneruje rozsah hodnot
# funkce range(10) - vygeneruje rozsah čísel od 1ky do 10ky
# funkce range(-10,10) - vygeneruje rozsah celých čísel od -10ky do 9ky

def program():
    for i in range(10):
        print(i)
#program()



def perla():
    for i in "ahoj":
        print(i)
#perla()


# Program vygeneruje n čísel od -10 do 10

import random # Přidání knihovny na radnomizaci

def nahodnecisla():
    pocet = int(input("Kolik čísel se má vygenerovat: "))
    for i in range(pocet):
        print(random.randint(-10,10))  # Vygeneruje číslo v daném intervalu
#nahodnecisla()



def nahodnec():
    pocet = int(input("Kolik čísel se má vygenerovat: "))
    for i in range(pocet):
        print(random.randint(-10,10), end="; ")  # Vygeneruje číslo v daném intervalu a bude mezi nimi mezera
#nahodnec()

# Program vygeneruje pouze sudá čísla

def sude():
    sude = 1
    for i in range(2, 101):
        if sude == 1:
            print(i)
        sude = sude * -1 
#sude()

# Program vygeneruje sudá čísla
# a mezitím bude kontrolovat jestli máme sudé(pravdu) nebo sude(nepravdu)


def suda1():
    sude = True
    for i in range(2, 101):
        if sude == 1:
            print(i)
        sude = not True
suda1()