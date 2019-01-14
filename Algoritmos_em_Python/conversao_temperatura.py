"""
Converter de Farenheit para Celsius

"""


print("#############################################")

f = float(input("Temperatura em graus Farenheit:"))


C = (5* (f-32)/9)



arrendodar = C - int(C)

if(arrendodar > 0):
    C = int(C)
    C = C + 1

print("TEMPERATURA EM GRAUS CELSIUS = ", C)

print("##############################################")
