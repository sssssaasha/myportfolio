#Primeiro, importamos as bibliotecas randint para podermos estruturar a randomização da jogada do computador e getpass para podermos
#esconder a opção que os jogadores escolhem, deixando a gameplay mais interessante.
from random import randint
import getpass

#Depois, criamos nosso menu, usando print para imprimir as informações que gostaríamos que o jogador visualizasse. E também criamos a variável menu,
#que pede do jogador a opção que ele quer escolher. Usamos int, pois o dado que estamos pedindo é um número inteiro.
print("--- Menu Jokenpô ---")
print("1 - humano x humano")
print("2 - humano x computador")
print("3 - computador x computador")
print("4 - sair do jogo")
menu = int(input("Escolha o modo de jogo: "))

#Esse primeiro while serve para que, enquanto o jogador escolher as opções 1, 2 ou 3 do menu, os modos de jogo acontecem como especificados mais à frente
while menu <= 3 and menu != 4:

#Para termos um sistema de rounds e placar, colocamos contadores iniciando no zero, para que eles aumentem de acordo com a passagem do jogo.
#Esses contadores se repetem nos 3 modos de jogo, mas cada um com sua especificidade de acordo com o modo que está sendo jogado.
    round1 = 0
    placarUm = 0
    placarDois = 0
