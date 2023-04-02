# listas-python
<h2>Busca binária</h2>
O primeiro input serão as suas coordenadas e as do Esquadrão do Tempo, respectivamente:

ccord_X_você coord_Y_coord

coord_X_Esquad coord_Y_Esquad

Para cada “pista” haverá um série de entradas:

Nome do próximo local

Se o local for “Tumba Secreta de Quentin Trembley”, haverá uma entrada com a coordenada dos policiais:

coord_X_Pol coord_Y_Pol

Dimensão das matrizes e as matrizes:

N

a_11 a_12 … a_1n

.

.

.

a_n1 a_n2 … a_nn

b_11 b_12 … b_1n

.

.

.

b_n1 b_n2 … b_nn

Output

A cada pista, você deve imprimir as coordenadas do local que acabou de chegar e quantos movimentos foram necessários para chegar lá:

{nome_do_próximo_local} está na coluna {coord_X} e na linha {coord_Y}. Foram dados {qnt_passos} passos para chegar lá.

Se o Esquadrao do Tempo chegar em você, imprima:

Parado! Está cercado pelo Esquadrão De Segurança para Evitar o Paradoxo do Tempo. O que quer que você diga pode ou já foi usado contra você no Tribunal do Futuro.

Talvez não foi uma boa ideia ajudar o Ford…

No fim, se você voltou para o CIn e salvou o Ford:

IUHU, VOCÊ SALVOU O FORD!! Agora, todos podem voltar para casa!

Mas, se você não conseguir salvar o Ford:

Oh, não! O Ford vai ter que achar outro jeito de voltar para casa.
<h2>Desventurando a mente </h2>
a mensagem se dividia em duas partes:

A primeira informava em qual índice da sequência de Fibonacci se encontra o número que iremos utilizar para decifrar nosso código.
Na segunda parte, x-y são as posições de dois dígitos no número que foi encontrado na primeira parte. x = posição do primeiro dígito e y = posição do segundo dígito do código.
Os dois dígitos encontrados são concatenados e formam um código ASCII.
Utilize a função chr() para descobrir seu significado que fará parte da mensagem final.

Exemplo:
Suponha que o número dado para o índice da sequência de fibonacci seja 32 e que x-y seja 2-3.
Na sequência de fibonacci, o número 32 da sequência é 2178309.
Os dígitos na posição 2 e 3 do número encontrado são, respectivamente, 7 e 8.
Portanto, devemos buscar na tabela ASCII o dígito de código ASCII 78.
Descobrimos, finalmente, que o dígito encontrado é a letra N.

Descoberto isso, o velho deixou você responsável por fazer o script que receberia as informações da máquina e encontrar qual é a mensagem sendo passada por cada memória.

Obs.: tanto a sequência de Fibonacci, quanto a contagem dos índices são iniciados em zero

Input

A primeira entrada indica a quantidade de decodificações que precisam ser realizadas

n

Em seguida, você receberá as n mensagens a serem decodificadas

z x-y

...

Output

A saída consiste na combinação de todas as decodificações:
"{MENSAGEM DECODIFICADA}"

<h2>Digitalizando Diários </h2>
Para tanto, o seu programa deve ser capaz de receber os nomes de determinada quantidade de registros e o diário onde cada um se encontra, armazená-los no diário correspondente, e, depois, permitir que o usuário busque-os, indicando o diário referente.

Input

O primeiro input consiste em um inteiro n >= 1, indicando o número de entradas subsequentes, que consistirão nas informações a registrar.

n

Esses n inputs sempre terão o formato abaixo, em que {conteudo} pode ser uma string qualquer e {numero_do_diario} pode ser o número 1, 2 ou 3 separados por vírgula e um espaço:

{conteudo}, {numero_do_diario}

...

Depois, será recebido um inteiro m >= 1, referente ao número de informações que queremos buscar:

m

Seguido de m strings a buscar, cada uma referenciando, ou não, a algum dos n nomes recebidos anteriormente:

