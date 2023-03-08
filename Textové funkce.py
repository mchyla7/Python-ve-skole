
#* Metody pro práci s textem
# len("abc") = 3
# r="abcefg"
# r.upper()   - Převod na velká písmena
# r.lower()   - Převod na malá písmena
# r.count(s)  - Počet výskytů s v r
# r.index(s)  - Pozice 1. výskytu s v r
# r.index(s,n)- Pozice 1.výskytu s v r od pozice n
# r.lstrip()  - Odstraní mezery ze začátku
# r.rstrip()  - Odstraní mezery z konce
# r.strip()   - Odstraní mezery z obou stran
# str.replace(old, new]) - Nahrazení textu
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
# Následně zobrazí počet výskytůhledaného řetězce.
# Poté se opět zeptá na hledaný řetězce
# Program napíše na které pozici se daný znak vyskytuje poprvé
# Program se ukončí pokus hledaný řetězec je prázdný

def googleswhile():
    text = input("Zadejte text: ")
    while(True):
        hledani = input("Zadejte co hledáte: ")
        pocet = text.count(hledani)
        if pocet == "":
            break
        print(f"Počet je {pocet}")
        print(f"Pozice prvního výskytu je {text.index(pocet)}")    
#googleswhile()


# Program načte text a zeptá se na hledaný řetězec
# Následně zobrazí počet výskytů hledaného řetězce
# Následně zobrazí pozici v textu, kse se nachází.
# Například: "ababa" pozice znaku "a": 0,2,4


def heldaniz():
    text = input("Zadejte text: ")
    hledany = input("Zadejte hledaný znak: ")
    pocet = text.count(hledany)

    vyskyt = ""
    print (f"Počet výskytů {pocet}")

    if pocet > 0:
        p = 0
        for i in range(pocet):
            pozice = text.index(hledany.p)
            vyskyt += str(pozice) + "; "
            p = pozice + 1 # Určuje od které pozice bude dále hledat

    print(f"Pozice výskytů je {vyskyt}")
hledaniz()

