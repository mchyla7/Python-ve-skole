# ord("znak/písmenko") - Napíše číslo daného znaku
# chr(číslo)           - Napíše znak daného čísla


# Vypište pozice číslic v tabulce Ascii

def prvniASCII():
    print("0 -", ord("0"))
    print("1 -", ord("1"))
    print("2 -", ord("2"))
    print("3 -", ord("3"))
    print("4 -", ord("4"))
    print("5 -", ord("5"))
    print("6 -", ord("6"))
    print("7 -", ord("7"))
    print("8 -", ord("8"))
    print("9 -", ord("9"))
#prvniASCII()

# Učitelův

def druhyASCII():
    for i in range(0,10):
        print(str(i),ord(str(i)))
druhyASCII()


# Vypište velká písmena abecedy z ASCII tabulky

def tretiASCII():
    for i in range(65,91):
        print(chr(i))
tretiASCII()


# Program načte text bez diakritiky a zakodujeho tak, že každý znak nahradí znakem o 3 místa posunutým v ASCII Tabulce
def kodovani():
    text = input(str("Zadejte text: "))
    