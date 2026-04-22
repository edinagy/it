# *******************
# Exercitiul 1
# Creeaza 3 variabile:
# nume
# varsta
# oras
# Atribuie valori si afiseaza-le fiecare pe rand cu print().

# Rezolvare exercitiul 1:

nume = "Nagy"
varsta = "23"
oras = "Oradea"
print(nume)
print(varsta)
print(oras)

# *******************
# Exercitiul 2
# Creeaza variabilele:

# prenume = "Ana"
# an_nastere = 2002
# inaltime = 1.68

# Afiseaza valorile intr-un mod clar, ca in exemplu:
# Prenume: Ana
# An nastere: 2002
# Inaltime: 1.68

# Rezolvare exercitiul 2:

prenume = "Eduard"
an_nastere = 2002
inaltime = 1.74

print("prenume", prenume )
print("an_nastere", an_nastere)
print("inaltime", inaltime)

# *******************
# Exercitiul 3
# Creeaza doua variabile de tip string:
# prenume
# nume_familie
# Afiseaza numele complet folosind concatenare cu +.
# Exemplu rezultat:
# Andrei Popescu

# Rezolvare exercitiul 3:

prenume = "Eduard"
nume_familie = "Nagy"
print(prenume + " " + nume_familie)

# *******************
# Exercitiul 4
# Creeaza variabilele:
# oras = "Timisoara"
# tara = "Romania"
# Afiseaza propozitia:
# Locuiesc in Timisoara, Romania
# Rezolva folosind print() cu virgula intre elemente.

# Rezolvare exercitiul 4:

oras = "Timisoara"
tara = "Romania"
print("Locuiesc in", oras + ",", tara)

# *******************
# Exercitiul 5
# Creeaza variabilele:
# nume = "Maria"
# varsta = 22
# Afiseaza propozitia:
# Maria are 22 ani
# Rezolva prin concatenare cu +, deci trebuie sa folosesti si str().

# Rezolvare exercitiul 5:

nume = "Maria"
varsta = 22
print(nume + " are " + str(varsta) + " ani ")

# *******************
# Exercitiul 6
# Refa exercitiul 5, dar de data aceasta folosind f-string.

# Rezolvare exercitiul 6:

nume = "Maria"
varsta = 22
print(f"{nume} are {varsta} ani")

# *******************
# Exercitiul 7
# Refa exercitiul 5, dar de data aceasta folosind .format().

# Rezolvare exercitiul 7:

nume = "Maria"
varsta = 22
print("{} are {} ani".format(nume, varsta))

# *******************
# Exercitiul 8
# Creeaza 4 variabile:
# produs = "lapte"
# pret = 8.5
# cantitate = 2
# magazin = "Lidl"
# Afiseaza o propozitie la alegere care sa contina toate aceste informatii.
# Exemplu:
# Am cumparat 2 bucati de lapte din Lidl la pretul de 8.5 lei

# Rezolvare exercitiul 8:

produs = "lapte"
pret = 8.5
cantitate = 2
magazin = "Lidl"

print(f"Am cumparat {cantitate} sticle de {produs} de la {magazin}, la pretul de {pret} lei bucata.")

# *******************
# Exercitiul 9
# Creeaza un mini-cartonas de prezentare cu:
# nume
# varsta
# oras
# ocupatie
# Afiseaza totul pe mai multe linii folosind \n.

# Rezolvare exercitiul 9:

nume = "Eduard"
varsta = 23
oras = "Oradea"
ocupatie = "Student"

print("Cartonas de prezentare:\n")
print("Nume:", nume)
print("Varsta:", varsta)
print("Oras:", oras)
print("Ocupatie:", ocupatie)

# *******************
# Exercitiul 10
# Scrie un text pe mai multe randuri folosind triple quotes """ """.

# Rezolvare exercitiul 10:

text = """Pe mine ma cheama
Nagy Eduard
si imi doresc 
sa invat Python
iar dupa sa invat
CyberSecurity"""
print(text)

# *******************
# Exercitiul 11
# Creeaza variabilele:
# zi = "luni"
# temperatura = 23.5
# Afiseaza propozitia:
# Astazi este luni si sunt 23.5 grade afara
# Fa exercitiul in 2 variante:
# cu f-string
# cu .format()

# Rezolvare exercitiul 11:

zi = "luni"
temperatura = 23.5
print(f"Astazi este {zi} si sunt {temperatura} grade afara")

zi = "luni"
temperatura = 23.5
print("Astazi este {} si sunt {} grade afara".format(zi, temperatura))

