
# Program načítá čísla
# Po každém načtení se zeptá jestli chceme program ukončit
# Každé čtvrté číslo se v tisku dá na další řádek
# po zadání "a" se program ukončí
# po zadání "a" se zobrazí volba:
# 1. výpis
# 2. průměr
# 3. maximální a minimalní hodnotu
# 4. počet záporných čísel
# 5. součet záporných čísel
#  6. konec


def programek():
    otazka = ""
    tisk = ""
    nabidka = ""
    soucet = 0
    soucetzapor = 0
    pocet = 0
    pocetnanovyradek = 0
    maxcislo = -9999999999999999999999999 # Musí být číslo větší aby se uloží číslo
    mincislo = 99999999999999999999999999 # Musí být velké aby se uložilo nejmenší
    zapornecisla = 0
    while(otazka.lower() != "a"): # Pokud(otázka.je_jedno_jestli_male_nebo_velke() nesmí být "a")
        cislo = float(input("Zadejte číslo: "))        
        tisk += str(cislo) + "; " # Přídá zadané číslo do tisku
        pocet += 1 # počítá kolik čísel je
        pocetnanovyradek += 1 # Počítá čísla aby fungovalo odřádkování

        if pocetnanovyradek > 3: # Pokud je pocetnanovyradek větší než 3
            tisk += "\n" # Přidá do tisku nový řádek
            pocetnanovyradek = 0 # Vynuluje počítadlo

        soucet += (cislo) # Sčítá všechny zadaná čísla

        if (cislo > maxcislo): # Pokud je číslo větší než zadané číslo
            maxcislo = cislo   # Přepíše se

        if (cislo < mincislo): # Pokud je číslo menší než zadané číslo
            mincislo = cislo   # Přepíše se

        if (cislo < 0): # Pokud je číslo menší než 0 -- Je záporné
            zapornecisla += 1      # Přídá se další číslo do počítadla záporných čísel
            soucetzapor += cislo # Scítá záporná čísla

        otazka = input("Chcete program ukončit? 'a' pro ukončení: ") # Zeptá se co chci udělat
    while(True):
        nabidka = input("1. Výpis čísel; 2. Průměr; 3. Maximální a minimální hodnota; 4. Počet záporných čísel; 5. Součet záporných čísel; 6. Konec programu: ")
        if nabidka == "1":
            print(tisk)
        elif nabidka == "2":
            print("Průměr je: ", soucet/pocet)
        elif nabidka == "3":
            print(f"Minimální hodnota je: {mincislo} a  maximální hodnota je: {maxcislo}")
        elif nabidka == "4":
            print("Počet záporných čísel je: ", zapornecisla)
        elif nabidka == "5":
            print(f"Součet záporných čísel je: {soucetzapor}")
        elif nabidka == "6": # Pokud zadáme 6 tak se program vypíná. Pokud cokoliv jiného tak jede dál
            break
programek()
