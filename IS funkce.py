
# str.isalpha()      - Vrátí True pokud jsou všechny znaky písmena a řetězec obsahuje alespoň jeden znak
# str.isdigit()      - Vrátí True pokud jsou všechny znaky jsou číslice a řetězec obsahuje alespoň jeden znak
# str.islower()      - Vrátí True pokud jsou všechny znaky malá písmena a řetězec obsahuje alespoň jeden znak
# str.isupper()      - Vrátí True pokud jsou všechny znaky velká písmena a řetězec obsahuje alespoň jeden znak
# text.startswith(s) - Začíná text řetězcem s?
# text.endswith(s)   - Končí text řetězcem s?
# ord()              - Převod znaku na Ascii
# chr()              - převod ascii na znak
# str.isnumeric      - Testuje zda jde text převést na číslo


# Program bude pracovat s textovým řetězcem, který načte, následně vypíše počet malých a počet velkých písmen

def retezec():
    text = input("Zadejte text: ")
    velkych = 0
    malych = 0
    for i in text:
        if (i.islower() == True):
            malych += 1
        if (i.isupper() == True):
            velkych += 1
    print(f"Velkých písmen je {velkych}")
    print(f"Malých písmen je {malych}")
#retezec()


# S čísly

def cisla():
    text = input("Zadejte text: ")
    cisla = 0
    for i in text:
        if (i.isdigit() == True):
            cisla += 1
    print(f"Čísel je {cisla}")
#cisla()


# Program bude pracovat s textovým řetězcem, který načte, následně vypíše počet malých, počet velkých písmen a počet číslic

def celyretez():
    text = input("Zadejte text: ")
    velkych = 0
    malych = 0
    cisla = 0
    for i in text:
        if (i.islower() == True):
            malych += 1
        if (i.isupper() == True):
            velkych += 1
        if (i.isdigit() == True):
            cisla += 1
    print(f"Čísel je {cisla}")
    print(f"Velkých písmen je {velkych}")
    print(f"Malých písmen je {malych}")
    print("Počet písmen je", velkych+malych)
#celyretez()


# Program načte text. Poté zobrazí volbu:
# 1. Výpis velkých písmen
# 2. Výpis malých písmen
# 3. Výpis číslic
# 4. Konec

def nacitac():
    text = input("Zadejte text: ")
    velke = ""
    male = ""
    cisla = ""
    while(True):
        otazka = input("1. Výpis velkých písmen; 2. Výpis malých písmen; 3. Výpis čísel; 4. Konec    ")
        if (otazka == "1"):
            for i in text:
                if (i.isupper() == True):
                    velke += i
            print(f"Velké písmena jsou {velke}")
        if (otazka == "2"):
            for z in text:
                if (z.islower() == True):
                    male += z
            print(f"Velké písmena jsou {male}")
        if (otazka == "3"):
            for c in text:
                if (c.isdigit() == True):
                    cisla += c
            print(f"Čísla jsou {cisla}")
        if (otazka == "4"):
            break
#nacitac()


# Program načte dvě hodnoty. Pokud jsou obě číselné pak zobrazí jejich součet
# Jinak zobrazí spojení obou hodnot 1+1=2 / 1+abc=1abc
# Odstraní jejcih případné mezery
#* str.isnumeric - Testuje zda jde text převést na číslo

#  float - desetiný datový typ - 1.0
#  string - textový datový typ "text"

def JednaAbc():
    text1 = input("Zadejte první hodnotu: ").strip()
    text2 = input("Zadejte druhou hodnotu: ").strip()
    if (text1.isnumeric() and text2.isnumeric()):
        print(float(text1)+float(text2))
    else:
        print(text1+text2)
JednaAbc()

