
area = int(input("Digite a area:"))


litros = area // 6
    
if area % 6 > 0:
    litros = litros + 1



latas = litros // 18

if area % 18 > 0:
    latas = latas + 1

galao = litros // 4

if litros % 4 > 0:
    galao = galao + 1


precoLatas = latas*80
precoGalao = galao*25


print(precoLatas)
print(precoGalao)









