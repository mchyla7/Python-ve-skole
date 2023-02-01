

#* Importovaný random

import random


def znakyVTextu():
    text = "abcdefghij"
    print("První znak: ", text[0])
    print("Poslední znak: ", text[-1])
    print("Vše od druhého znaku: ", text[1:])
    print("Druhý až čtvrtý: ", text[1:4])
#znakyVTextu()



def textVypis():
    for i in "abcdefghijklmnop":
        print(i)
#textVypis()

# Program načte text, zobrazí jej tak že znaky budou odděleny mezerou ""

def text():
    text = input("Zadejte písmena: ")
    tisk = ""
    for i in text:
        tisk += i + "  "
    print(tisk)
#text()


# Program načte text, zobrazí jej tak že znaky budou napsány v opačném pořadí

def textopacneporadi():
    text = input("Zadejte písmena: ")
    tiskopac = ""
    for i in text:
        tiskopac = i + " " + tiskopac 
    print(tiskopac)
#textopacneporadi()


# Program načte text, případně mezery nahradí "_"
# aho j - aho_j

def nahradt():
    text = input("Zadejte text: ")
    tisk = ""
    for i in text:
        if i == " ":
            tisk += "_"
        else:
            tisk+=i
    print(tisk)
#nahradt()


# Program načte text a následně očísluje všechny znaky


def ocislovat():
    text = input("Zadejte text: ")
    tisk = ""
    pocitadlo = 1
    for i in text:
        tisk += str(pocitadlo)+ "." + i + ", "
        pocitadlo += 1
    print(tisk)
#đocislovat()

# Program načte text a čísla nahradí "_"

def podtrzitkomistomezer():
    cisla = "0123456789"
    text = input("zadejte text: ")
    tisk = ""
    for i in text:
        if i in cisla:tisk+=""
        else: tisk+=i
    print(tisk)
#podtrzitkomistomezer()




# Program se zeptá na text
# Následně se bude ptát na pozice znaků a zobrazovat dané znaky
# Ošetřete situaci, kdy se zadá neexistující pozice
#
# Hint: len("abcd") funkce vrátí počet znaků v textu


def retardovanyprogram():
    text = input("Zadejte text: ")
    while(True):
        cislo = int(input("Zadejte číslo znaku: "))
        if cislo <=0 or cislo > len(text):
            print("Chyba")
            continue

        print(text[cislo-1])
#retardovanyprogram()




# Program se zeptá na text
# Následně se bude ptát na pozice znaků a zobrazovat dané znaky
# Ošetřete situaci, kdy se zadá neexistující pozice
# Program se ukončí pokud se za číslo zadáme písmeno

def retardovanyprogramsukoncenim():
    text = input("Zadejte text: ")
    pisemna = ("abcdefghijklmnopqrsstuvwxyz")
    pisemnaV = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    while(True):
        try:
            cislo = int(input("Zadejte číslo znaku: "))
        except:
            break # Ukončí cyklus - kod pokračuje za cyklem

        if cislo <=0 or cislo > len(text):
            print("Chyba")
            continue
        print(text[cislo-1])
#retardovanyprogramsukoncenim()



# Funkce zobraí nahodně zvolený znak z abecedy
# random.choice(text) - vrátí náhodně zvolený znak z textu v proměnné text

def nahodnyZnak():
    znaky = "abcdefghijklmnopqrstuvwxyz"
    print(random.choice(znaky))
#nahodnyZnak()



# Program bude generovat heslo (Řetězec náhodných znaků)
# Program se zeptá na počet znaků
# První znak bude písmenko a pak číslo
# Pak vytsikne heslo

#* Můj program
#! Nevytiskne mi liché čísla

def heslo():
    znaky = "abcdefghijklmnopqrstuvwxyz"
    cisla = "1234567890"
    pocet = int(input("Zadejte počet znaků: "))
    heslo = ""
    pocetmain = int(pocet/2)
    for i in range(pocetmain):
        heslo += random.choice(znaky)
        heslo += random.choice(cisla)
    print("Tvoje heslo je: ", heslo)