{conteudo_buscado}

...

Output

Para cada uma das m buscas, será printada uma dessas frases, dependendo do seu resultado:

"Informacoes sobre {conteudo_buscado} estao no Diario {numero_do_diario}", no caso da informação buscada ser encontrada, ou

"Nenhum dos diarios possui informacoes sobre {conteudo_buscado}", caso o conteúdo buscado não exista em nenhum dos diários.

<h2>Gideolandia</h2>
Em Gravity Falls, Gideãozinho é um menino vidente que diz poder ler mentes, prever o futuro e falar com os mortos na sua Tenda da Telepatia, concorrente da Cabana do Mistério do tivô Stan. Como vingança à família Pines, Gideãozinho almeja roubar a escritura da Cabana do Mistério e transformá-la no Parque de Diversões do Gideãozinho. Para isso, ele precisa do código do cofre do tivô Stan e você, estudante do CIn, será um agente de Gideãozinho que terá que encontrar o código secreto do cofre e roubar a escritura da Cabana do Mistério.
Gideãozinho, com a ajuda de Bill Cipher, encontraram um conjunto de números que formam uma pré-sequência, porém ela estava criptografada.

Input

Para descriptografar, você vai receber o tamanho da sequencia, uma chave em número inteiro e a pré-sequência correspondente

tamanho

chave

sequencia

Output

Para descriptografar a pré-sequência você precisará substituir os números de acordo com as seguintes regras:

Dado uma chave K

Se k > 0, substitua o i-ésimo número pela soma dos próximos k números
Se k < 0, substitua o i-ésimo número pela soma dos k números anteriores
Se k == 0, substitua o i-ésimo número por 0
OBS: A sequência é circular, portanto o elemento seguinte de sequencia[N-1] é sequencia[0] e o elemento anterior de sequencia[0] é sequencia[N-1], em uma sequência de tamanho N

Por fim, se a chave k for 0 imprima:

Não foi dessa vez Gideãozinho a chave corrompeu e a sequencia ficou assim: {sequencia_final}

caso contrário imprima:

Vamos lá Gideãozinho a sequencia final é {sequencia_final}

Em que sequencia_final é a sequência com os números separados por vírgulas e espaços
<h2>Mensagens</h2>
Input

Primeiro de tudo você irá receber o nome do nosso inimigo!!

nomeInimigo

Depois, você receberá o nome do seu aliado que estará ali para lhe ajudar.

nomeAliado

Após o input dos nomes você receberá um relatório sobre o dia atual, de como está a situação climática…

climaAtual

Depois disso receberá 9 números em uma única linha correspondente a mensagem criptografada obtida do seu inimigo!! A quantidade de mensagens é indefinida e só parará com uma condição de parada.

mensagem1

mensagem2

mensagem3

…

mensagem_final

Exemplo1: 1 2 3 4 5 6 7 8 9
Exemplo2: 10 123 1345 0543 234 102 -1
Seu input só irá parar caso receba: Cansado finalizando o número de mensagens e terminando a contagem.

DICA: Organizar as mensagens em uma lista pode ajudar

Output

A primeira ação a ser feita é analisar o clima para a decodificação.

Caso o clima NÃO seja Ensolarado ou Nublado ou ChuvosoNormal ou ChuvosoComRaio, printe:

Infelizmente esse clima não está bom. Não conseguimos decifrar a mensagem, o que será do mundo agora??

Tenho certeza que conseguiremos na próxima {nomeAliado}

Após as mensagens o programa deve ser ENCERRADO!!

Caso o clima seja algum dos acima citados você deverá fazer ações específicas:
Ensolarado
Caso o clima esteja Ensolarado a ação a ser feita é realizar uma ORDENAÇÃO dos números de cada mensagem acima obtida. A ordenação deve ser feita do MENOR valor para o MAIOR.
Ao fim dessa etapa, você deve printar:

