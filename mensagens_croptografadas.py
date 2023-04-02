quantidade = int(input())

codificada = []
clear_list = []
lista_numeros = []
lista_letras = []

letra_numerico = 0
soma_par = 0
soma_impar = 0
multiplicacao = 1

decodificadora = ''
mensagem = ''
mensagem_letra = ''
mensagem_final = ''
sem_resposta = True

while quantidade > 0 :
    quantidade -= 1
    linha = input()
    decodificadora = input()
    linha = input()
    codificada = input().split(' ')
    # loop para retirar os caracteres especiais da lista
    for i in codificada :
        if i == '!' or i == '@' or i == '$' or i == '%' or i == '&' or i == '#' or i == ' ':
            nada = True
        else :
            clear_list += [i]
    # loop para  criar a lista apenas de numeros
    for s in clear_list :
        if s == '0' or s == '1' or s == '2' or s == '3' or s == '4' or s == '5' or s == '6' or s == '7' or s == '8' or s == '9' :
            lista_numeros += [s]

    if len(clear_list) == 0 :
        sem_resposta = False

    if decodificadora == 'Portal' :
        # loop para criar a lista so de letras
        for a in clear_list :
            if a == '0' or a == '1' or a == '2' or a == '3' or a == '4' or a == '5' or a == '6' or a == '7' or a == '8' or a == '9' :
                nada
            else :
                lista_letras += [a]
        # loop para percorrer as letras e transforma-las no valor decimal
        for l in lista_letras :
            letra_numerico = (ord(l) + 1)
            # para o caso de ser z o proximo valor decimal seria }, então o if faz ir pro 'a'
            if letra_numerico == 123 :
                mensagem_letra += chr(97)
            else:
                mensagem_letra += chr(letra_numerico)

            letra_numerico = 0

        mensagem_final += mensagem_letra + ' '

    elif decodificadora == 'Experimento' :
        # loop para ver se os numeros sao pares ou impares
        for p in lista_numeros :
            inteiro = int(p)
            if inteiro%2 == 0 :
                soma_par += inteiro
            else :
                soma_impar += inteiro
            inteiro = 0

        mensagem_final += str(soma_par) + ' '

    elif decodificadora == 'Realidade' :

        for p in lista_numeros :
            inteiro = int(p)
            if inteiro%2 == 0 :
                soma_par += inteiro
            else :
                soma_impar += inteiro
            inteiro = 0

        mensagem_final += str(soma_impar) + ' '

    elif decodificadora == 'Schembulock' :
        # multiplica todos os numeros
        for p in lista_numeros :
            inteiro = int(p)
            multiplicacao = inteiro * multiplicacao
            inteiro = 0

        mensagem_final += str(multiplicacao) + ' '
    # zerar os valores das variaveis para nao acumular em cada loop
    clear_list = []
    multiplicacao = 1
    soma_impar = 0
    soma_par = 0
    lista_numeros = []
    lista_letras = []
    mensagem_letra = ''

else :
    if sem_resposta == False :
        print('Esse formato de mensagem nem Bill Cipher entenderia!')
    else:
        print(f'Consegui! A mensagem decodificada de Bill Cipher é: {mensagem_final [:-1]}')