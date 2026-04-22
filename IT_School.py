import random
# Compilator - Un program care traduce codul sursa scris de programator intr o forma executabila pentru calculator
# Ex: C/ C++

# Interpretor - Un program care citeste si executa codul pas cu pas
# 1. Noi scriem codul Python
# 2. Interceptorul Python il citeste
# 3. Il executa

# print("Salut") # Pasul 1
# print("Astazi invatam python") # Pasul 2
# print("Aceasta este prima lectie") # Pasul 3
#
# print(10)
# print(3.14)
# print(2+3)
# print(10-4)
# print(5 * 2)
# print(23456*29484)

# nume = "Ana"
# print(nume)

# varsta = 25
# print(varsta)
# varsta = 27
# print(varsta)

# print(type(nume))
# print(type(varsta))

# Sintaxa reprezinta regulile dupa care se scrie cod intr un limbaj de programare

#recapitulare
# Variabila - este un loc din memorie in care stocam o valoare
# Exemple:

# # semnul " = " -> pune valoarea din dreapta in variabila din stanga
# # print() -> afiseaza informatii pe ecran
# # Exemplu:
#
# # print("Salut")
# # print(10)
#
# # De ce folosim print?
# # 1. Afisam informatii pe ecran
# # 2. Afisam valori numerice
# # 3. Afisam variabile
# # 4. Verificam daca programul face ceea ce ne asteptam
#
# # Exemplu:
# print("Florin")
# nume = "Ana"  # stocheaza un text
# varsta = 20  # stocheaza un numar intreg
# inaltime = 1.60  # stocheaza un numar zecimal

# print(nume, varsta) # Python pune automat spatiu intre ele atunci cand sunt separate prin virgula

# Putem afisa si text si variabile
# print("Numele meu este:", nume)

# Mai multe moduri de afisare cu print()
# Varianta 1 -cu virgula in print()
# nume = "Maria"
# varsta = 22
#
# print("Numele este", nume)
# print("Varsta", varsta)

# Varianta 2 - cu + intre stringuri

# prenume = "Ion"
# nume_familie = "Popescu"
#
# print(prenume + " " + nume_familie) # " " -> un string care contine un spatiu, pentru a separa prenumele de numele de familie
# # + -> lipeste textele (in cazul nostru, nume si prenume_familie)
# # cu +, ambele parti trebuie sa fie stringuri(variabile prenume si nume_familie in cazul noostru)
#
# # Ok
# oras = "Timisoara"
# print("Locuiesc in " + oras)
#
# # NOK
# varsta = 25
#
# # Varianta corectata
# print("Am" + str(varsta) + " ani")# str() -> converteste un numar intr-un string
#
# # Varianta 3 - cu f-string / cu acolade {}
# nume = "Andrei"
# varsta = 21
#
# print(f"Numele meu este {nume} si am {varsta} ani")
# # litera f inainte de string spune ca in interior vom pune variabile
# # variabilele se scriu intre acolade {}
#
# # Varianta 4 - cu metoda format()
# nume = "Elena"
# varsta = 20
#
# print("Ma numesc {} si am {} ani".format(nume, varsta))

# Exercitiu 1 -> Creaza o variabila nume si afiseaza

# nume = "Eduard"
# print(nume)
#
# # Exercitiu 2 -> Creaza 2 variabile nume si oras, apoi afiseaza pe aceeasi linie
#
# nume = "Eduard"
# oras = "Oradea"
# print(f"{nume} din {oras}")
# print(nume + " din " + oras)
# print(nume, oras)
# text = ' d'
# print(len(text))

# Tipuri de date in Python
# 1. String (text) - se scrie intre ghilimele
# Un tip de date arata ce fel de valoare avem intr o variabila
# un nume este text
# o varsta este numar intreg
# o inaltime este un numar zecimal/float
# o valoare de tip da/nu poate fi adevarata sau falsa

# python trebuie sa stie ce fel de informatie pastreaza, pentru ca fiecare tip de date se comporta diferit

# 1. str - string - text
# string reprezinta textul
# Exemple
# nume = "Ana"
# oras = "Cluj"
# mesaj = "Salut"
# a = "Python"
# b = 'curs'
# # Observatie: Chiar daca scriem cifre intre ghilimele, ele vor fi tot considerate tot text - Ex: "123" este un string, nu un numar
# # Triple quotes - pentru stringuri care contin mai multe randuri
#
# """
# Acesta este un comentariu
# care contine mai multe randuri
# """
#
#
#
# text = """Acesta este un text
#                       care contine mai multe randuri
# si se scrie intre triple quotes"""