Caramba! Finalmente organizamos a mensagem secreta do {nomeInimigo} com esse clima Ensolarado! Vamos nessa {nomeAliado}!

Nublado
Caso o clima esteja Nublado a ação a ser feita é realizar uma ORDENAÇÃO dos números de cada mensagem acima obtida. A ordenação deve ser feita do MAIOR valor para o MENOR.
Ao fim dessa etapa, você deve printar:

Ufa! Mesmo com o clima Nublado ainda desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!

DICA: Buscar qualquer tipo de ordenação para usar (procurem vídeos no Youtube). Algum exemplo de ordenações básicas: Bubble Sort e Selection Sort. Link rápido para explicação sobre Selection Sort: https://www.youtube.com/watch?v=g-PGLbMth_g
ChuvosoNormal
Caso o clima esteja ChuvosoNormal a ação a ser realizada é comparar os valores de cada posição de uma mensagem com os da mesma posição da mensagem seguinte. Caso o valor da posição X da primeira mensagem seja MENOR que o valor da posição X da segunda mensagem, deverá haver uma troca entre eles.
Exemplo: Valores da mensagem1 com Valores da mensagem2, Valores da mensagem2 com Valores da mensagem3, Valores da mensagem3 com Valores da mensagem4…
OBS: A última mensagem NÃO sofre troca com uma mensagem posterior por não haver continuação.

Ao fim dessa etapa, você deve printar:

Nem mesmo a chuva vai nos parar de salvar o mundo! Desvendamos a mensagem do {nomeInimigo}! Vamos nessa {nomeAliado}!

ChuvosoComRaio
Caso o clima esteja ChuvosoComRaio a ação a ser feita é quase a mesma lógica do ChuvosoNormal mas agora a troca só ocorre caso o valor da posição X da primeira mensagem seja MAIOR que o valor da posição X da segunda mensagem.
OBS: A última mensagem NÃO sofre troca com uma mensagem posterior por não haver continuação.
Ao fim dessa etapa, você deve printar:

Eitaa! Até mesmo essa chuva com trovoadas não nos parou. Estamos indo até você, {nomeInimigo}! Vamos nessa {nomeAliado}!

Agora com todas as mensagens prontas para leitura podemos finalmente confirmar seu plano! Descobrimos que a quantidade de mensagens representa uma quantidade de ataques a ser feito. Portanto, a próxima ação é:

Printar Agora decodificamos as {quantidade} mensagens do {nomeInimigo} e sabemos seus {quantidade} lugares de ataque.

Printar Os lugares sao:

Após os prints acima, você deve mostrar o local do ataque que cada mensagem passou. Para isso, para CADA MENSAGEM você deve:

Printar {posição} lugar:

Em que posição corresponde à numeração de cada lugar. A primeira mensagem é o primeiro lugar, a segunda mensagem é o segundo lugar, a terceira mensagem é o terceiro lugar, etc. e deve estar em número decimal , inciando do 1.

Exemplo: 1 lugar, 2 lugar…
Agora sabendo de qual lugar estamos falando devemos mostrar suas coordenadas, o horário do ataque e também a data! Para isso, basta olharmos nossa mensagem decodificada e pegar seus valores. A coordenada corresponde aos 3 primeiros valores obtidos, o horário corresponde aos próximos 3 valores e, por fim, a data corresponde aos últimos 3 valores.

OBS: Esses são os valores obtidos APÓS a ordenação ou a troca (depende do clima)
OBS: Cada local de ataque possui suas informações, então são os 9 valores do primeiro lugar, depois do segundo lugar, e assim por diante.
Então nossa próxima ação a ser feita é:

Printar Coordenadas: {posição0 da msg}° {posição1 da msg}' {posição2 da msg}''

Printar Horario: {posição3 da msg}h {posição4 da msg}m {posição5 da msg}s

Printar Data: {posição6 da msg}/{posição7 da msg}/{posição8 da msg}

