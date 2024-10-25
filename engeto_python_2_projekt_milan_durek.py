"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Milan Důrek 
email: m.durek@seznam.cz
discord: arkalik
"""

"""
Dořešit býky
Dořešit chybu při generování náhodných čísel
"""

import random

nahodne_cislo_je_vporadku = int(1)
nahodne_cislo = int()
zadane_cislo = int()
pocet_nul = int(0)
pocet_jednicek = int(0)
pocet_dvojek = int(0)
pocet_trojek = int(0)
pocet_ctyrek = int(0)
pocet_petek = int(0)
pocet_sestek = int(0)
pocet_sedmicek = int(0)
pocet_osmicek = int(0)
pocet_devitek= int(0)
ukoncit_program = int(1)
pocet_pokusu = int(0)
pocet_krav = int(0)
pocet_byku = int(0)

print("Hi there!")
print("-----------------------------------------------")

print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
print("-----------------------------------------------")

nahodne_cislo = random.randrange(1000,9999,1)
# print(str(nahodne_cislo))

while nahodne_cislo_je_vporadku != 0:
    for prvek in str(nahodne_cislo):
        if str(prvek) == str(0):
                pocet_nul = pocet_nul + 1
        elif str(prvek) == str(1):
                pocet_jednicek = pocet_jednicek + 1
        elif str(prvek) == str(2):
                pocet_dvojek = pocet_dvojek + 1
        elif str(prvek) == str(3):
                pocet_trojek = pocet_trojek + 1
        elif str(prvek) == str(4):
                pocet_ctyrek = pocet_ctyrek + 1                                
        elif str(prvek) == str(5):
                pocet_petek = pocet_petek + 1
        elif str(prvek) == str(6):
                pocet_sestek = pocet_sestek + 1
        elif str(prvek) == str(7):
                pocet_sedmicek = pocet_sedmicek + 1
        elif str(prvek) == str(8):
                pocet_osmicek = pocet_osmicek + 1
        else:
             pocet_devitek = pocet_devitek +  1
        if pocet_nul > 1 or pocet_jednicek > 1 or pocet_dvojek > 1 or pocet_trojek > 1 or pocet_ctyrek > 1 or pocet_petek > 1 or pocet_sestek > 1 or pocet_sedmicek > 1 or pocet_osmicek > 1 or pocet_devitek > 1:
                nahodne_cislo = random.randrange(1000,9999,1)
#                print(str(nahodne_cislo))
                nahodne_cislo_je_vporadku = 1
                pocet_nul = int(0)
                pocet_jednicek = int(0)
                pocet_dvojek = int(0)
                pocet_trojek = int(0)
                pocet_ctyrek = int(0)
                pocet_petek = int(0)
                pocet_sestek = int(0)
                pocet_sedmicek = int(0)
                pocet_osmicek = int(0)
                pocet_devitek= int(0)
        else: nahodne_cislo_je_vporadku = 0

while ukoncit_program != 0:
        zadane_cislo = input("Enter a number:")
        pocet_nul = int(0)
        pocet_jednicek = int(0)
        pocet_dvojek = int(0)
        pocet_trojek = int(0)
        pocet_ctyrek = int(0)
        pocet_petek = int(0)
        pocet_sestek = int(0)
        pocet_sedmicek = int(0)
        pocet_osmicek = int(0)
        pocet_devitek= int(0)
        if len(zadane_cislo) < 4:
                print("Zadaný řetězec:",zadane_cislo, "je kratší než 4 znaky. Zadaný řetězec má:", len(zadane_cislo),"znaky. Zadejte prosím nové číslo:")
                continue
        elif len(zadane_cislo) > 4:
                print("Zadaný řetězec:",zadane_cislo," je delší než 4 znaky. Zadaný řetězec má:", len(zadane_cislo),"znaků. Zadejte prosím nové číslo:")
                continue 
        elif str.isnumeric(zadane_cislo) is False:
                print("Zadaný řetězec:",zadane_cislo,"obsahuje nečíselné znaky. Zadejte prosím nové číslo:")
                continue
        elif str(zadane_cislo[0:1]) == str(0):
                print("Zadaný řetězec:",zadane_cislo,"obsahuje nulu na začátku. Zadejte prosím nové číslo:")
                continue
        else: 
                for prvek in str(zadane_cislo):
                        if str(prvek) == str(0):
                                pocet_nul = pocet_nul + 1
                        elif str(prvek) == str(1):
                                pocet_jednicek = pocet_jednicek + 1
                        elif str(prvek) == str(2):
                                pocet_dvojek = pocet_dvojek + 1
                        elif str(prvek) == str(3):
                                pocet_trojek = pocet_trojek + 1
                        elif str(prvek) == str(4):
                                pocet_ctyrek = pocet_ctyrek + 1                                
                        elif str(prvek) == str(5):
                                pocet_petek = pocet_petek + 1
                        elif str(prvek) == str(6):
                                pocet_sestek = pocet_sestek + 1
                        elif str(prvek) == str(7):
                                pocet_sedmicek = pocet_sedmicek + 1
                        elif str(prvek) == str(8):
                                pocet_osmicek = pocet_osmicek + 1
                        else:
                                pocet_devitek = pocet_devitek +  1
                if pocet_nul > 1 or pocet_jednicek > 1 or pocet_dvojek > 1 or pocet_trojek > 1 or pocet_ctyrek > 1 or pocet_petek > 1 or pocet_sestek > 1 or pocet_sedmicek > 1 or pocet_osmicek > 1 or pocet_devitek > 1:
                        print("Zadaný řetězec:",zadane_cislo, "obsahuje 2x stejné číslo. Zadejte prosím nové číslo:")
                        continue
                elif str(nahodne_cislo) == str(zadane_cislo):
                        pocet_pokusu = pocet_pokusu +  1
                        print("Correct, you've guessed the right number in", pocet_pokusu,"guesses!")
                        break
                else: 
                        pocet_pokusu = pocet_pokusu +  1
                        for prvek in str(zadane_cislo):
                                for prvek2 in str(nahodne_cislo):
                                        if str(prvek) == str(prvek2):
                                                pocet_krav = pocet_krav + 1
                        if str(zadane_cislo)[0] == str(nahodne_cislo)[0]:
                                pocet_byku = pocet_byku + 1
                        if str(zadane_cislo)[1] == str(nahodne_cislo)[1]:
                                pocet_byku = pocet_byku + 1                        
                        if str(zadane_cislo)[2] == str(nahodne_cislo)[2]:
                                pocet_byku = pocet_byku + 1
                        if str(zadane_cislo)[3] == str(nahodne_cislo)[3]:
                                pocet_byku = pocet_byku + 1                                

                        print(pocet_byku,"bulls,", pocet_krav,"cows")
                        pocet_krav = int(0)
                        pocet_byku = int(0)
                        continue

                                                   



# ukoncit_program = int(0)
