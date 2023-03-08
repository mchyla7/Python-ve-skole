
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

text()


# PRogram načte text
# Liché znaky budou velkým písmenem
# Sudé budou malým


def sude():
    text = input("Zadjete text: ")
    while()