# print(text)
 # Diferenta dintre " " si """ """
 # cu ghilimele normale scriem de obicei texte pe o singura linie
 # cu ghilimele triple putem scrie texte mai lungi, pe mai multe linii

 # \n - newline - trece la randul urmator

# print("Salutare\nBine ai venit\nLa curs") # textul scris intr o singura linie de cod, dar la afisare apare pe mai multe linii
# print("Meinu:\n1. Pizza\n2. Paste\n3. Sucuri")

# Int - integer - numar intreg - numere fara zecimale

# varsta = 25
# an = 2026
# numar_persoane = 15
#  # float - numar zecimal
# inaltime = 1.75
# pret = 19.99
# temperatura = 15.5
#In python, zecimalele se scriu cu punct, nu cu virgula
# print(15.5) #OK
# print(15,5 + 2) #NOK

# bool - boolean - adevarat sau fals
# acest tip de date are doar doua valori: True (adevarat) sau False (fals)

# invata_python = True
# este_ziua_mea = False
#
# variabila = None

# x = "25"
# y = int(x)
# # print(x + 5)
# print("10" + "5")
# print(10 + 5)
#
# x = "19.99"
# print(type(x))
# decimal = float(x)
# print(type(decimal))
#
# # operatori aritmetici
# # simboluri folosite pentru calculele matematice
#
# # + -> adunare
# # - -> scadere
# # * -> inmultire
# # / -> impartire
# # ** -> ridicare la putere
# # // -> impartire intreaga
# # % -> restul impartirii
#
# # Adunare
# a = 10
# b = 5
# suma = a + b
# print(suma)
#
# # Scadere
# diferenta = a - b
# print(diferenta)
#
# # Inmultire
# produs = a * b
# print(produs)
#
# # Impartire
# cat = a / b
# print(int(cat))
#
# # : 2.f -> se foloseste ca sa afisam un numar zecimal cu exact 2 cifre dupa virgula
# # f vine de la float
# # .2 insemana 2 zecimale
#
# rezultat = 10 / 3
# print(rezultat)
# print(f"{rezultat:.4f}")
# # important:   :.2f nu schimba valoarea, doar modul de afisare
#
# #impartirea intreaga
# print(10 // 3)
# # pentru ca 10 impartit la 3 este 3.333.. iar // pastreaza doar intreaga, adica 3
#
# # restul impartirii
# print(10 % 3)
# print(8 % 2)
# # daca restul este 0, numarul este divizibil cu 2
# # util pentru a verifica daca un numar este par sau impar
#
# # puterea
# print(2 ** 3)
# print(5 ** 2)
#
# # Ordinea operatiilor
# # in Python se respecta ordinea matematica a operatiilor
# print(2 + 3 * 4) # inmultirea se face inaintea adunarii
#
# # in matematica = inseamna egalitate
# # in programare = inseamna atribuire
# x = 10 # x primeste valoarea 10 -> pune valoarea 10 in variabila x
#
# # input()- cum citim date de la utilizator
# # input este o functie care permite utilizatorului sa scrie ceva de la tastatura
#
# nume = input("Cum te numesti? ")
# print(nume)
#
# # 1. programul afiseaza mesajul cum te numesti?
# # 2. utilizatorul scrie ceva
# # 3. valoarea introdusa este salvata in variabila nume
#
# # input() -> returneaza inttodeauna text
# varsta = input("Cati ani ai?\n ")
# print(varsta)
# print(type(varsta))

# varsta =  int(input("Cati ani ai?\n"))
# print(varsta)
# print(type(varsta))
#
# inaltime = float(input("Ce inaltime ai?\n"))
# print(inaltime)
# print(type(inaltime))

# numar1 = input("Primul numar: ")
# numar2 = input("Al doilea numar: ")
#
# print(numar1 + numar2)
#
# numar1 = int(input("Primul numar: "))
# numar2 = int(input("Al doilea numar: "))
#
# print(numar1 + numar2)