#heslo()


#* Učitelův

def heslo2():
    znaky = "abcdefghijklmnopqrstuvwxyz"
    pocet = int(input("Zadejte počet znaků: "))

    znak = True # Proměná slouží jako přepínač - jednou bude znak a jednou bude číslice
    heslo = ""
    for i in range(pocet):
        if znak: 
            heslo += random.choice(znaky)
        else:
            heslo += str(random.randint(0,9))
        znak = not znak # Negace hodnoty
    print("Tvoje heslo je ", heslo)
#heslo2()



# Program vytvoří heslo
# Které bude obsahovat písmena i číslice
# Bude začínat číslicí a bude končit písmenem



def heslo3():
    znaky = "abcdefghijklmnopqrstuvwxyz"
    cisla = "0123456789"
    pocet = int(input("Zadejte počet znaků: "))
    heslo = ""
    prvniZnak = random.choice(cisla)
    posledníZnak = random.choice(znaky)

    for i in range(pocet-2):
        heslo += random.choice(znaky + cisla)
    heslo = prvniZnak + heslo + posledníZnak
    print("Tvoje heslo je: ", heslo)
#heslo3()


# Program vytvoří heslo
# Které bude obsahovat písmena i číslice
# Bude začínat číslicí a bude končit písmenem
# Program se zeptá kolik hesel má vygenerovat
# Program se zeptá, jestli má vygenerovat se speciálním znakem


def heslo4():
    znaky = "abcdefghijklmnopqrstuvwxyz"
    cisla = "0123456789"
    specialniZnaky = "?:-/()#*+$"
    pocet = int(input("Zadejte počet znaků: "))
    pocetHesel = int(input("Kolik hesel se má vygenerovat: "))
    pouzitZnak = input("Speciální znak: ")

    for p in range(pocetHesel):
        heslo = ""
        prvniZnak = random.choice(cisla)
        posledníZnak = random.choice(znaky)
        for i in range(pocet - 2):
            heslo += random.choice(znaky + cisla)
        
        if pouzitZnak == "1":
            heslo = prvniZnak + random.choice(specialniZnaky) + heslo[1:] + posledníZnak   #Použje první heslo v 223 řádku a vymaže jeden znak 

        else:
            heslo = prvniZnak + heslo + posledníZnak
        print(heslo)
#heslo4()



# Program načte text
# Načte hledaný znak
# Program vrátí, kolikrát se daný znak v textu nachází


def hledaniVtextu():
    text = input("Zadejte text: ")
    hledat = input("Zadejte hledaný znak: ")
    pocet = 0
    for znak in text:
        if hledat == znak: pocet += 1
    print("Počet výskytů je ", pocet)

#hledaniVtextu()



# Program načte text
# Načte hledaný znak
# Program s zeptá co chci odstratnit a následně to odstraní


def mazaniTextu():
    text = input("Zadejte text: ")
    tisk = ""
    hledat = input("Zadejte znak, který chete smazat: ")
    for i in text:
        if hledat != i:
            tisk += i

    print(tisk)

#mazaniTextu()




# Program načte text
# Zobrazí volbu
# 1. Výpis zadaného textu
# 2. Výpis textu v opačném pořadí
# 3. Všechny číslice nahradí znakem "*" a zobrazí text
# 4. Konec


def vypis():
    text = input("Zadejte text: ")
    while(True):
        nabidka = input("1. Text, 2. Text naopak, 3. Čísla nahrazené * a daný text, 4. Konec : ")
        if nabidka == "1":
            print(text)
        if nabidka == "2":
            tiskopac = ""
            for i in text:
                    tiskopac = i + tiskopac 
            print(tiskopac)
        if nabidka == "3":
            cisla = "0123456789"
            tisk = ""
            for i in text:
                if i in cisla:tisk+=""
                else: tisk+=i
            print(tisk)
        if nabidka == "4":
            break
vypis()

                    