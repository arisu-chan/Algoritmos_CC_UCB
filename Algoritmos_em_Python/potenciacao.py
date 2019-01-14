"""
Potenciacao

Multiplicar uma base tantas vezes quantas forem o expoente
"""

base = int(input("Informe a base:"))
exp = int(input("Informe o expoente:"))


mult = 1

cont = 0


while cont < exp:
    mult = base*mult
    cont = cont + 1


print(mult)
