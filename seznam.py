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

    for i in range(pocet):
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

# Vytvořte program, který budre vytvářet slova
# Načítání se ukončí, pokud vložíte prázdný řetězec
# Program slova abecedně seřadí a pod sebe vypíše

def pridavejslova():
    list = []
    while(True):
        slova = input("Zadej slova: ")
        if slova == "":
            break
        list.append(slova)
    list.sort()
    for slova in list:
        print(list)
pridavejslova()

# Do předchozího programu přidejte výpis nejdelších slov

def pridavejSlova2():
    list = []
    while(True):
        slova = input("Zadej slova: ")
        if slova == "":
            break
        list.append(slova)
    list.sort()
    for slova in list:
        print(list)
    print("Nejdelší slovo: ")
    maxH = len(max(list))
    for slova in list:
        if len(slova) == max:
            print(list)
pridavejSlova2()

# Program vygeneruje n čísel a uloží jej do seznamu
# Dále vygeneruje nabídku
# 1. Výpis seřazený vzestupně
# 2. Výůpis min a max
# 3. Konec

def generejsn():
    seznam = []
    pocet = int(input("Počet hodnot: "))

    for i in range(pocet):
        seznam.append(random.randint(-50,50))
    seznam.sort()
    while(True):
        volba = input("1. Seřazený výpis, 2. Max a Min, 3. Konec : ")
        if volba == "1":
            for cislo in seznam:
                print(cislo)
        elif volba == "2":
            print("Max: ", max(seznam), "Min: ", min(seznam))
        elif volba == "3":
            print("Konec programu 👋")
            break
generejsn()

# Udělat z toho podprogramy

def nacitaniCisel(seznam):
    pocet = int(input("Počet hodnot: "))

    for i in range(pocet):
        seznam.append(random.randint(-50,50))
    seznam.sort()
    return(seznam)

def serazenyvypis(seznam):
    for cislo in seznam:
        return(cislo)

def maxAndMin(seznam):
    return("Max: ", max(seznam), "Min: ", min(seznam))

def hlavniProgram():
    seznam = []
    seznam = nacitaniCisel(seznam)
    while(True):
        volba = input("1. Seřazený výpis, 2. Max a Min, 3. Konec : ")
        if volba == "1":
            serazenyvypis(seznam)
        elif volba == "2":
            maxAndMin(seznam)
        elif volba == "3":
            print("Konec programu 👋")
            break
hlavniProgram()
