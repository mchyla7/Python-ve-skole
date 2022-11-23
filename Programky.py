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
#cisla0()



# Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# po zadání a se program ukončí
# a vypíše všechny čísla
# + 
# jejich průměr


def cisla0():
    cislavse = ""
    pocet = 0
    prumer = 0
    while(True):
        cislo = input("Zadejte číslo: ")
        cislavse+=  cislo + "; " 
        prumer+= float(cislo)
        pocet += 1
        otazka = input("Chcete skončit? a - pro skončení   ")
        if (otazka.lower() == "a"): break # /neco/.lower() ----- převede text na malé písmena
        prumer+= cislo
        pocet + 1
    print(cislavse)
    print("Průměr je: ", prumer/pocet)
#cisla0()



# # Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# po zadání "a" se program ukončí
# a vypíše všechny čísla
# + 
# jejich průměr
# a čtvrté číslo je na novém řádku

def nacitDotaz2():
    tisk=""; soucet=0; pocet =0; pocetnovyradek=0
    while(True):
        cislo= input("Zadej číslo: ")
        tisk = tisk +  cislo +"; "
        pocetnovyradek+=1
        if pocetnovyradek == 3:
            tisk = tisk + "\n"
            pocetnovyradek = 0
        soucet+=float(cislo)
        pocet+=1  # pocet = pocet +1  
        volba = input ("Chcete skončit? a - pro skončení   ")
        if (volba.lower() =="a"): break
    print(tisk)
    print("průměr:", soucet/pocet)
#nacitDotaz2()



# Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# po zadání "a" se program ukončí
# po zadání "a" se zobrazí volba:
# 1. výpis
# 2. průměr
# 3. maximální a minimalní hodnotu
# 4. počet záporných čísel
# 5. konec

def nacitamcislaskalkulackou():
    tisk = ""
    otazka = ""
    soucet = 0
    pocet = 0 
    pocetzapornych = 0
    nejvetsi = -999999
    nejmensi = 9999999
    while(otazka.lower() != "a"):
        cislo = float(input("Zadejte číslo: "))
        tisk += str(cislo) + "; "
        soucet += (cislo)
        pocet += 1
        if(cislo > nejvetsi):
            nejvetsi = cislo
        if(cislo < nejmensi):
            nejmensi = cislo
        if(cislo < 0):
            pocetzapornych+= 1
        otazka = input("Chcete zobrazit nabídku? (a) - ")
    while(True):    
        volby = input("1. Výpis, 2. Průměr, 3.Maximální a minimální hodnotu, 4. Počet záporných čísel a 5. Vypne program : ")
        if volby == "1":
            print(tisk)
        elif volby == "2":
            print("Průměr je: ", soucet/pocet)
        elif volby == "3":
            print(f"Nejmenší číslo: {nejmensi} a Největší je: {nejvetsi}")
        elif volby == "4":
            print("Počet záporných hodnot: ", pocetzapornych)
        else:
            break
nacitamcislaskalkulackou()



