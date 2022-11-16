# Program se zeptá na počet čísel
# Poté se počet těchto čísel načte
# Program zobrazí součet těchto čísel

def zeptanicisel():
    soucet = 0
    pocet = 0
    pocetcisel = float(input("Zadejte počet čísel: "))
    while(pocet != pocetcisel):
        pocet += 1
        cislo = float(input("Zadej číslo"))
        soucet += cislo
    print(soucet)
#zeptanicisel()


# Program načítá čísla
# Po načtení nečíselné hodnoty se načítání ukončí
# Nasledně vypíše všechny číselné hodnoty

def cyklusnekonci():
    a = 0
    tisk = ""
    while(True):
        try:a = float(input("Zadejte číslo: "))
        except: break
        tisk+= str(a) + ", "
    print(tisk)
#cyklusnekonci()



# Program načítá čísla
# Po načtení nečíselné hodnoty se načítání ukončí
# nebo se ukončí když je číslo menší než mínus 100 nebo plus 100
# Nasledně vypíše všechny číselné hodnoty

def cykluskonci():
    a = 0 # Daná promněnná, do které se ukládají daná čísla
    maxc = -999999 # Maximalní číslo (Musí být malé aby jsi mohl určit které je větší)
    tisk = "" # Just tisk idk
    minc = 99999 # Minimalní číslo (Musí být velké aby jsi mohl určit které je menší)
    while(True):
        try: a = float(input("Zadejte číslo: "))
        except: break
        if a <- 100 or a > 100 :break # Pokud bude číslo menší než -100 a nebo větší než 100, tak se vypni a pokračuj na 47
        tisk+= str(a) + ", " 
        if(a > maxc):
            maxc = a
        if(a < minc):
            minc = a
    print(tisk)
    print("Maximum: ",maxc)
    print("Minimum: ",minc)
# cykluskonci()


# Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# po zadání a se program ukončí
# a vypíše všechny čísla


def cisla0():
    cislavse = ""
    while(True):
        cislo = input("Zadejte číslo: ")
        cislavse+=  cislo + "; " 
        otazka = input("Chcete skončit? a - pro skončení   ")
        if (otazka.lower() == "a"): break # *neco*.love() ----- převede text na malé písmena
    print(cislavse)
cisla0()



# Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# po zadání a se program ukončí
# a vypíše všechny čísla
# + 
# ! jejich průměrnou hodnotu Nefunguje
#


def cisla0():
    cislavse = ""
    pocet = 0
    prumer = 0
    while(True):
        cislo = input("Zadejte číslo: ")
        cislavse+=  cislo + "; " 
        soucet+= float(cislo)
        pocet += 1
        otazka = input("Chcete skončit? a - pro skončení   ")
        if (otazka.lower() == "a"): break # *neco*.love() ----- převede text na malé písmena
        soucet += cislo
        pocet + 1
    print(cislavse)
    print("Průměr je: ", soucet/pocet)
cisla0()