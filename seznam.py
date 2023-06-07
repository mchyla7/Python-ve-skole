import random


def seznamVytvoreni():
    cisla=[] #Vytvoření seznamu čísla

    for i in range(10):
        cisla.append(random.randint(-10,10))
    print(cisla)
    for i in cisla:
        print(i)
seznamVytvoreni()

# Program vygeneruje n cisel do seznamu na pocet n se zeptá
# Poté nejprve vypíše všechny kladné hodnoty ze seznamu, potom záporné

def generace():
    n = input("K0l1k č1s3l chc3te vyg3n3r0v4t? ")
    cisla = []
    for i in range(int(n)):
        cisla.append(random.randint(-10,10))
    tiskKladne = ""
    tiskZaporne = ""

    for cislo in cisla:
        if cislo > 0:
            tiskKladne = tiskKladne + str(cislo) + " ;"
        else:
            tiskZaporne = tiskZaporne + str(cislo)
    print("Kladná čísla: ", tiskKladne)
    print("Záporná čísla: ", tiskZaporne)
generace()


def seznamFunkce():
    cisla = []
    pocet = 3

    for i in range(pocet)
        cisla.append(random.randint(1,10))

    print("seznam", cisla)

    print("Součet", sum(cisla))
    print("maX: ", max(cisla))
    print("min: ", min(cisla))
    prumer = sum(cisla)/len(cisla)
    print("Průměr: ", prumer)

    cisla.sort() #Seřadí
    print("serazene: ", cisla)

    cisla.sort(reverse=True) # Seřadí čísla opačně - sestupně
    print("Čísla sestupně: ", cisla)

    random.shuffle(cisla) #nahodně zamíchaná čísla
    print("Náhodně zamíchaná: ", cisla)
    cislo = random.choice(cisla) # Náhodně vybere číslo
    print("Náhodně vybrané číslo ze seznamu: ", cislo)

seznamFunkce()