# GRESELI FRECVENTE
#nume = Ana -> corect: "Ana" ; variabila de tip string/text trebuie sa fie intre ghilimele
#inaltime = 1,75 -> corect: 1.75 ; in python foloseste punctul pentru zecimale

# cand unesti text cu un numar fara conversie
# varsta = 20
# print("Am " + str(varsta)+ " ani") # TREBUIE SA CONVERTIM VARIABILA VARSTA LA STRING PENTRU A PUTEA LIPI/CONCATENA TEXTUL

#input() returneaza intotdeauna text/string - >ai nevoie sa faci conversie la tipul de date dorit (int, float etc)

# se confunda / cu //
# / -> rezultatul decimal
# // -> doar cu partea intreaga

# Exercitii

# 1. Citeste de la tastatura numele utilizatorului si afiseaza un mesaj : "Bun venit la curs, X"

# 2. Citeste de la tastatura 2 numere intregi si afiseaza suma lor

# numar_1 = int(input("numar_1:"))
# numar_2 = int(input("numar_2:"))

# suma= numar_1 + numar_2
#
# print(f"Suma numerelor este {suma}")

#3. Citeste de la tastatura 2 numere intregi si afiseaza suma, scaderea, inmultirea si impartirea

# suma= numar_1 + numar_2
# print(f"Suma numerelor este {suma}")
#
# diferenta = numar_1 - numar_2
# print(f"Diferenta numerelor este {diferenta}")
#
# produs = numar_1 * numar_2
# print(f"Produs numerelor este {produs}")
#
# cat = numar_1 / numar_2
# print(f"Catul numerelor este {cat}")

# 4. Citeste varsta si afiseaza peste 5 ani vei avea x ani

# varsta = int(input("Varsta este:"))
# varsta_viitoare = varsta + 5
# print(f"Peste 5 ani voi aveea {varsta_viitoare}")

#5. Citeste un pret si o cantitate si calculeaza costul final

# pret = float(input("Pretul este:"))
# cantitate = int(input("Cantitati este:"))
#
# cost_final = pret * cantitate
#
# print(f"Costul total platit va fi {cost_final:.1f}")


# 6. <= -. mai mic sau egal
# a <= b -> False

#Operatori logici

# 1. AND -> ambele conditii trevuie sa fie True / Adevarate
# 2. OR -? cel putin una din conditii trebuie sa fie True
# 3. NOT -> inverseaza valoarea - True -> False\


# x = 5
#
# if x == 5:
#     print("x este egal cu 5")

# 2.  Diferit de - !=
# if x != 10:
#     print("x NU este egal cu 10")

# 3. Mai mare decat - >
# temperatura = 30
#
# if temperatura > 25:
#     print("afara e cald")

#4. Mai mic decat - <
# elevi = 18
#
# if elevi < 19:
#     print("Clasa este mica")

# 5. Mai mare sau egal
# varsta = 18
#
# if varsta >= 18:
#     print("Ai voie sa votezi")

# 6. Mai mic sau egal
# pret = 99

# if pret <= 99:
#     print("Produsul este ieftin")

# 1. AND
# varsta = 20
# nationalitate = ("roman")
#
# if varsta > 18 and nationalitate == "roman":
#     print("Poti vota in Romania")
# else:
#     print("Nu poti vota in Romania")

# 2. OR
# zi = "sambata"
#
# if zi == "sambata" or zi == "duminica":
#     print("este weekend")

# 3. NOT
# ploua = False
#
# if not ploua:
#     print("Vremea este frumoasa")

# if not x -> aceasta este o verificare de tip "falsy". Python interpreteaza valoarea "x" in contextul de adevar sau fals
# if x: verifica daca x este adevarat (Truthy)
# if not x: verifica daca x este fals (Falsy)

# Ce valori sunt considerate falsy in Python
# Toate vor face ca not x sa fie True, adica sa execute codul din interiorul if
"""
1.None
2.False
3. 0 (orice numar 0)
4. ''/"" -> sir gol
5.[] -. lista goala
6.{} -> dictionar gol
7. set() -> set gol
8. () -> tuplu gol

5,6,7,8 -. colectii de date
"""

# Exemple concrete
# x = 0
# print(bool(x))
# print(not x)
# if not x:
#     print("Este zero")
#
# x = ''
# if not x:
#     print("String gol")
#
# x = [1, 2, 3]
# if not x:
#     print("Lista este goala") # NU se va afisa, lista contine elemente