OBS: Para CADA MENSAGEM deve-se mostrar a numeração (qual número é o local) e também suas coordenadas, horários e datas.
OBS: Não se importar com coordenadas, horários e datas fora da realidade também.
Agora com tudo pronto nós temos que agir rápido!! Apenas finalize o programa com a seguinte ação:

Printar Vamos rapido {nomeAliado}!!

Obrigado por salvar o mundo!!!
<h2>Mensagens Criptografadas</h2>
Input

Para decifrar a mensagem codificada você primeiro vai receber um número inteiro que é o total de palavras que você precisará decodificar:

n

Depois, por n vezes, você receberá a palavra decodificadora e a palavra codificada:

palavra_decodificadora

p a l a v r a _ c o d i f i c a d a

Em cada rodada, após decodificar a palavra codificada por meio das instruções da palavra decodificadora, você deve guardar essa palavra para compor a mensagem final.

💡 Obs.: Observe que existem quebras de linhas entre os inputs, e as letras na mensagem codificada são separadas por um espaço vazio

Output

O output final caso você consiga decodificar as palavras é uma mensagem com todas as palavras decodificadas separadas por espaço (lembre que cada conjunto de entrada com uma palavra decodificadora e uma palavra codificada gerava uma palavra):

"Consegui! A mensagem decodificada de Bill Cipher é: {palavra1 palavra2 palavra3 ... palavraN}"

Se a mensagem final não tiver letras ou números, você deve imprimir:

"Esse formato de mensagem nem Bill Cipher entenderia!"
<h2>Ordenando</h2>
Input

Você irá receber o número N de criaturas a serem ordenadas, em seguida N linhas contendo os nomes das criaturas.

OBS: O mesmo nome pode aparecer duas vezes na entrada.

Output

Você deverá imprimir as criaturas em ordem lexicográfica e separadas por vírgula (exceto na última criatura).

OBS: Caso exista algum nome repetido, não imprima este mais de uma vez
<h2>Procurando objetos</h2>
OBS.: Você não poderá utilizar o método count(), o método find() nem qualquer função que ordene listas nessa questão. Além disso, não haverá casos de empate em relação ao item mais encontrado.

Input

A entrada inicial será o objeto que Stanford Pines está procurando:

objeto_procurado

A próxima entrada será uma lista dos itens do episódio que você coletou. Os itens serão separados por vírgula e espaço e os seus nomes estarão todos na mesma linha:

item_1, item_2, item_3, …, item_n

Output

Para cada item repetido que você coletar, a saída deve ser:

Após análises, percebi que {item_repetido} foi coletado mais de uma vez...

OBS: Essa saída só deverá ser printada na primeira vez em que o item for repetido.

Caso existam itens repetidos, você deverá imprimir uma saída com o valor do coeficiente de erros de viagens interdimensionais:

Certo, o coeficiente de erros de viagens interdimensionais é {coeficiente}

Atenção: O coeficiente de erros de viagens interdimensionais é o resultado da divisão da quantidade de itens coletados pela quantidade de vezes que você encontrou o item que foi mais coletado (qt_itens_coletados/qt_item_mais_repetido). Ele é um float com DUAS casas decimais.

Se você coletou o objeto que Stanford Pines está procurando e ele não é um erro interdimensional:

Você encontrou o item necessário para me ajudar a voltar para minha dimensão! Finalmente voltarei para Gravity Falls!

Se você não coletou o objeto que Stanford Pines está procurando ou ele é um erro interdimensional:

Que pena, você não encontrou o item necessário para me ajudar a voltar para minha dimensão...

No final do programa, você sempre deve printar:

(Como prometido, você retorna ao DA do CIn. Mas, por razões desconhecidas, você se esquece do ocorrido)

O walkie-talkie está na sua mão. Depois de um tempo, você diz: "Que aparelho velho!"

(Após pensar sobre o que fazer com o walkie-talkie, você resolve jogá-lo no banheiro do CIn)
