
#*  Relační podmínky
# x == y                # x Je rovno y 
# x != y                # x není rovno y 
# x > y                 # x je větší než y
# x < y                 # x je menší než y
# x <= y                # x je větší nebo rovno y
# x >= y                # x je mneší nebo rovno y


#Zjišťujeme jestli je číslo kladné


def kladne():
    cislo = float(input("Číslo: "))
    if cislo>0:
        print("Číslo je kladné ✔")
#kladne()

#* Zjišťujeme jestli je číslo kladné nebo nekladné


def kladne_nekladne():
    cislo = float(input("Číslo: "))
    if cislo>0:
        print("Číslo je kladné ✔")
    else: # Else se používá jen jednou v programu a nelze ho použít víckrát
        print("Číslo není kladné ❌")
#kladne_nekladne()

def kladnecislo():
    cislo =  float(input("Zadejte číslo: "))
    if cislo > 0:
        print("Číslo je kladné")
    elif cislo == 0:
        print("Číslo je nula")
    elif cislo < 0:
        print("Číslo je záporné")
#kladnecislo()



def plnoletost():
    vek = float(input("Váš věk: "))
    if vek >= 18:
        print("Jsi plnoletý 😘")
    else:
        print("Nejsi plnoletý 😖")
#plnoletost()

#Zjístit vzálenost od nuly
#Program na zjíštění absolutní hodnoty

def absolutnihodnota():
    cislo = float(input("Zadej číslo: "))
    if cislo < 0:
        print("Číslo je od nuly vzdáleno o:", -1*cislo)
    else:
        print("Číslo je vzdáleno od nuly o: ", cislo)
#absolutnihodnota()


#Program na zaokrouhlení čísla

def zaokrouhli():
    cislo = float(input("Zadej číslo: "))
    pocetmist = int(input("Počet desetiných míst: "))
    print(round(cislo,pocetmist))
#zaokrouhli()

#* Program načte číslo s desetiným místem
#  - Zeptá se jestli chceme zaokrouhlit
#  - Pokud ano, tak zaokrouhlí číslo a vytiskne ho
#  - Pokud ne, tak vytiskne číslo, které jsme zadali 


def chceszaokrouhlit():
    cislo = float(input("Zadej číslo: "))
    ano = str(input("Chceš číslo zaokrouhlit? y/n "))
    if ano == "y":
        print(round(cislo))
    elif ano == "n":
        print("Tvoje číslo je: ",cislo)
#chceszaokrouhlit()


#* Program na zjištění jakou máš známku slovy

def znamky():
    znamka = float(input("Zadej svojí známku: "))
    if znamka == 1:
        print("Tvoje známka je výborná" )
    elif znamka == 2:
        print("Tvoje známka je chválitelná")
    elif znamka == 3:
        print("Tvoje známka je dobrá")
    elif znamka == 4:
        print("Tvoje známka je dostatečná")
    elif znamka == 5:
        print("Tvoje známka je nedostatečná")
    else:
        print("Chyba - Taková známka není")
#znamky()





# Program načte dvě čísla nejdříve zobrazí větší potom menší - seřadí je

def serad():
    cislo1 = float(input("Zadej první číslo: "))
    cislo2 = float(input("Zadej druhé číslo: "))
    if cislo1 > cislo2:
        print(cislo1, "----" ,cislo2)
    else:
        print(cislo2 ,"----", cislo1)
#serad()



# Program načte tři čísla nejdříve zobrazí větší potom menší - seřadí je

def serad():
    cislo1 = float(input("Zadej první číslo: "))
    cislo2 = float(input("Zadej druhé číslo: "))
    cislo3 = float(input("Zadej třetí číslo: "))
    if cislo1 >= cislo2 >= cislo3:
        print(cislo1, "----" ,cislo2, "----" ,cislo3)
    elif cislo1 >= cislo2 <= cislo3:
        print(cislo1, "----" ,cislo3, "----" ,cislo2)
    elif cislo1 <= cislo2 <= cislo3:
        print(cislo3, "----" ,cislo2, "----" ,cislo1)
    elif cislo1 <= cislo2 >= cislo3:
        print(cislo3, "----" ,cislo2, "----" ,cislo1)
