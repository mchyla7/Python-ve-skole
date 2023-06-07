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
#MainProgram() 

# Napište podprogramy na  zašifrování a dekodování textu a vložte je do hlavního pragramu

def sifra(text):
    textsifra = ""
    for i in text:
        textsifra += chr(ord(i)+3)
    return(textsifra)

def dekodovani(textsifra):
    text = ""
    for y in textsifra:
        textsifra += chr(ord(y)-3)
    return(text)

def KodingDekodingTextu():
    while(True):
        volba = input("1. Zašifrovat \n2. Dešifrovat \n3. Konec \nVyberte program: ")
        if volba == "1":
            text = input("Zadejte text pro zašifrování: ")
            print (sifra(text), "\n")
        elif volba=="2":
            text = input("Zadej text pro dešifrování: ")
            print(dekodovani(text),"\n")
        elif volba =="3": 
            print("Ukončování programu 👋")
            break
KodingDekodingTextu()

#! Dekodování nefunguje


# Z následujícího programu vytvořte hlavní program a podprogramy        
                
# Program načte text.  
# Poté zobrazí nabídku:
# 1.	Program zobrazí délku textu.
# 2.	Program text zobrazí tak, že první a poslední písmeno bude velkým písmenem.
# 3.	Program zobrazí text tak, že všechny mezery a čárky budou nahrazeny  podtržítky.
# 4.	Program se zeptá na znak, poté zobrazí, zda se znak v textu vyskytuje. Pokud se vyskytuje, pak program zobrazí číslo pozice prvního výskytu znaku.
# 5.	Konec
# Dokud není zadaná volba 5, program se stále vrací k volbě.
#Z následujícího programu vytvořte hlavní program a podprogramy        
        
        


def delkatextu(text):
    return("Délka textu:",len(text))

def prvniAposledni(text):
    prvni=text[0].upper()
    posledni=text[-1].upper()
    ostatni =text[1:-1]        
    return(prvni+ostatni+posledni)

def nahrazeni(text):
    return(text.replace(" ", "_").replace(",", "_"))

def vyskytuje(text):
    znak=input("Zadej znak  ")
    if(text.count(znak)>0):
        return("Znak se vyskytuje.")
        return("První výskyt je na pozici ",text.index(znak))
    else:
        return("Znak se nevyskytuje!!!!!")


def shrnuti1():
    text = input("Zadej text  ")
    while(True):
        volba=input("1.delka,2.uprava,3.nahrazeni,4.vzhledavani,5.konec")
        if(volba=="1"):
            print(delkatextu)
        elif(volba=="2"):
            print(prvniAposledni)
        elif(volba=="3"):
            print(nahrazeni)
        elif(volba=="4"):
            print(vyskytuje)
        elif (volba=="5"):
            print("Ukončování programu 👋")
            break
shrnuti1()