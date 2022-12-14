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
#! Můj nefunguje

def randomsudy():
    for i in range(0, 10):
        cislo = random.randint()
    if cislo % 2 == 0:
        print(cislo)
#randomsudy()       
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


def program():
    soucet = 0
    tisk = ""
    pocet = int(input("Zadejte počet čísel: "))
    for i in range(pocet):
        cislo = input("Zadejte číslo: ")
        tisk += cislo + "; "
        soucet += float(cislo)
    print(f"Průměr je {round(soucet/pocet)}")    # Funkce round zaokrouhlí čísla na dvě desetiná místa
    print(tisk)
#program()


# Program se zeptá na počet čísel nasledně je načte
# Pote zobrazí jejich průměr a vypíše je
# Použít cyklus for
# Pokud to nebude číslo tak se znova se opakuje


def program():
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
#program()




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
program()