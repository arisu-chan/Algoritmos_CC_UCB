"""
> 50 -> leva multa

4reais por kg excedente

Calcular o excesso (em kg) do peso de peixes e o valor da multa

"""


print("#############################################")

peso = float(input("Informe o peso dos peixes:"))

excesso = peso - int(peso)

multa = int((peso - 50)*4)

print("Excesso (em kg) do peso dos peixes = ", excesso)
print("Valor da multa = ", multa)


print("##############################################")
