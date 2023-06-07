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