nomeInimigo = input()
nomeAliado = input()
clima = input()

mensagem = []
lista = []
juncao = []

contador = 0

seguir = True

while seguir :
    contador += 1
    mensagem = input().split(' ')
    if mensagem[0] == 'Cansado' :
        seguir = False
    else :
        if clima == 'Ensolarado':
            for i in range(len(mensagem)) :
                minimo = i
                for j in range(i + 1, len(mensagem)) :
                    inteiro1 = float(mensagem[minimo])
                    inteiro2 = float(mensagem[j])
                    if inteiro1 > inteiro2 :
                        minimo = j
                mensagem[i], mensagem[minimo] = mensagem[minimo], mensagem[i]
                inteiro1 = 0
                inteiro2 = 0
        elif clima == 'Nublado':
            for i in range(len(mensagem)) :
                maximo = i
                for j in range(i + 1, len(mensagem)) :
                    inteiro1 = float(mensagem[maximo])
                    inteiro2 = float(mensagem[j])
                    if inteiro1 < inteiro2 :
                        maximo = j
                mensagem[i], mensagem[maximo] = mensagem[maximo], mensagem[i]
                inteiro1 = 0
                inteiro2 = 0
        elif clima != 'Ensolaradao' and clima != 'Nublado' and clima != 'ChuvosoNormal' and clima != 'ChuvosoComRaio' :
            print(f'Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??')
            print(f'Tenho certeza que conseguiremos na próxima {nomeAliado}')
            break
        for x in mensagem :
            lista += [x]
        juncao.append(lista)
    lista = []
else:
    posicao = 0
    if clima == 'Ensolarado':
        print(f'Caramba! Finalmente organizamos a mensagem secreta do {nomeInimigo} com esse clima Ensolarado! Vamos nessa {nomeAliado}!')
        print(f'Agora decodificamos as {contador-1} mensagens do {nomeInimigo} e sabemos seus {contador-1} lugares de ataque.')
        print(f'Os lugares sao:')

        for a in range(len(juncao)):
            posicao += 1
            print(f'{posicao} lugar:')
            print(f"Coordenadas: {juncao[a][0]}° {juncao[a][1]}' {juncao[a][2]}''")
            print(f'Horario: {juncao[a][3]}h {juncao[a][4]}m {juncao[a][5]}s')
            print(f'Data: {juncao[a][6]}/{juncao[a][7]}/{juncao[a][8]}')
        print(f'Vamos rapido {nomeAliado}!!')

    elif clima == 'Nublado':
        print(f'Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!')
        print(f'Agora decodificamos as {contador-1} mensagens do {nomeInimigo} e sabemos seus {contador-1} lugares de ataque.')
        print(f'Os lugares sao:')

        for a in range(len(juncao)):
            posicao += 1
            print(f'{posicao} lugar:')
            print(f"Coordenadas: {juncao[a][0]}° {juncao[a][1]}' {juncao[a][2]}''")
            print(f'Horario: {juncao[a][3]}h {juncao[a][4]}m {juncao[a][5]}s')
            print(f'Data: {juncao[a][6]}/{juncao[a][7]}/{juncao[a][8]}')
        print(f'Vamos rapido {nomeAliado}!!')

    elif clima == 'ChuvosoNormal':
        controle = len(juncao)
        for p in range(len(juncao)-1) :
            valor1 = juncao[p]
            valor2 = juncao[p+1]
            for q in range(9) :
                inteiro1 = float(valor1[q])
                inteiro2 = float(valor2[q])
                if inteiro1 < inteiro2 :
                  valor1[q], valor2[q] = valor2[q], valor1[q]
                inteiro1 = 0
                inteiro2 = 0
        print(f'Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!')
        print(f'Agora decodificamos as {contador-1} mensagens do {nomeInimigo} e sabemos seus {contador-1} lugares de ataque.')
        print(f'Os lugares sao:')

        for a in range(len(juncao)):
            posicao += 1
            print(f'{posicao} lugar:')
            print(f"Coordenadas: {juncao[a][0]}° {juncao[a][1]}' {juncao[a][2]}''")
            print(f'Horario: {juncao[a][3]}h {juncao[a][4]}m {juncao[a][5]}s')
            print(f'Data: {juncao[a][6]}/{juncao[a][7]}/{juncao[a][8]}')
        print(f'Vamos rapido {nomeAliado}!!')

    elif clima == 'ChuvosoComRaio' :
        controle = len(juncao)
        for p in range(len(juncao)-1) :
            valor1 = juncao[p]
            valor2 = juncao[p+1]
            for q in range(9):
                inteiro1 = float(valor1[q])
                inteiro2 = float(valor2[q])
                if inteiro1 > inteiro2 :
                    valor1[q], valor2[q] = valor2[q], valor1[q]
                inteiro1 = 0
                inteiro2 = 0
        print(f'Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeInimigo}! Vamos nessa {nomeAliado}!')
        print(f'Agora decodificamos as {contador-1} mensagens do {nomeInimigo} e sabemos seus {contador-1} lugares de ataque.')
        print(f'Os lugares sao:')

        for a in range(len(juncao)):
            posicao += 1
            print(f'{posicao} lugar:')
            print(f"Coordenadas: {juncao[a][0]}° {juncao[a][1]}' {juncao[a][2]}''")
            print(f'Horario: {juncao[a][3]}h {juncao[a][4]}m {juncao[a][5]}s')
            print(f'Data: {juncao[a][6]}/{juncao[a][7]}/{juncao[a][8]}')
        print(f'Vamos rapido {nomeAliado}!!')

