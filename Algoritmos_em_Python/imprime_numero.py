num = float(input("Informe um número:"))



excesso = num - int(num)

if excesso > 0:
    num = int(num)
    num = num + 1


print(num)