# Alte modalitati de a scrie if

# 1. if pe o singura linie

# x = 3
# if x % 2 != 0: print("Numar impar")

# 2. if termar(pe o singura linie - inlocuieste if/else)
# x = 7

# rezultat = "Par" if x % 2 == 0 else "Impar"
# print(rezultat)

# if x % 2 == 0:
#     rezultat = "Par"
# else:
#     rezultat = "Impar"
# print(rezultat)


# 3. if cu in (verificare apartenenta)
# litera = 'b'
# if litera in "aeiou":
#     print("Este vocala")
# else:
#     print("Este consoana")

# 4. if cu bool() (conditie implicita)
# nume = "Maria"
#
# if nume:
#     print("Ai introdus un nume")

# 5. if comparativ cu mai multe valori
# x = 7
#
# if 5 < x < 10:
#     print("x este intre 5 si 10")

# Nested if - if in interiorul altui if - folosit pentru mai multe niveluri de verificare
# varsta =  int(input("Introdu varsta ta: "))
#
# if varsta >= 18:
#     print("esti adult")
#
#     if varsta >= 65:
#         print("Esti pensionar")
#     else:
#         print("Inca muncesti")
#
# else:
#     print("Esti minor")

# Exercitii:

# 1. Citeste un numar de la tastatura sau introdu un numar de la tastatura

# numar = int(input("Introdu numar: "))
#
# if numar % 2 == 0:
#     print("Par")
# else:
#     print("Impar")


# 2. Afiseaza daca un numar introdus este pozitiv / negativ sau zero

# numar_1 = int(input("Valoare:"))
#
# if numar_1 == 0 :
#     print("Este zero")
# elif numar_1 > 0:
#     print("Pozitiv")
# else:
#     print("Negativ")

# 3.Verifica daca un numar introdus de la tastatura este intre 1 si 100, inclusiv

# numar_2 = int(input("Introdu un numar: "))
#
# if numar_2 > 1 and numar_2 <= 100:
#     print("In interval")
# else:
#     print("Inafara intervalului")
#
# if 1 < numar_2 <= 100:
#     print("In interval")
# else:
#     print("Inafara intervalului")

# 4. Daca temperatura este sub 0 - ger; intre 0-15 - frig; intre 16-25 - placut; peste 25 - cald

# temperatura = int(input("Mentioneaza temperatura de afara: "))
#
# if temperatura < 0:
#     print("Ger")
# elif temperatura >= 0 and temperatura <= 15:
#     print("Frig")
# elif temperatura >= 16 and temperatura <= 25:
#     print("Placut")
# elif temperatura > 25:
#     print("Cald")
# else:
#     print("De ce?")



# Ce este WHILE in Python
# - Instructiunea WHILE este o structura de control care executa un bloc de cod atata timp cat o conditie este adevarata

# Sintaxa
# while conditie:
    # bloc de cod executat daca "conditie" este true

# Exemplu
# x = 0
# while x < 5:
#     print(x)
#     x += 1

# 1.Conditia trebuie sa se schimbe
# x = 0
# while True:
#     print("bunica mea")
#     x += 1
#     if x == 30:
#         break

# Daca nu modifici variablele din conditie, vei crea o bucla infinita / loop infinit

# 2. Comanda BREAK
# x = 0
# while True:
#     print("aragaz")
#     x += 1
#     if x == 30
#         break

# 3. Comanda CONTINUEA
# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x)

# 4. else in while
# x = 0
# while x < 3:
#     print(x)
#     x += 1
#  else:
#     print("WHILE s a terminat in mod normal")

# Se executa doar daca bucla se incheie in mod normal (fara BREAK)

# Cazuri de utilizare

# 1. Numarare
# x = 10
# while x > 0:
#     print(x)
#     x -= 1

# 2. Asteptare pana la o conditie
# conditie = ""
# while conditie != "exit":
#     conditie = input("Scrie 'exit' pentru a iesi: ")

# 3. Valoare input
# valoare = int(input("Introdu un numar pozitiv:"))
# while valoare <= 0:
#     valoare =  int(input("Numar invalid. Reincearca: "))

# while True cu break
# while True:
#     comanda = input("Comanda: ")
#     if comanda == "stop":
#         break
#     print("Ai tastat:", comanda)

