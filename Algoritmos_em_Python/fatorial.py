"""
Calcular o fatorial de um número


fat de 0 = 0! = 1

fat de 1 = 1! = 1



"""

num = int(input("Informe um número:"))



fat = 1

cont = 0


while cont < num:
    if num == 0:
        fat = 1
    else:
        fat *= (num-cont)

        cont = cont + 1


print(fat)
    
