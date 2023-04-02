jogador = input().split()
patrulha = input().split()

jogador = list(map(int, jogador))
patrulha = list(map(int, patrulha))

policia_ativa = False
entrada = True

while entrada:
    local = input()
    if local == 'Tumba Secreta de Quentin Trembley':
        policia = input().split()
        policia = list(map(int, policia))
        policia_ativa = True
        entrada = False
    # controle das matrizes.
    tamanho_matriz = int(input())
    matriz_l1 = []
    matriz_l2 = []
    matriz_multiplicada = []
    # pra criar uma linha da matriz.
    for i in range(tamanho_matriz):
        linha_matriz = input().split()
        linha_matriz = list(map(int, linha_matriz))
        matriz_l1.append(linha_matriz)
    # criando outra linha da matriz.
    for i in range(tamanho_matriz):
        linha_matriz = input().split()
        linha_matriz = list(map(int, linha_matriz))
        matriz_l2.append(linha_matriz)
    # multiplicação das matrizes criadas
    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz):
            resultado = 0
            for k in range(tamanho_matriz):
                #segue a regra de algebra na multiplicação
                resultado += matriz_l1[i][k]*matriz_l2[k][j]
            matriz_multiplicada.append(resultado)
    # soma da diagonal
    cord_y = matriz_multiplicada[0]
    for i in range(1, tamanho_matriz):
        cord_y += matriz_multiplicada[i * (tamanho_matriz+1)]
    # soma da linha principal
    cord_x = 0
    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz):
            cord_x += int(matriz_l1[i][j]) + int(matriz_l2[i][j])

    qtd_passos = abs(jogador[0] - cord_x) + abs(jogador[1] - cord_y)
    jogador[0] = cord_x
    jogador[1] = cord_y

    # coodernadas da patrulha.
    patrulha[0] += qtd_passos
    limites = 0
    while patrulha[0] > 7:
        patrulha[0] -= 7
        limites += 1
        if limites % 2 != 0:
            patrulha[0] = 7 - patrulha[0]
    # qnd a patrulha encontra o jogador
    if not policia_ativa:
        if jogador[0] == patrulha[0] and jogador[1] == patrulha[1]:
            print('Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.')
            print('Talvez não foi uma boa ideia ajudar o Ford…')
            print('Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.')
            entrada = False
        else:
            print(f'{local} está na coluna {cord_x} e na linha {cord_y}. Foram dados {qtd_passos} passos para chegar lá.')
else:
    # movimentos da policia
    if policia_ativa:
        passos_policia = abs(cord_x - policia[0]) + abs(cord_y - policia[1])
        if qtd_passos <= passos_policia:
            if jogador[0] == patrulha[0] and jogador[1] == patrulha[1]:
                print('Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.')
                print('Talvez não foi uma boa ideia ajudar o Ford…')
                print('Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.')
            else:
                print(f'{local} está na coluna {cord_x} e na linha {cord_y}. Foram dados {qtd_passos} passos para chegar lá.')
                print('IUHU, VOCÊ SALVOU O FORD!! Agora, todos podem voltar para casa!')
        else:
            print('Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.')