#serad()


#* Převede na malé písmena - text.lower()
#* Převede na velké písmena - text.upper()

# Program načte text
# Zeptá se 1.převést na velké, 2. na malé
# Jiná volba - vytiskne původní text


def velkynebomaly():
    text = input("Zadejte text: ")
    a = input("Velké písmena - 1, Malé písmena - 2: ")
    if  a == "1":
        print(text.upper())
    elif a == "2":
        print(text.lower())
    else:
        print(text)
#velkynebomaly()




# Program který pro dvě čísla x,y
# Spočítá hodnotu 1/(x*y)
# Ale musí být podmínka že nesmí být číslo 0

def dvecisla():
    x = float(input("Vložte první číslo: "))
    y = float(input("Vložte druhé číslo: "))
    if x*y == 0:
        print("Nula se nemůže použít")
    else: 
        print("Hodnota je: ", 1/(x*y))
#dvecisla()


# Zjistěte, zda číslo x leží uvnitř, před nebo za hranicí intervalu <1,100>

def interval():
    x = float(input("Zadejte číslo: "))
    if x  >= 100:
        print(x, "Nepatří do intervalu <1,100>")
    elif x <= 0:
       print(x, "Nepatří do intervalu <1,100>") 
    else: 
       print(x, "Patří do intervalu <1,100>")
    q = input("do you want to continue?: ")
#interval()


# Jsou 4 druhy vstupného:
# 300,- -- do 10 let včetně
# 500,- -- od 11-18 let včetně
# 1000,- -- od 19-60 let včetně
# 400,- -- od 60 let včetně 
# Jsi mrtvý lol -- od 100 let včetně
#
#Program, který po zadání vstupného spočítá kolik mu bude stát lístek


#TODO Opravit 
#!Chyba opravit doma

def vstupne():
    vek = int(input("Zadejte věk: "))
    if vek > 100:
        print("Rip Boomer")
    elif vek >= 60:
        print("Bude tě to stát 400 Kč.")
    elif vek < 59 and vek >= 18:
        print("Bude tě to stát 1000 Kč.")
    elif vek <= 18 and vek >= 11:
        print("Bude tě to stát 500 Kč.") 
    else: 
        vek > 10
        print("Bude tě to stát 300 Kč.")
#vstupne()


def kalkulator():
    x = float(input("Zadejte první číslo: "))
    znamenko = input("Vyberte operaci (+|-|*|/): ")
    y = float(input("Zadejte druhé číslo: "))
    if znamenko == "+" :
        print(x+y)
    elif znamenko == "-":
        print(x-y)
    elif znamenko == "*":
        print(x*y)
    elif znamenko == "/":
        if y == 0:
            print("! Nulou se nedá dělit !")
        else:
            print(x/y)
    else:
        print("Zadejte správnou operaci")   
#kalkulator()

def nictakovehotadynemam():
    try:
        cislo = float(input("Číslo: "))
    except:
        print("Číslo není kladné ✔")
        return
    if cislo > 0: 
        print("Gratiuluji zadal jsi kladné číslo")
nictakovehotadynemam()



#  Program načte dvě číselné hodnoty A a B
#  Program provede výraz a/b
#  Když je b nebo a 0 tak to napíše chybu
#  Celý program má být bez if
#! Nemám tušení co a jak

def dveciselnehodnoty():
    try:
        cislo1 = int(input("Zadejte první číslo: "))
        cislo2 = int(input("Zadejte druhé číslo: "))
        expect:
            print("Nezadal jsi číslo")
        return
    
    try:
            print(cislo1/cislo2)
        except:
            print("nulou nelze dělit")
dveciselnehodnoty()