# Funkce bez paramteru - nevrací hodnotu

def soucetJedna():
    a = float(input("A: "))
    b = float(input("B: "))
    print(a+b)

# soucetJedna()

# Funkce s parametrem - nevrací hodnotu

def soucetDva(a,b):
    print(a+b)

# soucetDva(10,30)

# FUnkce s parametrem - vraci hodnotu

def soucetCtvrty(a,b):
    return(a+b)

# print (soucetCtvrty(10,30))


# Vytovřte program který načte číslo a vypíše zda je kladné/záporné/nula. Funkce je bez parametrů a nevrací hodnotu

def start():
    cislo = float(input("Zadejte číslo: "))
    if cislo > 1:
        print("Kladné")
    elif cislo < 0:
        print("Záporné")
    elif cislo == 0:
        print("Nula")

# Vytvořte variantu, kde číslo vstupuje pomocí parametru. Funkce nevrací hodnotu a funkci zavolejte

def KzNL(c):
    if c > 0:
        return("Kladné")
    elif c < 0:
        return("Záporné")
    elif c == 0:
        return("Nula")
        

# Program se zpeta, zda chceme zjistit obvod čtverce, obdelníku nebo trojuhleníku a kruhu
# Násldně se program zepta na strany a zodbrazí zvoleny obvod
# Nejprve vytvořte tři funkce pro výpočet obvod pro jednotlivé tvary
# Funkce budou mít parametr a budou vracet hodnotu
# Následně pozijte v hlavním programu

def obvodCtverce():
    a = float(input("Zadejte stranu: "))
    return(4*a)

def obvodObdelniku():
    ao = float(input("Zadejte stranu a: "))
    bo = float(input("Zadejte stranu b: "))
    return(2*(ao+bo))

def obvodtrojuhelniku():
    at = float(input("Zadejte stranu a: "))
    bt = float(input("Zadejte stranu b: "))
    ct = float(input("Zadejte stranu c: "))
    return(at+bt+ct)

def obvodKruhu():
    r = float(input("Zadej poloměr: "))
    return(2*3,14*r)

def HlavniProgram():
    while(True):
        otazka = input("1. Obvod čtverce, \n2. Obvod Obdelníku, \n3. Obvod Trojuhleníku \n4. Obvod Kruhu, \n5. Konec\n")
        if otazka =="1":
            print(obvodCtverce())
        elif otazka == "2":
            print(obvodObdelniku())
        elif otazka == "3":
            print(obvodtrojuhelniku())
        elif otazka == "4":
            print(obvodKruhu())
        elif otazka == "5":
            break
#HlavniProgram()

# Program načte text, poté zobrazí volbu: 
# 1. Výpis velkých písmen
# 2. Výpis malých písmen
# 3. Výpis číslic
# 4. Konec
# Volby vytvořte ve formě podprogramů, které budou mít parametr a budou vracet hodnotu

def velkaPismena(text):
    tisk = ""
    for i in text:
        if i.isupper():
            tisk += i
    return(tisk)

def malaPismena(text):
    tisk = ""
    for i in text:
        if i.islower():
            tisk += i
    return(tisk)

def cisla(text):
    tisk = ""
    for i in text:
        if i.isdigit():
            tisk += i
    return(tisk)

def MainProgram():
    text = input("Zadejte text: ")
    while(True):
        volba = input("1. Výpis velkých písmen, \n2. Výpis malých písmen, \n3. Výpis číslic, \n4. Konec\n")
        if volba == "1":
            print(velkaPismena)
        elif volba == "2":
            print(malaPismena)
        elif volba == "3":
            print(cisla)
        elif volba == "4":
            break
MainProgram() 