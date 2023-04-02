tamanho = int(input())
chave = int(input())
sequencia = input().split(',')
sequencia = list(map(int, sequencia)) 
lista_final = []
soma = 0

if chave > 0:
    #vai obter os novos valores da lista a partir do indice
    for i in sequencia:
        indice = sequencia.index(i)
        for j in range(1, chave + 1):
            if (indice + j) >= tamanho:
                indice = -j
            soma += sequencia[indice + j]
        else:
            lista_final.append(soma)
        soma = 0

elif chave < 0:
    #vai obter os novos valores da lista a partir do indice
    for i in sequencia:
        indice = sequencia.index(i)
        # vai calcular os valores que vem antes e colocá-los no valor da lista recebido, indo de trás pra frente
        for j in range(-1, chave - 1, -1):
            if (indice + j) < -tamanho:
                indice = -j - 1
            soma += sequencia[indice + j]
        else:
            lista_final.append(soma)
        soma = 0

else:
    for i in sequencia:
        lista_final.append(0)

lista_string = ''
contador = 0

for k in lista_final:
    lista_string += f'{k}'
    contador += 1
    if contador < tamanho:
        lista_string += ', '

if chave == 0:
    print(f'Não foi dessa vez Gideãozinho a chave corrompeu e a sequencia ficou assim: {lista_string}')
else:
    print(f'Vamos lá Gideãozinho a sequencia final é {lista_string}')