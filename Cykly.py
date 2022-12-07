#
#*     Cykly
#

#
# while(podmínka): -- Dokud je podmínka splněná = opakuje se blok příkazu
#   blok příkazu

# Program bude načítat kladné čísla. Po zadní nekladného se načítání ukončí.
# Následně program načte čísla zobrazí

def cyklus():
    tisk = ""
    a = 1
    while(a > 0):
        a = float(input("Zadejte kladné číslo: "))
        if a > 0:
            tisk=tisk+str(a)    + "; "
    print(tisk)
#cyklus()

#  S programem break

def cyklus2():
    tisk = ""
    while(True):
        a = float(input("Zadejte kladné číslo: "))
        if a <= 0: break # Break ukončí cyklus
        tisk=tisk+str(a) + "; "
    print(tisk)
#cyklus2()


# Bez IFu

def cyklus3():
    tisk = ""
    a = float(input("Zadejte kladné číslo: "))
    while(a > 0):
        tisk=tisk+str(a) + "; "
        a = float(input("Zadejte kladné číslo: "))
    print(tisk)
#cyklus3()


# Program načítá čísla, pokd zadám 0 program se ukončí
# S nulou se nebude dále pracovat
# Program zobrazí výpis a součet daných čísel
# Průměrnou hodnotu
# Opačný výpis
#! mrd** to je

def programbeznuly():
    tisk = ""
    a = float(input("Zadejte kladné číslo: "))
    while(a > 0):
        tisk=tisk+str(a) + "; "
        a = float(input("Zadejte kladné číslo: "))
    print(tisk, " ;",  )
#programbeznuly()


#* Učitelův program
# Program načítá čísla, pokd zadám 0 program se ukončí
# S nulou se nebude dále pracovat
# Program zobrazí výpis a součet daných čísel
# Průměrnou hodnotu
# Opačný výpis

def ucitel():
    c = 0
    tisk = ""
    tiskopac = ""
    soucet = 0
    pocet = 0
    while (True):
        c = float(input("Zadejte číslo: "))
        if (c==0): break #Po zadání 0 ukončí načítání
        
        tisk += str(c) + ";" # tisk = tisk + str(c) + ";" 
            # vytváření opačného výpisu
        tiskopac = str(c) + ";" + tiskopac
        soucet += c      #soucet = soucet + c
        pocet += 1       # pocet = pocet + 1

    print(tisk)
    print("Součet: ", soucet)
    print("Průměr: ", soucet/pocet)
    print("Opačný výpis: ", tiskopac)
#ucitel()



# Program načte čísla, pokud zadáme číslo větší než 100 nebo <- 100  Načítání se ukončí
# Program zobrazí nejprve záporná čísla

def nacitanicisel():
    TiskZ = ""
    Tisk = ""
    soucet = 0
    while(True):
        cislo = float(input("Zadejte číslo: "))
        if cislo <- 100 or cislo > 100 :break
        if cislo < 0: TiskZ += str(cislo) + "; "
        else: Tisk += str(cislo) + "; "
        soucet = soucet + cislo

    print(TiskZ)
    print(Tisk)
    print(soucet)
nacitanicisel()
