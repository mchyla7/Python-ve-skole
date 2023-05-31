
#* Metody pro práci s textem
# len("abc") = 3 - napíše počet znaků
# r="abcefg"
#* r.upper()   - Převod na velká písmena
#* r.lower()   - Převod na malá písmena
# r.count(s)  - Počet výskytů s v r
# r.index(s)  - Pozice 1. výskytu s v r
# r.index(s,n)- Pozice 1.výskytu s v r od pozice n
# r.lstrip()  - Odstraní mezery ze začátku
# r.rstrip()  - Odstraní mezery z konce
#* r.strip()   - Odstraní mezery z obou stran
#* str.replace(old, new]) - Nahrazení textu
# str.isalpha() - Vrátí True pokud jsou všechny znaky písmena a řetězec obsahuje alespoň jeden znak
# str.isdigit() - Vrátí True pokud jsou všechny znaky jsou číslice a řetězec obsahuje alespoň jeden znak
# str.islower() - Vrátí True pokud jsou všechny znaky malá písmena a řetězec obsahuje alespoň jeden znak
# str.isupper() - Vrátí True pokud jsou všechny znaky velká písmena a řetězec obsahuje alespoň jeden znak
# text.startswith(s) - Začíná text řetězcem s?
# text.endswith(s)   - Končí text řetězcem s?
# ord() - Převod znaku na Ascii
# chr() - Převod ascii na znak


def text():
    text="abc"
    print(len(text))
    print(text.upper())
    print(text.lower())
    print(text[0].upper())
    print(text[0].upper()+text[1:].lower())
#text()


# Program načte text
# Liché znaky budou velkým písmenem
# Sudé budou malým


def sude():
    text = input("Zadjete text: ")
    text2 = ""
    velke = True
    for i in text:
        if velke:
            text2 += i.upper()
        else:
            text2 += i.lower()
        velke = not velke
    print(text2)
#sude()


# Program načte text
# Odstraní případné mezery před a za textem - strip()
# Text zobrazí pod sebou

def mezery():
    text = input("Zadejte text: ")
    text = text.strip()
    for znak in text:
        print(znak)
#mezery()

# Program načte text a zeptá se na hledaný řetězec.
# Následně zobrazí počet výskytů hledaného řetězce.
# text.count(hledaný text) - vrátí počet výskytů

def google():
    text = input("Zadejte text: ")
    hledani = input("Zadejte co hledáte: ")
    pocet = text.count(hledani)
    print(f"Počet je {pocet}")
#google()

# Program načte text a zeptá se na hledaný řetězec
# Následně zobrazí počet výskytů hledaného řetězce.
# Poté se opět zeptá na hledaný řetězce
# Program napíše na které pozici se daný znak vyskytuje poprvé
# Program se ukončí pokus hledaný řetězec je prázdný
#! nefungje

def googleswhile():
    text = input("Zadejte text: ")
    while(True):
        hledani = input("Zadejte co hledáte: ")
        pocet = text.count(hledani)
        if pocet == "":
            break
        print(f"Počet je {pocet}")
        print(f"Pozice prvního výskytu je")    



# Program načte text a zeptá se na hledaný řetězec
# Následně zobrazí počet výskytů hledaného řetězce
# Následně zobrazí pozici v textu, kse se nachází.
# Například: "ababa" pozice znaku "a": 0,2,4

# Program načte text
# Odstraní mezery před a za, ostatní mezery nahradí "_"
# Vstup "a b c"
# Výstup "a_b_c"

def nahrazenimezer():
    text = input("Zadejte text: ")
    text2 = text.strip().replace(" " , "_")
    print(text2)

#nahrazenimezer()


# Program načte text
# Poté zobrazí nabídku:
# 1. Program se zeptá na délku textu
# 2. Program zobrazí text tak, že první a poslední písmeno bude vždy velkým
# 3. Program zobrazí text tak, že všechny mezery a čárky budou nahrazeny podtržítkem
# 4. Program se zeptá na znak, poté zobrazí, zda se znak v textu vyskytuje - Pokud se vyskytuje, program hned zobrazí číslo pozice prvního výskytu znaku
# 5. Konec
# Dokud není zadaná žádná volba 5, program se stále vrací k volbě.

def nacitanikravin():
    text = input("Zadejte text: ")

    while(True):
        otazka = input("1. Délka textu  ; 2. Celý text a první a poslední písmeno je velkým ; 3. Text a mezery a čárky jsou nahrazeny podtržítkem ; 4. Vyskyt zanku v textu ; 5. Konec  : ")
        
        if (otazka == "1"):
            print(len(text))

        if (otazka == "2"):
            prvni = text[0].upper()
            posledni = text[-1].upper()
            ostatni = text[1:-1]
            print(prvni+ostatni+posledni)

        if (otazka == "3"):
            bezhackuamezer = text.strip().replace(" ","_").replace(",", "_")
            print(bezhackuamezer)

        if (otazka == "4"):
            znak = input("Zadejte znak: ")
            if (text.count(znak)>0):
                print(f"Zank se vyskytuje a jeho první výskyt je na pozici {text.index(znak)}")
            else:
                print("Znak se zde nevyskytuje")

        if (otazka == "5"):
            break

#nacitanikravin()


# Program načte text
# Pokud obsahuje čísla tak je odstraní
# vstup "123ahojtykktnicolas"
# vystup "ahojtykktnicolas"

def nactitext():
    text = input("Zadejte text: ")
    if (text == 1,2,3,4,5,6,7,8,9,0):
        text2 = text.replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","")
        print(text2)
    else:
        print(text)
#nactitext()

#* Učitelův

def odstrancislaoddruhepozice():
    text = input("Zadejte text: ")
    text2 = ""
    for z in text:
        if (not z.isdigit()):
            text2 += z
    print(text2)
#odstrancislaoddruhepozice()

# Druhá možnost

def odstrancislaoddruhepozice2():
    text = input("Zadejte text: ")
    cisla = "0123456789"
    for z in cisla:
        text = text.replace(z, "")
    print(text)
#odstrancislaoddruhepozice2()


# Program se zeptá na text
# Z daného textu vezme číslo a uloží
# Následně jej vytiskne a písmenka nevytiskne
# vstup "123456axt" výstup "123456"
#! Nefunguje úplně geniálně ale je to od učitele, takže sere pes

def vytahcisel():
    text = input("Zadejte text: ")
    cislo = ""
    for znak in text:
        if not znak.isdigit():break
        cislo += znak
    print(cislo)
#vytahcisel()


