#vezes que se repete
repeticao = int(input())
#termos da sequencia de fibbonachi
n1, n2 = 0, 1
cont = 0
fibbonachi = [0, 1]
# lista que contêm o termo que deve parar
nova = []
# recebe a leitura de cada numero do item
asc = ''
mensagem = ''

while repeticao > 0:
    repeticao -= 1
    lista = input().split(' ')
    indice = int(lista[0])
    termos = lista[1].split('-')

    while cont < indice :
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fibbonachi += [nth]
        cont += 1
    else:
        numero = indice
        termo = str(fibbonachi[numero])

        for i in termo :
            nova += [i]
        else:
            xx = int(termos[0])
            yy = int(termos[1])
            x = nova[xx]
            y = nova[yy]
            valor_tabela = [x, y]

            for a in valor_tabela :
                asc += a
            else:
                valor = int(asc)

        mensagem += chr(valor)

    fibbonachi = [0, 1]
    n1 = 0
    n2 = 1
    cont = 0
    asc = ''
    xx = 0
    yy = 0
    x = ''
    y = ''
    numero = 0
    termo = ''
    nova =[]
    asc = ''
    valor = 0

print(mensagem)