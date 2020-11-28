#!/usr/bin/env python
"""
Met dit rekenmachine kan je optellen,aftrekken,vermenigvuldigen en delen door 2 getallen te kiezen
bron : https://www.youtube.com/watch?v=HOqTyB9GzHA
"""


__author__ = "Sven De Visscher"
__email__ = "sven.devisscher@student.kdg.be"
__status__ = "Development"


# Deze functie telt 2 getallen op
def optellen(x, y):
    return x + y

# Deze functie trekt 2 getallen van elkaar af
def aftrekken(x, y):
    return x - y

# Deze functie vermenigvuldigt 2 getallen
def vermenigvuldigen(x, y):
    return x * y

# Deze functie deelt 2 getallen door elkaar
def delen(x, y):
    return x / y

print("Select operation.")
print("1.Optellen")
print("2.Aftrekken")
print("3.Vermenigvuldigen")
print("4.Delen")

while True:
    # Vraagt input aan de gebruiker
    keuze = input("Enter choice(1/2/3/4): ")

    # Bekijkt of de keuze één van de 4 opties is
    if keuze in ('1', '2', '3', '4'):
        num1 = float(input("Typ het eerste getal: "))
        num2 = float(input("Typ het 2de getal: "))

        if keuze == '1':
            print(num1, "+", num2, "=", optellen(num1, num2))   # Telt de 2 getallen op

        elif keuze == '2':
            print(num1, "-", num2, "=", aftrekken(num1, num2))   # Trekt de 2 getallen af

        elif keuze == '3':
            print(num1, "*", num2, "=", vermenigvuldigen(num1, num2))   # Vermenigvuldigd de 2 getallen

        elif keuze == '4':
            print(num1, "/", num2, "=", delen(num1, num2))  # Deelt de 2 getallen door elkaar
        break
    else:
        print("Ongeldige input")    # Zegt dat je een ongeldig getal hebt ingevoerd.

