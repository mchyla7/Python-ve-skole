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
    a = 0
    tisk = ""
    while(True):
        try: a = float(input("Zadejte číslo: "))
        except: break
        if a <- 100 or cislo > 100 :break
        tisk+= str(a) + ", "
    print(tisk)
cykluskonci()
