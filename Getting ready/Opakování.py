# Program se zeptá na počet čísel, následně je vygeneruje ✅
# Poté se zeptá co chceme zobrazit
# Použíjte cyklus for ✅
# Následně zobrazí počet kladných čísel a počet záporných čísel ✅
# Program následně zobrazí největší a nejmenší číslo ✅
# Opravit chyby - Program nespadne když zadám písmeno ✅

import random

def ucimse():
   tisk = ""
   maxc = -9999999
   minc =   9999999
   kladne = 0
   zaporne = 0
   while(True):
      try:
            pocetCisel = int(input("Zadejte počet čísel: "))
            break
      except:
            print("Nezadal jsi číslo")

   for i in range(pocetCisel):
      cislo = random.randint(-10000,10000)
      tisk += str(cislo) + "; "

      if (cislo > maxc):
         maxc = cislo
      if (cislo < minc):
         minc = cislo
      if (cislo > 0):
         kladne += 1
      if (cislo < 0):
         zaporne += 1


   while(True):
         otazka = input("\n 1. Zobrazit čísla;   2. Zobrazit největší a nejmenší číslo;    3. Zobrazit počet kladných a záporných čísel;    4. Ukončit program   : " )
         if otazka == "1":
            print("\n", tisk)
         if otazka == "2":
            print(f"\n Nejmenší číslo je {minc} a největší číslo je {maxc}")
         if otazka == "3":
            print(f"\n Počet kladných čísel je {kladne} a počet záporných je {zaporne}")
         if otazka == "4":
            break
ucimse()