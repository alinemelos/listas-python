quant = int(input())
entrada = ''
num_diario = 0
diario1 = []
diario2 = []
diario3 = []
busca = ''
num_informacoes = 0

while quant > 0 :
    entrada, num_diario = input().split(',')
    if num_diario == ' 1' :
        diario1 += [entrada]
    elif num_diario == ' 2' :
        diario2 += [entrada]
    elif num_diario == ' 3' :
        diario3 += [entrada]

    quant -= 1
else :
    num_informacoes = int(input())
    while num_informacoes > 0 :
        busca = input()
        if busca in diario1 :
            print(f'Informacoes sobre {busca} estao no Diario 1')
        elif busca in diario2 :
            print(f'Informacoes sobre {busca} estao no Diario 2')
        elif busca in diario3 :
            print(f'Informacoes sobre {busca} estao no Diario 3')
        else :
            print(f'Nenhum dos diarios possui informacoes sobre {busca}')
        num_informacoes -= 1

