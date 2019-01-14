"""
Calcular o peso ideal de uma pessoa

"""


print("#############################################")

altura = float(input("Informe a sua altura:"))

sexo = input("Digite o sexo:")

if(sexo!='m' and sexo!='f'):
    print("Opcao invalida")
else:
    if sexo == 'm':
        print("Sua peso ideal = ", (72.7*altura)-58)        
    else:
        print("Seu peso ideal =  ", (62.1*altura) - 44.7)




print("##############################################")
