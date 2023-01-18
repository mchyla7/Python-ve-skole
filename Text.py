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
nahradt()

# Program načte text a následně očísluje všechny znaky

def ocislovat():
    text = input("Zadejte text: ")
    tisk = ""
    pocitadlo = 0
    for i in text:
        if i 
    print(tisk)