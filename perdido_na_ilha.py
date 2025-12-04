import random

#j += 1 == frente (direita).

#i -= 1 ==  cima

def fromCodeToMap(dados,matrizZerada):

    for i in range(10):
        matrizZerada.append([])
        for j in range(10):
            matrizZerada[i].append(0)

    partes = dados.split(";")
    for valores in partes:
        separa_dados = valores.split()
       
        if len(separa_dados) == 3:
            linha = int(separa_dados[0])
            coluna = int(separa_dados[1])
            valor = int(separa_dados[2])
            matrizZerada[linha][coluna] = valor

    return matrizZerada

def printMap(matrizComVal):
    print("\nMatriz com peso de cada casa\n")

    for i in range(10):
        for j in range(10):
            print(matrizComVal[i][j],end = " ")
        print()
    print("\n------------------------------------------------------------------------")

def showWalkedPath(matriz, custo_atual):

    print("Progresso atual:")
    for i in range(10):
        for j in range(10):
            print(matriz[i][j],end = " ")
        print()
    print(f"\nCusto parcial: {custo_atual}")

def caminhoFixo(matriz_fixa):
    
    caminhadaFixa = "010101010101010101"
    i = 9
    j = 0
    passos_fixa = 0
    custoFixa = matriz_fixa[i][j]
    matriz_fixa[9][0] = 0

    print(f"\nCaminhada Fixa: {caminhadaFixa}")

    for num in caminhadaFixa:

        if num == "0":
            j+=1
            custoFixa += matriz_fixa[i][j]
            matriz_fixa[i][j] = 0
            passos_fixa +=1

        elif num == "1":
            i-=1
            custoFixa += matriz_fixa[i][j]
            matriz_fixa[i][j] = 0
            passos_fixa+=1

        if passos_fixa % 5 == 0:
            print()
            showWalkedPath(matriz_fixa, custoFixa)
            print()

    for i in range(10):
        for j in range(10):
            print(matriz_fixa[i][j],end = " ")
        print()
    
    print(f"\nCusto Total Fixa:{custoFixa}\n")
    print("------------------------------------------------------------------------")

def caminhoRandom(matriz_random,cont_rodagem):
    i = 9
    j = 0
    custo_random = matriz_random[i][j]
    lista_random = []
    matriz_random[9][0] = 0
    for _ in range(18):
        caminhadaRandom = random.randint(0,1) 
        lista_random.append(caminhadaRandom)

    while not (i == 0 and j == 9): # enquanto não for...
            
        for num in lista_random:
            if num == 0:
                if j < 9:
                    j+=1
                    custo_random+= matriz_random[i][j]
                    matriz_random[i][j] = 0
                else:
                    j = j

            elif num == 1:
                if i > 0:
                    i-=1
                    custo_random += matriz_random[i][j]
                    matriz_random[i][j] = 0
                else:
                    i = i
        
    print(f"\nCaminhada Random {cont_rodagem+1}:{lista_random}")
    print(f"Custo total:{custo_random}\n")
    
def gulosa(matriz_gulosa):
    print("------------------------------------------------------------------------")
    print("\nCaminhada Gulosa\n")
    i = 9
    j = 0
    matriz_gulosa[9][0] = 0

    custo_gulosa = matriz_gulosa[i][j]
    caminho_percorrido = ""
    passos = 0

    while not (i == 0 and j == 9):

        if i > 0:
            cima = matriz_gulosa[i-1][j]
        else:
            cima = float('inf') # ai se i > 0, "direta" nunca vai ser maior que o "cima"

        if j < 9 :
            direita = matriz_gulosa[i][j+1]
        else:
            direita = float('inf')

        if direita <= cima: #se for < ou = vai p frente 
            j+=1
            custo_gulosa+=matriz_gulosa[i][j]
            matriz_gulosa[i][j] = 0
            caminho_percorrido+="0"

        else: # direita < cima
            i-=1
            custo_gulosa+=matriz_gulosa[i][j]
            matriz_gulosa[i][j] = 0      
            caminho_percorrido+="1"
        passos+=1

        if passos % 5 == 0:
            print()
            showWalkedPath(matriz_gulosa, custo_gulosa)
            print()

    for i in range(10):
        for j in range(10):
            print(matriz_gulosa[i][j],end=" ")
        print()

    print(f"\nO custo da Gulosa foi: {custo_gulosa}")
    
matriz = []
entrada ="0 0 3; 0 1 25; 0 2 3; 0 3 8; 0 4 8; 0 5 1; 0 6 25; 0 7 1; 0 8 3; 0 9 8; 1 0 1; 1 1 3; 1 2 8; 1 3 3; 1 4 8; 1 5 1; 1 6 25; 1 7 3; 1 8 8; 1 9 1; 2 0 25; 2 1 1; 2 2 8; 2 3 1; 2 4 1; 2 5 1; 2 6 1; 2 7 25; 2 8 3; 2 9 1; 3 0 8; 3 1 25; 3 2 25; 3 3 25; 3 4 1; 3 5 3; 3 6 8; 3 7 8; 3 8 3; 3 9 25; 4 0 1; 4 1 1; 4 2 1; 4 3 25; 4 4 25; 4 5 3; 4 6 3; 4 7 25; 4 8 25; 4 9 8; 5 0 1; 5 1 25; 5 2 25; 5 3 1; 5 4 8; 5 5 8; 5 6 1; 5 7 3; 5 8 1; 5 9 8; 6 0 3; 6 1 8; 6 2 8; 6 3 3; 6 4 8; 6 5 3; 6 6 3; 6 7 3; 6 8 25; 6 9 8; 7 0 3; 7 1 25; 7 2 25; 7 3 3; 7 4 8; 7 5 1; 7 6 1; 7 7 8; 7 8 25; 7 9 3; 8 0 8; 8 1 1; 8 2 25; 8 3 3; 8 4 8; 8 5 8; 8 6 3; 8 7 3; 8 8 1; 8 9 25; 9 0 1; 9 1 25; 9 2 1; 9 3 1; 9 4 8; 9 5 25; 9 6 8; 9 7 3; 9 8 25; 9 9 1;"

matriz_inicial = fromCodeToMap(entrada, matriz) # me retona a matriz pronta
printMap(matriz_inicial) # so é pra printar


matriz_paraFixo = []
for linha_original in matriz_inicial:

    copia_da_linha = linha_original[:]  # ...crie uma cópia dessa linha
    matriz_paraFixo.append(copia_da_linha) # 3. Adicione a cópia da linha na sua nova matriz
caminhoFixo(matriz_paraFixo)


for cont_vez in range(10):
    matriz_paraRandom = []
    for linha_original in matriz_inicial:
        copia_da_linha = linha_original[:]
        matriz_paraRandom.append(copia_da_linha)

    caminhoRandom(matriz_paraRandom,cont_vez)


matriz_paraGulosa = []
for linha_original in matriz_inicial:

    copia_da_linha = linha_original[:]
    matriz_paraGulosa.append(copia_da_linha) 
gulosa(matriz_paraGulosa)