#Utilizamos um while para selecionar e inicializar o primeiro modo de jogo onde será humanoxhumano
#Atenção! Caso não esteja rodando o modo 1 é só ir em run, configurações e ativar "Emulate terminal in output console"
    while menu == 1:
        round1 += 1
        print(f'--- Round {round1} ---')
        if menu== 1:
            #Aqui utilizamos o getpass para ocultar as escolhas do jogadores tornando o jogo mais divertido
            jogadorUm = getpass.getpass("Jogador um escolha pedra, papel ou tesoura: ")
            jogadorDois = getpass.getpass("Jogador dois escolha pedra, papel ou tesoura: ")
            print("j1: ", jogadorUm, "\nj2: ", jogadorDois)
            #Usamos blocos if para calcular qual jogador ganha no pedra, papel ou tesoura
            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura') and (jogadorDois == 'pedra' or jogadorDois == 'papel' or jogadorDois == 'tesoura'):
                if jogadorUm == 'tesoura' and jogadorDois == 'papel':
                    placarUm = placarUm + 1
                elif jogadorUm == 'tesoura' and jogadorDois == 'pedra':
                    placarDois = placarDois + 1
                elif jogadorUm == 'pedra' and jogadorDois == 'tesoura':
                    placarUm = placarUm + 1
                elif jogadorUm == 'pedra' and jogadorDois == 'papel':
                    placarDois = placarDois + 1
                elif jogadorUm == 'papel' and jogadorDois == 'tesoura':
                    placarDois = placarDois + 1
                elif jogadorUm == 'papel' and jogadorDois == 'pedra':
                    placarUm = placarUm + 1
                else:
                    print("Empate")
        #Aqui apresentamos na tela o placar e perguntamos se a pessoa quer continuar jogando
        print("--- Placar ---")
        print(f' {placarUm} vs {placarDois}')
        menu = int(input('Se gostaria de continuar digite 1, se não, digite 5: '))
        #Caso a pessoa decida sair do modo o menu é apresentado novamente
        if menu != 1 and menu != 2 and menu != 3 and menu != 4:
            print("--- Menu Jokenpô ---")
            print("1 - humano x humano")
            print("2 - humano x computador")
            print("3 - computador x computador")
            print("4 - sair do jogo")
            menu = int(input("Escolha o modo de jogo: "))

    #Inicializamos as variaveis que serão utilizadas no segundo modo de jogo
    round2 = 0
    placarTeste1 = 0
    placarComputador1 = 0
    #Utilizamos outro while para o segundo modo que será humanoxcomputador
    while menu == 2:
        if menu == 2:
            round2 += 1
            print(f'--- Round {round2} ---')
            jogadorUm = input("Jogador escolha pedra, papel ou tesoura: ")
            #Aqui randomizamos as jogadas do computador
            itens = ('pedra', 'papel', 'tesoura')
            computador = randint(0,2)
            print(itens[computador])
            #Usamos blocos if para calcular se o jogador ou o computador ganha no pedra, papel ou tesoura
            if (jogadorUm == 'pedra' or jogadorUm == 'papel' or jogadorUm == 'tesoura'):
                if jogadorUm == 'tesoura' and itens[computador] == 'papel':
                    placarTeste1 = placarTeste1 + 1
                elif jogadorUm == 'tesoura' and itens[computador] == 'pedra':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'tesoura':
                    placarTeste1 = placarTeste1 + 1
                elif jogadorUm == 'pedra' and itens[computador] == 'papel':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'papel' and itens[computador] == 'tesoura':
                    placarComputador = placarComputador1 + 1
                elif jogadorUm == 'papel' and itens[computador] == 'pedra':
                    placarTeste1 = placarTeste1 + 1
                else:
                    print("Empate")
            #Aqui apresentamos na tela o placar e perguntamos se a pessoa quer continuar jogando
            print("--- Placar ---")
            print(f' {placarTeste1} vs {placarComputador1}')
            menu = int(input('Se gostaria de continuar digite 2, se não, digite 5: '))
            #Caso a pessoa decida sair do modo o menu é apresentado novamente
            if menu != 1 and menu != 2 and menu != 3 and menu != 4:
                print("--- Menu Jokenpô ---")
                print("1 - humano x humano")
                print("2 - humano x computador")
                print("3 - computador x computador")
                print("4 - sair do jogo")
                menu = int(input("Escolha o modo de jogo: "))

    #Inicializamos as variaveis que serão utilizadas no terceiro modo de jogo
    round3 = 0
    placarTeste2 = 0
    placarComputador2 = 0
    #Utilizamos outro while para o segundo modo que será computadorxcomputador
    while menu == 3:
        round3 += 1
        print(f'--- Round {round3} ---')
        if menu == 3:
            #Aqui randomizamos as jogadas do computador duas vezes
            itens = ('pedra','papel','tesoura')
            computadorUm = randint(0,2)
            computadorDois = randint(0,2)
            print(itens[computadorUm])
            print(itens[computadorDois])

            #Usamos blocos if para calcular qual computador ganha no pedra, papel ou tesoura
            if itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'papel':
                placarTeste2 = placarTeste2 + 1
            elif itens[computadorUm] == 'tesoura' and itens[computadorDois] == 'pedra':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'tesoura':
                placarTeste2 = placarTeste2 + 1
            elif itens[computadorUm] == 'pedra' and itens[computadorDois] == 'papel':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'tesoura':
                placarComputador2 = placarComputador2 + 1
            elif itens[computadorUm] == 'papel' and itens[computadorDois] == 'pedra':
                placarTeste2 = placarTeste2 + 1
            else:
                print("Empate")
        #Aqui apresentamos na tela o placar e perguntamos se a pessoa quer continuar jogando
        print("--- Placar ---")
        print(f' {placarTeste2} vs {placarComputador2}')
        menu = int(input('Se gostaria de continuar digite 3, se não, digite 5: '))
        #Caso a pessoa decida sair do modo o menu é apresentado novamente
        if menu != 1 and menu != 2 and menu != 3 and menu != 4:
            print("--- Menu Jokenpô ---")
            print("1 - humano x humano")
            print("2 - humano x computador")
            print("3 - computador x computador")
            print("4 - sair do jogo")
            menu = int(input("Escolha o modo de jogo: "))

    #Caso a pessoa decida parar de jogar, aqui encerramos o jogo.
    if menu == 4:
        print("Encerrando o jokenpô...")
        print("Muito obrigado, ")
        print("Alex Menegatti Secco, ")
        print("Ana Flávia Martins dos Santos, ")
        print("Isabella Vanderlinde Berkembrock, ")
        print("Mariana de Castro, ")
        print("Nicole Pereira Guarnieri!")
