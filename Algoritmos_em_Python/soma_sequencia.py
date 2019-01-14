"""
Dado um número inteiro positivo n
Calcular a soma dos n primeiros números inteiros positivos
"""


n = int(input("Digite o primeiro numero:"))


# 5 = 5+4+3+2+1+0


cont = 0
soma = 0

while cont <=n:
    soma = soma + cont
    cont = cont + 1


print(soma)
