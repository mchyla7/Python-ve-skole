
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

# Zjišťujeme jestli je číslo kladné nebo nekladné


def kladne_nekladne():
    cislo = float(input("Číslo: "))
    if cislo>0:
        print("Číslo je kladné ✔")
    else:
        print("Číslo není kladné ❌")
kladne_nekladne()