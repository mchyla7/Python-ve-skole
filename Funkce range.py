# Program zobrazí čísla od 1 do 10

# funkce range(hodnota) - vygeneruje rozsah hodnot
# funkce range(10) - vygeneruje rozsah čísel od 1ky do 10ky
# funkce range(-10,10) - vygeneruje rozsah celých čísel od -10ky do 9ky

def bang():
    for i in range(10):
        print(i)
#bang()



def perla():
    for i in "ahoj":
        print(i)
#perla()


# Program vygeneruje n čísel od -10 do 10

import random  # Přidání knihovny na radnomizaci


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
        if sude == True:
            print(i)
        sude = not True
#suda1()


# Program vygeneruje sudá čísla potom lichá

def sudaalicha():
    for i in range(2, 101):
        print(i)
    for il in range(1, 101):
        print(il)
#sudaalicha()

#Ucitel

def suda2():
    tisks=""
    tiskl=""
    sude = True
    for i in range(2, 101):
        if sude == True:
            tisks+= str(i) + " ;"
#suda1()

# Operator vrací zbytek po celočíselném dělení

def testsude():
    cislo = float(input("Zadejte číslo: "))
    if cislo % 2 == 0:
        print("sude")
    else:
        print("Liché")
#testsude()




# Program který vygeneruje náhodných 10 sudých čísel      
#* Učitel

def testsudecisla():
    pocet = 10
    i = 0
    while(i < pocet):
        cislo = random.randint(1, 1000)
        if cislo % 2 == 0:
            print(cislo)
        i += 1
#testsudecisla()

# Program se zeptá na počet čísel nasledně je načte
# Pote zobrazí jejich průměr a vypíše je
# Použít cyklus for


def progra():
    soucet = 0
    tisk = ""
    pocet = int(input("Zadejte počet čísel: "))
    for i in range(pocet):
        cislo = input("Zadejte číslo: ")
        tisk += cislo + "; "
        soucet += float(cislo)
    print(f"Průměr je {round(soucet/pocet)}")    # Funkce round zaokrouhlí čísla na dvě desetiná místa
    print(tisk)
#progra()


# Program se zeptá na počet čísel nasledně je načte
# Pote zobrazí jejich průměr a vypíše je
# Použít cyklus for
# Pokud to nebude číslo tak se znova se opakuje


def prog():
    soucet = 0
    tisk = ""
    cislo = 0
    while(True):
        try:
            pocet = int(input("Zadejte počet čísel: "))
            break
        except:
            print("Zadal jsi nečíselnou hodnotu")
        
    for i in range(int(pocet)):
                try:
                    cislo = float(input("Zadejte číslo: "))
                except:
                    print("Zadal jsi nečíselnou hodnotu")
                    return
                tisk += str(cislo) + "; "  
                soucet += cislo
    print(f"Průměr je {round(soucet/pocet)}")    # Funkce round zaokrouhlí čísla na dvě desetiná místa
    print(tisk)
#prog()




# Program se zeptá na počet čísel nasledně je načte
# Pote zobrazí jejich průměr a vypíše je
# Použít cyklus for
# Pokud to nebude číslo tak se znova se opakuje
# Program následně zobrazí největší a nejmenší číslo



def program():
    soucet = 0
    mincislo =  99999
    maxcislo = -99999
    cislo = 0
    while(True):
        try:
            pocet = int(input("Zadejte počet čísel: "))
            break
        except:
            print("Zadal jsi nečíselnou hodnotu")

    tisk = ""
    soucet = 0    
    for i in range(int(pocet)):
        while(True):
                try:
                    cislo = float(input("Zadejte číslo: "))
                    break
                except:
                    print("Zadal jsi nečíselnou hodnotu")
        tisk = tisk + str(cislo) + "; "  
        soucet += cislo
        if (cislo > maxcislo): 
             maxcislo = cislo   
        if (cislo < mincislo): 
           mincislo = cislo   

    print(f"Průměr je {round(soucet/pocet)}")    # Funkce round zaokrouhlí čísla na dvě desetiná místa
    print(tisk)
    print(f"Největší číslo je {maxcislo} a nejmenší číslo je {mincislo}")
#program()




#Program se zepta na počet znaků, následně je načte.
#Ošetřete, aby byl vždy zadaný pouze jeden znak.
#len("aaa")   3
#Poté je vypíše .

def pr10():
    pocet = int(input("Zadej pocet znaků: "))
    tisk=""
    for i in range(pocet):
        while (True):
            znak = input("Zadej znak: ")
            if(len(znak)==1): break
            print("Nezadal jsi jeden znak!")
        tisk += znak
    print (tisk)
#pr10()


# Program se zeptá na počet čísel, následně je vygeneruje
# Poté zobrazí čísla na řádku oddělená " ;" 
# Použíjte cyklus for
# Následně zobrazí počet kladných čísel a počet záporných čísel

