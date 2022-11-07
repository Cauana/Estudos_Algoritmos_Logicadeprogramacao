#média ponderada (com pesos diferentes)
media = 0
count = 0
for nota in range(1,6):
    count+=1
    n = float(input('Digite as notas:'))
    peso = n*count
    media += peso
mediafinal = media/15
print(f'A média final é {mediafinal:.2f}')