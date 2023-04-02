quant = int(input())
lista = list()
nome = ''
seguir = True
lista_auxiliar = str() # para guardar os valores e conseguir colocar os espaçamentos corretos

while quant > 0:
    nome = input()
    # vai checar se o nome ja esta na lista
    if nome in lista:
        seguir # nada acontece
    else:
        lista += [nome] # adiciona o nome à lista
    quant -= 1
else:
    # vai comparar em dupla cada valor que está na lista e trocar de lugar caso esteja fora da ordem alfabetica
    for a in range(len(lista)-1, 0, -1):
        for i in range(a):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
    # vai pegar cada palavra da lista principal, colocar dentro da lista auxiliar e adicionar ', '
    for b in range(len(lista)):
        lista_auxiliar += lista[b] + ', '
# para apagar o ', ' do ultimo nome
print(lista_auxiliar[:-2])