def opa():
    tisk = ""
    pocet = int(input("Zadejte počet čísel: "))
    pocetzapornych = 0
    pocetkladnych = 0
    pocetnul = 0
    for i in range(pocet):
        cislo = random.randint(-100, 100)
        tisk += str(cislo) + "; "
        if(cislo > 0): 
            pocetkladnych += 1
        elif (cislo < 0): 
            pocetzapornych += 1
        elif (cislo == 0): 
            pocetnul += 1
    print(f"{tisk} Počet kladných čísel je {pocetkladnych}, Počet záporných čísel je {pocetzapornych} a nul je celkem {pocetnul}")
#opa()



# Program se zeptá na počet čísel, následně je vygeneruje
# Poté zobrazí čísla na řádku oddělená " ;" 
# Použíjte cyklus for
# Následně zobrazí počet kladných čísel a počet záporných čísel
# Opravit chyby - Program nespadne když zadám písmeno

def opačko():
    tisk = ""
    while(True):
        try:
            pocet = int(input("Zadejte počet čísel: "))
            break
        except:
            print("Zadal jsi nečíselnou hodnotu")
    pocetzapornych = 0
    pocetkladnych = 0
    pocetnul = 0
    for i in range(pocet):
        cislo = random.randint(-100, 100)
        tisk += str(cislo) + "; "
        if(cislo > 0): 
            pocetkladnych += 1
        elif (cislo < 0): 
            pocetzapornych += 1
        elif (cislo == 0): 
            pocetnul += 1
    print(f"{tisk}")
    print(f"Počet kladných čísel je {pocetkladnych}")
    print(f"Počet záporných čísel je {pocetzapornych}")
    print(f"Počet nul je {pocetnul}")
#opačko()


# Program se zeptá na počet čísel, následně je vygeneruje
# Poté zobrazí čísla na řádku oddělená " ;" 
# Použíjte cyklus for
# Následně zobrazí počet kladných čísel a počet záporných čísel
# Program následně zobrazí největší a nejmenší číslo
# Opravit chyby - Program nespadne když zadám písmeno



def opač():
    tisk = ""
    while(True):
        try:
            pocet = int(input("Zadejte počet čísel: "))
            break
        except:
            print("Zadal jsi nečíselnou hodnotu")
    pocetzapornych = 0
    maxcislo = -999999999
    mincislo = 999999999
    
    pocetkladnych = 0
    pocetnul = 0
    for i in range(pocet):
        cislo = random.randint(-10000, 10000)
        tisk += str(cislo) + "; "
        if(cislo > 0): 
            pocetkladnych += 1
        elif (cislo < 0): 
            pocetzapornych += 1
        elif (cislo == 0): 
            pocetnul += 1

        if (cislo > maxcislo):
            maxcislo = cislo
        if (cislo < mincislo):
            mincislo = cislo
    print(f"{tisk}")
    print(f"Počet kladných čísel je {pocetkladnych}")
    print(f"Počet záporných čísel je {pocetzapornych}")
    print(f"Počet nul je {pocetnul}")
    print(f"Největší číslo je {maxcislo}")
    print(f"Nejmenší číslo je {mincislo}")
#opač()


# Program se zeptá na počet čísel, následně je vygeneruje
# Poté se zeptá co chceme zobrazit
# Použíjte cyklus for
# Následně zobrazí počet kladných čísel a počet záporných čísel
# Program následně zobrazí největší a nejmenší číslo
# Opravit chyby - Program nespadne když zadám písmeno



def opak():
    tisk = ""
    while(True):
        try:
            pocet = int(input("Zadejte počet čísel: "))
            break
        except:
            print("Zadal jsi nečíselnou hodnotu")
    pocetzapornych = 0
    maxcislo = -999999999
    mincislo = 999999999
    
    pocetkladnych = 0
    pocetnul = 0
    for i in range(pocet):
        cislo = random.randint(-10000, 10000)
        tisk += str(cislo) + "; "
        if(cislo > 0): 
            pocetkladnych += 1
        elif (cislo < 0): 
            pocetzapornych += 1
        elif (cislo == 0): 
            pocetnul += 1
        if (cislo > maxcislo):
            maxcislo = cislo
        if (cislo < mincislo):
            mincislo = cislo
    while(True):
        nabidka = input("1. Výpis čísel; 2. Počet kladných čísel; 3. Maximální a minimální hodnota; 4. Počet záporných čísel; 5. Počet nul; 6. Konec programu: ")
        if nabidka == "1":
            print(tisk)
        elif nabidka == "2":
            print("Počet kladných čísel je: ", pocetkladnych)
        elif nabidka == "3":
            print(f"Minimální hodnota je: {mincislo} a  maximální hodnota je: {maxcislo}")
        elif nabidka == "4":
            print("Počet záporných čísel je: ", pocetzapornych)
        elif nabidka == "5":
            print(f"Počet nul je: {pocetnul}")
        elif nabidka == "6":
            break
opak()