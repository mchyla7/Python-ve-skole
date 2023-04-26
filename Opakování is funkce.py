#* r.upper()   - Převod na velká písmena
#* r.lower()   - Převod na malá písmena
# r.count(s)  - Počet výskytů s v r
# r.index(s)  - Pozice 1. výskytu s v r
# r.index(s,n)- Pozice 1.výskytu s v r od pozice n
# r.lstrip()  - Odstraní mezery ze začátku
# r.rstrip()  - Odstraní mezery z konce
#* r.strip()   - Odstraní mezery z obou stran
#* str.replace(old, new]) - Nahrazení textu
# str.isalpha()      - Vrátí True pokud jsou všechny znaky písmena a řetězec obsahuje alespoň jeden znak
# str.isdigit()      - Vrátí True pokud jsou všechny znaky jsou číslice a řetězec obsahuje alespoň jeden znak
# str.islower()      - Vrátí True pokud jsou všechny znaky malá písmena a řetězec obsahuje alespoň jeden znak
# str.isupper()      - Vrátí True pokud jsou všechny znaky velká písmena a řetězec obsahuje alespoň jeden znak
# text.startswith(s) - Začíná text řetězcem s?
# text.endswith(s)   - Končí text řetězcem s?
# ord()              - Převod znaku na Ascii
# chr()              - převod ascii na znak
# str.isnumeric      - Testuje zda jde text převést na číslo


# Program bude načítat texty - ukončí načítání pokud není zadaný žádný znak
# Program nejprve zobrazí texty začínající číslicí potom zobrazí písmena a pak ostatní

def kravina():
    cisla = ""
    texty = ""
    ostatni = ""
    nevim = ""
    while(True):
        text = input("Zadejte text: ")
        if text == text:
            break
        if text[0].isdigit():
            cisla += text + "\n"
        if text[0].isnumeric():
            nevim += text + "\n" 
        if  text[0].isupper():
            texty += text + "\n"
        if text[0].isalpha():
            ostatni += text + "\n"

    print(nevim)
    print(cisla)
    print(texty)
    print(ostatni)
kravina()


 # Program načte text odstraní mezery před a za, mezery odstarní a nahradí "_" První znak Velkým ostatním malým

def mezery():
    text = input("Zadejte text: ")
    text = text.strip().replace(" ", "_")
    print(text[0].upper()+text[1:].lower())
mezery()


# Program načte text a zobrazí volbu
# 1. Zobrazí písmena
# 2. Zobrazí text tak že první a poslední písmeno bude velkým písmenem, ostatní znáky budou hvězdy
# 3. Pokud se v textu zobrazí mezera, pak zobrazí text pouze před mezerou. Pokud není mezera, zobrazí celý text
# 4. Konec

def volby():
    text = input("Zadejte text: ")
    while(True):
        otazka = input("1. Zobrazí písmena, 2. Hvězdičky, 3. Před mezerou, 4. Konec : ")
        if otazka == "1":
            tisk = ""
            for i in text:
                if i.isalpha():
                    tisk += i
                print(tisk)
        if otazka == "2":
            tisk2 = text[0].upper() + "*"*(len(text)-2) + text[-1].upper()
            print(tisk2)
        if otazka == "3":
            index = text.find(" ")
            if index == -1:
                print("Text bez mezery: ", text)
            else:
                print("Text před první mezerou: ", text[:index])
        if otazka == "4":
            break
volby()