# Blocul try / execpt
# Folosit pentru gestionarea execptiilor(pentru a prinde si trata erori care pot aparea in timpul rularii unui program) fara ca acesta sa se opreasca brusc
# In loc sa crape programul, try/execpt permite sa tratezi aceste situatii controlat

# Sintaxa
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Nu poti imparti la zero")

# Exemplu:
# try:
#     numar = int(input("Introdu un numar: "))
#     print("Numarul este: ", numar)
# except ValueError:
#     print("Nu ai introdus un numar valid")
# numar = int(input("Introdu un numar: "))
# print("Numarul este: ", numar)

# Fara try/except - va afisa eroarea "ValueError"
# numar = int(input("Introdu un numar: ")
# print("Numarul este: ", numar)

# Ce se intampla daca nu specifici nimic
# try:
#     x = 1 / 0
# except:
#     print("A aparut o eroare")

# 1.Generare de numere prime
# numar = 2 # numarul pe care il verificam
# while numar <= 20: # cat timp numarul curent este mai mic sau egal cu 20, repeta instructiunile
#     divizor = 2 # variabila cu care incercam sa impartim numarul
#     prim = True # Am pus True la inceput pentru ca presupunem ca numarul este prim
#     while  divizor < numar: # Cat timp divizorul este mai mic decat numarul, verifica daca numarul se imparte exact la acel divizor
#         if numar % divizor == 0: # Verifica daca se divide exact. Daca se indeplineste, inseamna ca numar se divide exact la divizor
#             prim = False # numarul nu mai este prim
#             break # oprim imediat bucla INTERIOARA
#         divizor += 1 # daca nu s a impartit exact, trecem la urmatorul divizor
#     if prim: # daca variabila prim este inca True, inseamna ca nu am gasit niciun divizor
#         print(numar)
#     numar += 1 # dupa verificare, trecem la urmatorul numar

# Ghiceste numarul - varianta fara modulul RANDOM
# numar_secret = 7
# ghicire = None
# while ghicire != numar_secret:
#     ghicire = int(input("Ghiceste numarul: "))
# print("Ai ghicit")

# Ghiceste numarul = varianta cu modulul RANDOM
# numar_secret = random.randint( 1, 30 )
# ghicire = None
# incercari = 0
# incercari_maxime = 5
#
# while ghicire != numar_secret and incercari <= incercari_maxime:
#     try:
#         ghicire = int(input("Ghiceste numarul(1 - 10). Ai 3 incercari: "))
#         incercari += 1
#         if ghicire < numar_secret:
#             print("Numarul este mai mare")
#         elif ghicire > numar_secret:
#             print("Numarul este mai mic")
#     except ValueError:
#         print("Introdu un numar valid")
#         continue
# if ghicire == numar_secret:
#     print(f"Ai ghicit din {incercari} incercari")
# else:
#     print(f"Ai pierdut, numarul era {numar_secret}")

# Exercitiu:
# Simulator bancomat
# Avem un sold initial de 1000 LEI. Vrem sa fisam un meniu:
# 1. Vezi sold
# 2. Depune bani
# 3. Retrage bani
# 4 Iesire
# Reguli:
# 1.Meniul trebuie repetat pana cand userul alege iesirea
# 2. La retragere, nu ai voie sume mai mari decat soldul
# 3. Fara sume negative sau zeri
# 4. Dupa fiecare operatie afisezi soldul nou

sold = 1000.0
aplicatia_ruleaza = True

while aplicatia_ruleaza:
    print("\n**** MENIU ****")
    print("1. Vezi sold")
    print("2. Depunde bani")
    print("3. Retrage bani")
    print("4. Iesire")
    print("***************\n")

    optiune = input("Alege o optiune (1-4): ")

    if optiune == "1":
        print(f"Soldul curect este: {sold:.2f} LEI")
    elif optiune == "2":
        suma_text = input("Introdu suma pe care vreo sa o retragi: ")
        try:
           suma = float(suma_text)
           if suma <= 0:
               print("Suma introdusa trebuie sa fie mai mare decat 0")
           else:
               sold = sold + suma
               print(f"Ai depus {suma:.2f} LEI")
               print(f"Noul sold este {sold:.2f} LEI")
        except ValueError:
            print("valoare invalida. Introdu un numar valid")


































