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
        

# Vytvořte variantu, kdy číslo vstupuje pomocí parametru a funkce hodnotu vrací. Funkci zavolejte