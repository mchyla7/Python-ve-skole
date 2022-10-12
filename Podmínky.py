
#*  Relační podmínky
# x == y                # x Je rovno y 
# x != y                # x není rovno y 
# x > y                 # x je větší než y
# x < y                 # x je menší než y
# x <= y                # x je větší nebo rovno y
# x >= y                # x je mneší nebo rovno y


#Zjišťujeme jestli je číslo kladné

from tkinter import N


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
chceszaokrouhlit()