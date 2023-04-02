objeto = input()
lista_itens = input().split(', ')
qnt_coletadas = 0
qnt_repetido = 0
contador = 0
coeficiente = 0
lista_auxiliar = []
lista_repetidos = []
a = []
repeticao = False
nome = ''
erro = True

qnt_coletadas = len(lista_itens)

# loop para printar os repetidos
for i in lista_itens :
    if i in lista_auxiliar :
        erro
        lista_repetidos += [i] #guardar os itens que se repetem
        if i in a : # parametroo para que nao print mais de uma vez sobre o msm objeto
            repeticao = True
        elif i not in a or repeticao == False:
            print(f'Após análises, percebi que {i} foi coletado mais de uma vez...')
            a += [i]
    else :
        lista_auxiliar += [i] # quem diz que tem repetição ou nao
else:
    a = []
# contabilizar quem é o mais repetido e quantas vezes se repete
for j in lista_itens :
    for v in lista_repetidos :
        if j == v:
            nome = v
            if nome == v:
                contador += 1
        else:
            a += [1]
    a += [contador]
    contador = 0
    nome = ''

qnt_repetido = int(max(a))

coeficiente = qnt_coletadas/(qnt_repetido+1)

if len(lista_repetidos) > 0 :
        print(f'Certo, o coeficiente de erros de viagens interdimensionais é {coeficiente:.2f}')

if objeto in lista_repetidos or objeto not in lista_itens:
    print('Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...')
else :
    print(f'Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!')

print('(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)')
print('O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"')
print('(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)')