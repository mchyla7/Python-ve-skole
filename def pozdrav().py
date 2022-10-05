def pozdrav():
    print("hello world")
#pozdrav()

#program mi napíše Hello World



#* Datové tipy
#  integer - celočíselný datový typ
#  float - desetiný datový typ
#  string - textový datový typ
#  bool - logický datový typ, může být nabýt dvou hodnot True/False

#* Proměnná
#  Je to místo v paměti počítače, které má:
#                                         1.NÁZEV 
#                                         2.DATOVÝ TYP 
#                                         3.OBLAST PLATNOSTI


def soucet2cisel():
   a = float(input("Zadej první hodnotu: "))
   b = float(input("Zadej druhou hodnotu: "))
   soucet = a + b
   print("Jsi nejlepší protože jsi udělal kalkulačku a výsledek je:" ,soucet)
#soucet2cisel()





# Program nacte strany obdelníku 
# Program zobrazí jeho obsah a obvod

def obdelnik():
    a = float(input("Zadej první stranu : "))
    b = float(input("Zadej druhou stranu: "))
    obsah = a * b
    obvod = 2 * (a + b)
    print("Obsah je:" ,obsah, "Obvod je:" ,obvod)
#obdelnik()






# S tím že se zbavím dvou řádku

# Program na výpočet obsahu a obvodu obdelníku

def obdelnik():
    a = float(input("Zadej první stranu : "))
    b = float(input("Zadej druhou stranu: "))
    print("Obsah je:" ,a+b, "Obvod je:" ,2*(a+b))   # A vložím obsah = (a*b) a obvod (2*(a+b)) do printu
#obdelnik()




# Program načte tři hodnoty a zobrazí jejich průměr

def prumer():
    a = float(input("Zadej první hodnotu: "))
    b = float(input("Zadej druhou hodnotu: "))
    c = float(input("Zadej třetí hodnotu: "))
    print("Průměr je: " ,(a+b+c)/3)   # vložím zadání do printu
#prumer()


#     "\n" ----- Tohle je nový řádek





def prumer2():
    a = float(input("Zadej první hodnotu: "))
    b = float(input("Zadej druhou hodnotu: "))
    c = float(input("Zadej třetí hodnotu: "))
    tisk = "➗| Průměr je: " + str((a+b+c)/3)
    tisk = tisk + "\n"
    tisk = tisk + "➕| Součet je  " + str(a+b+c)
    print(tisk)   # vytiskne všechny tři printy
#prumer2()






#Program načte jméno a věk první osoby
#Následně načte jméno a věk druhé osoby
#Program na jednom řádku vypíše jméno1 + věk1 + jméno2 + věk2
#Na dalším řádku zobrazí průměrný věk.


def jmeno_a_vek():
    jmeno1 = str(input("První jméno: "))
    vek1 = float(input("První věk: "))
    jmeno2 = str(input("Druhé jméno: "))
    vek2 = float(input("Druhý věk: "))
    tisk = "Jméno: " + str(jmeno1) + " | Věk: " + str(vek1)
    tisk = tisk + "\n            ❤"
    tisk = tisk + "\nJméno: " + str(jmeno2) + " | Věk: " + str(vek2) 
    print(tisk)
    print("Průměrný věk je: ", + (vek1 + vek2)/2)
#jmeno_a_vek()



# součet a součin
# mocnina prvního a druhého čísla

def mocniny():
    a = float(input("První číslo: "))
    b = float(input("Druhé číslo: "))
    vysledek = "\nSoucet: " + str(a+b)
    vysledek = vysledek +   "\nSoučin:: " + str(a*b)
    vysledek = vysledek +   "\nMocnina prvního čísla: " + str(a*a)
    vysledek = vysledek +   "\nMocnina druhého čísla: " + str(b*b)
    print(vysledek)
mocniny()
