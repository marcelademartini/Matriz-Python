from random import randint

#ordem da matriz --> matriz quadrada (total de linhas = total de colunas)
ordem = 5 

#geração da matriz
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        linha.append(randint(0,50))
    matriz.append(linha)
    
# impressão da matriz em formato tabular
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="\t")
    print()
        
#troca das diagonais
j = len(matriz) - 1
for i in range(len(matriz)):
    temp = matriz[i][i]
    matriz[i][i] = matriz[i][j]
    matriz[i][i] = temp
    j = j - 1 # -= 1
    
# impressão da matriz em formato tabular
print()
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="\t")
    print()