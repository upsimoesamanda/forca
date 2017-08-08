import random #Import_Importa uma biblioteca para o programa. Random é uma biblioteca que possui funções para trabalhar com listas

palavras = []
letrasErradas = ''#Variável ultilizada para contar as letras erradas
letrasCertas = ''#Variável utilizada para contar as letras certas
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Função que recebe possíveis palavras para o jogo 
def Receberpalavras():
    global palavras
    while True:
        p=input("Digite as possíveis palavras para o jogo:")
        palavras.append(p)#append adiciona as palavras da variável p na lista palavra.
        if p =="":
            break

#Def_ Cria uma função. A função principal é a função que ira armazenar os principais comandos do programa.
def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    Receberpalavras()
#A palavra secreta será definida pela função sortearPalavra()
    palavraSecreta = sortearPalavra()
    palpite = ''#O palpite é feito pelo jogador
    desenhaJogo(palavraSecreta,palpite)

    while True:# Com o while True o loop vai rodar enquanto a afirmação for verdadeira.
        palpite = receberPalpite() #palpite vai ser definido pela função receberPalpite()
        desenhaJogo(palavraSecreta,palpite)#Ao receber uma letra o jogo já começa a rodar e a função desenhaJogo() já começa a funcionar agindo por meio de
        #dois parametros a palavra secreta e o palpite
        if perdeuJogo():#if define uma condição de uma sentença que possa ser avaliada como verdadeira ou falsa. 
            print('Voce Perdeu!!!')
            break #Se a a condição for verdadeira o loop para. Break serve para quebrar um loop.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
#Função utilizada para verificar se voê perdeu o jogo        
def perdeuJogo():
    global FORCAIMG #global define que a variável está fora da função
    if len(letrasErradas) == len(FORCAIMG): #len informa quantos caracteres uma lista possui.Se o numero de letras erradas for igual ao numero de caracteres de FORCAIMa pessoa perdeu o jogo
        return True #O Return manda a resposta para o lugar que chamou a função. Se a pessoa perdeu o jogo ele retorna verdade senao falso. 
    else:#Else é uma sentença a ser avaliada se a sentença anterior for falsa. Senão.
        return False
# Função utilizada para verificar se você ganhou o jogo    
def ganhouJogo(palavraSecreta):
    global letrasCertas#A função chama uma variável que está fora dela, a variável LetrasCertas.
    ganhou = True#Na função ganhouJogo será verdade que o jogo foi ganho.
    for letra in palavraSecreta:#Para cada letra da palavraSecreta se a letra não estiver em letrascertas,'nao fizer parte', ganhou será falso
        if letra not in letrasCertas:
            ganhou = False 
    return ganhou #A função só retornará se a pessoa tiver ganhado.       
        

#Função utilizada para receber os palpites
def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")#input captura aquilo que for digitado pelo jogador
    palpite = palpite.upper()#upper deixa todos os caracteres em maiúsculo
    if len(palpite) != 1:#se o palpite tiver mais de uma letra o jogo pede para que o jogador escolha apenas uma letra.
        print('Coloque um unica letra.')
        receberPalpite()
    elif palpite in letrasCertas or palpite in letrasErradas:#Se o palpite já foi feito, o jogo avisa ao jogador.
        print('Voce ja disse esta letra.')
        receberPalpite()
    elif not "A" <= palpite <= "Z":#Se o palpite não for uma letra entra A e Z o jogo pede para que o jogador escolha apenas letras.
        print('Por favor escolha apenas letras')
        receberPalpite()
    else:
        return palpite
    
#Função desenha o bonequinho que define as tentativas do jogador.
#Por meio de dois parametros a palavraSecreta e o palpite.
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG
#Vai desenhar o bonequinho de acordo com o numero de letras erradas
    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:#Se o palpite estiver entre a palavraSecreta, a variável letrasCertas recebe e armazena o palpite. 
        letrasCertas += palpite
    else:#Se o palpite não estiver entre a palavraSecreta, a variável letrasErradas recebe e armazena o palpite.
        letrasErradas += palpite

    for letra in letrasCertas:#para cada letra acertada, o lugar vazio é substituido pela letra.
        for x in range(len(palavraSecreta)):#range criara uma lista com a  mesma quantidade de itens que a palavra secreta.
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )#Printar na tela as letras acertadas, os erros e os espaços que ainda estão vazios.
    print('Erros: ',letrasErradas)
    print(vazio)
     
#função que sortea uma palavra das palavras possíveis para o jogo.
def sortearPalavra():
    global palavras#Puxa as palavras do banco de palavras possíveis 
    return random.choice(palavras).upper()#E retorna uma palavra sorteada aleatoriamente(choice) todas em maiusculo(upper).

    
principal()
