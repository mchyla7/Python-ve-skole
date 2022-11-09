#
#*     Cykly
#

#
# while(podmínka): -- Dokud je podmínka splněná = opakuje se blok příkazu
#   blok příkazu

# Program bude načítat kladné čísla. Po zadní nekladného se načítání ukončí.
# Následně program načte čísla zobrazí

def cyklus():
    tisk = ""
    a = 1
    while(a > 0):
        a = float(input("Zadejte kladné číslo: "))
        if a > 0:
            tisk=tisk+str(a)    + "; "
    print(tisk)
#cyklus()

def cyklus2():
    tisk = ""
    while(True):
        a = float(input("Zadejte kladné číslo: "))
        if a <= 0: break # Break ukončí cyklus
        tisk=tisk+str(a) + "; "
    print(tisk)
cyklus2()

