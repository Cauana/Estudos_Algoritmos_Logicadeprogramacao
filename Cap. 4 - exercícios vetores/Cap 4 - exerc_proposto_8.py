#Crie um algoritmo que leia a pontuação final de 200 provas de um concurso e os nomes dos respectivos participantes, e apresente um ranking dos colocados que obtiveram mais de 70 pontos.
import random
listanomes = []
listanotas = []
listanomesacima = []
listanotasacima = []


for num in range(1,5):
    nome = str(input('Digite o nome: '))
    nota = random.randint(1,100)
    listanomes.append(nome)
    listanotas.append(nota)
    
print(listanomes)
print(listanotas)



for i in range(len(listanotas)):
    if listanotas[i]>=70:
        listanomesacima.append(listanomes[i])
        listanotasacima.append(listanotas[i])
print(listanomesacima)
print(listanotasacima)