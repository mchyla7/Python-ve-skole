
# 
#░░░░░██╗███████╗██████╗░███╗░░██╗░█████╗░  ░██████╗███████╗  ░░░░░██╗███████╗███╗░░██╗  ░█████╗░
#░░░░░██║██╔════╝██╔══██╗████╗░██║██╔══██╗  ██╔════╝██╔════╝  ░░░░░██║██╔════╝████╗░██║  ██╔══██╗
#░░░░░██║█████╗░░██║░░██║██╔██╗██║███████║  ╚█████╗░█████╗░░  ░░░░░██║█████╗░░██╔██╗██║  ██║░░██║
#██╗░░██║██╔══╝░░██║░░██║██║╚████║██╔══██║  ░╚═══██╗██╔══╝░░  ██╗░░██║██╔══╝░░██║╚████║  ██║░░██║
#╚█████╔╝███████╗██████╔╝██║░╚███║██║░░██║  ██████╔╝███████╗  ╚█████╔╝███████╗██║░╚███║  ╚█████╔╝
#░╚════╝░╚══════╝╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝  ╚═════╝░╚══════╝  ░╚════╝░╚══════╝╚═╝░░╚══╝  ░╚════╝░
#
#██████╗░██████╗░██╗██████╗░██████╗░░█████╗░██╗░░░██╗██╗░░░██╗  ███╗░░██╗░█████╗░
#██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗██║░░░██║██║░░░██║  ████╗░██║██╔══██╗
#██████╔╝██████╔╝██║██████╔╝██████╔╝███████║╚██╗░██╔╝██║░░░██║  ██╔██╗██║███████║
#██╔═══╝░██╔══██╗██║██╔═══╝░██╔══██╗██╔══██║░╚████╔╝░██║░░░██║  ██║╚████║██╔══██║
#██║░░░░░██║░░██║██║██║░░░░░██║░░██║██║░░██║░░╚██╔╝░░╚██████╔╝  ██║░╚███║██║░░██║
#╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░  ╚═╝░░╚══╝╚═╝░░╚═╝
#
#████████╗███████╗░██████╗████████╗
#╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
#░░░██║░░░█████╗░░╚█████╗░░░░██║░░░
#░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░
#░░░██║░░░███████╗██████╔╝░░░██║░░░
#░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░



#
# len("abc") = 3 - napíše počet znaků
# r="abcefg"
#
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



# Program načte text
# Zobrazí nabídku
# 1. Převede všechno na velká písmena
# 2. Převede všechno na malá písmena
# 3. Odstraní mezery z celého textu
# 4. Počáteční písmeno bude velké
# 5. Vymaže všechny čísla
# 6. Zamění vybraný znak za zadaný znak


def final():
    text = input("Zadejte text: ")
    while(True):
        otazka = input("1, 2, 3, 4, 5, 6, 7: ")
        if (otazka == "1"):
            print(text.upper())
        if (otazka == "2"):
            print(text.lower())
        if (otazka == "3"):
            print(text.replace(" ", ""))
        if (otazka == "4"):
            prvni = text[0].upper()
            posledni = text[-1].upper()
            ostatni = text[1:-1]
            print(prvni+ostatni+posledni)
        if (otazka == "5"):
            text2 = text.replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","")
            print(text2)
        if (otazka == "6"):
            hledany = input("Zadejte hledaný znak: ")
            pocet = text.count(hledany)
            vyskyt = ""
            print (f"Počet výskytů {pocet}")

            if pocet > 0:
                p = 0
                for i in range(pocet):
                    pozice = text.index(hledany)
                    vyskyt += str(pozice) + "; "
                    p = pozice + 1 # Určuje od které pozice bude dále hledat

            print(f"Pozice výskytů je {vyskyt}")
        if (otazka == "7"):
            break

final()

