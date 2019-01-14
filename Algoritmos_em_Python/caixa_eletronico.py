print("###########################")
print("#                         #")
print("#                         #")
print("#                         #")
print("#    Caixa eletrônico     #")
print("#    Saque                #")
print("#    Saldo                #")
print("#                         #")
print("#                         #")
print("#                         #")
print("###########################")


valor_sacar = int(input("Digite o valor a sacar:"))


notasCem = valor_sacar // 100

notasCinq = (valor_sacar % 100)//50


notasDez = (valor_sacar % 100) % 50//10

notasCinco = (valor_sacar % 100) % 50 % 10//5

notasUm = (valor_sacar % 100) % 50 % 10 % 5//1


if 10<= valor_sacar<=600:
    if notasCem > 0:
        print("Quantidade de notas de 100:", notasCem)
    if notasCinq > 0:
        print("Quantidade de notas de 5:", notasCinq)
    if notasDez > 0:
        print("Quantidade de notas de 10:", notasDez)
    if notasCinco > 0:
        print("Quantidade de notas de 1:", notasUm)

else:
    print("Nao foi possivel realizar o saque!")
