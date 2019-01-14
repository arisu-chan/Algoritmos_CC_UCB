print("###########################")
print("#                         #")
print("#                         #")
print("#                         #")
print("#    Dia da Semana        #")
print("#    by Lucas Correia     #")
print("#                         #")
print("#                         #")
print("#                         #")
print("#                         #")
print("###########################")


dia = int(input("Digite o dia da semana:"))

if(dia < 0 | dia > 7):
    print("Esse dia não existe!")
elif dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terca")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
else:
    print("Sabado")