# *******************
# Exercitiul 12
# Creeaza variabile pentru 3 colegi:
# coleg1
# coleg2
# coleg3
# Afiseaza propozitia:
# In grupa mea sunt: X, Y si Z

# Rezolvare exercitiul 12:

coleg1 = "Cristina"
coleg2 = "Sergiu"
coleg3 = "Bianca"
print(f"In grupa mea sunt: {coleg1}, {coleg2}, {coleg3}")

# *******************
# Exercitiul 13
# Creeaza variabilele:
# marca = "Audi"
# model = "A4"
# an = 2007
# Afiseaza:
# Masina mea este un Audi A4 din anul 2007
# Foloseste concatenare cu +.

# Rezolvare exercitiul 13:

marca = "Audi"
model = "A4"
an = 2007

print("Masina mea este un " + marca + " " + model + " din anul " + str(an))

# *******************
# Exercitiul 14
# Creeaza 3 variabile booleene:
# are_tema
# este_prezent
# a_invatat_python
# Atribuie valori True sau False si afiseaza-le.
# Exemplu:
# Are tema: True

# Rezolvare exercitiul 14:

are_tema = True
este_prezent = False
a_invatat_python = True

print("Are tema:", are_tema)
print("Este prezent:", este_prezent)
print("A invatat Python:", a_invatat_python)

# *******************
# Exercitiul 15
# Creeaza urmatoarele variabile:
# nume = "Florin"
# job = None
# salariu = 5000
# Afiseaza-le pe toate si observa cum se afiseaza valoarea None.

# Rezolvare exercitiul 15:

nume = ("Florin")
job = ("None")
salariu = 5000

print("Nume:", nume)
print("Job:", job)
print("Salariu:", salariu)

# *******************
# Exercitiul 16
# Creeaza variabilele:
# materie1 = "Python"
# materie2 = "SQL"
# materie3 = "Testing"
# Afiseaza un “orar” pe mai multe linii folosind \n.

# Rezolvare exercitiul 16:

materie1 = "Python"
materie2 = "Sql"
materie3 = "Testing"

print("Orarul meu:\n" + materie1 + "\n" + materie2 + "\n" + materie3)

# *******************
# Exercitiul 17
# Creeaza variabilele:
# prenume = "Ioana"
# varsta = 19
# inaltime = 1.72
# este_elev = True
# Afiseaza toate informatiile intr-o singura propozitie, folosind f-string.

# Rezolvare exercitiul 17:

prenume = "Ioana"
varsta = 19
inaltime = 1.72
este_elev = True

print(f"{prenume} are {varsta} ani, are inaltimea de {inaltime} si este elev: {este_elev}")

# *******************
# Exercitiul 18
# Creeaza doua variabile string:
# cuvant1 = "Hello"
# cuvant2 = "Python"
# Afiseaza:
# cele doua cuvinte separate prin spatiu
# cele doua cuvinte pe linii diferite

# Rezolvare exercitiul 18:

cuvant1 = "Hello"
cuvant2 = "Python"

print(cuvant1 + " " + cuvant2)

print(cuvant1 + "\n" + cuvant2)

# *******************
# Exercitiul 19
# Creeaza variabilele:
# nume_film
# an_aparitie
# nota
# Afiseaza o propozitie de forma:
# Filmul X a aparut in anul Y si are nota Z
# Rezolva in 3 moduri:
# cu virgula in print()
# cu f-string
# cu .format()

# Rezolvare exercitiul 19:

nume_film = "The Hobbit: The Desolation of Smaug"
an_aparitie = 2013
nota = 7.8

print("Filmul", nume_film, "a aparut in anul", an_aparitie, "si are nota", nota)
print(f"Filmul {nume_film} a aparut in anul {an_aparitie} si are nota {nota}")
print("Filmul {} a aparut in anul {} si are nota {}".format(nume_film, an_aparitie, nota))

# *******************
# Exercitiul 20
# Fa o descriere completa despre tine sau despre o persoana inventata, folosind:
# minimum 6 variabile
# cel putin un int
# cel putin un float
# cel putin un bool
# text afisat pe mai multe linii
# cel putin o propozitie cu f-string

# Rezolvare exercitiul 20:

nume = "Eduard"
varsta = 23
inaltime = 1.74
oras = "Oradea"
ocupatie = "Student"
are_animale = True
hobby = "Gaming"

print(f"Numele meu este {nume} si am {varsta} ani.\n"
      f"Locuiesc in {oras} si sunt {ocupatie}.\n"
      f"Am inaltimea de {inaltime}.\n"
      f"Imi place {hobby}.\n"
      f"Am animale de companie? {are_animale}.")