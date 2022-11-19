# importações
from random import randint
from time import sleep
# pergunta para o start do jogo
while True:
    esc=int(input('Escolha entre: \n[1]PEDRA\n[2]PAPEL\n[3]TESOURA\n '))
    pc = randint(1, 3)
    print('O pc está escolhendo...')
    sleep(2)
    print('-'*50)
    # resutados
    if pc == 1:
        if esc == 1:
                print('Empate pois as escolhas foram iguais ')
                print('pc=PEDRA Sua escolha=PEDRA')
        elif esc == 2:
                print('Você ganhou pois o pc colocou pedra e você papel')
        elif esc == 3:
                print('Você perdeu pois o pc colocou pedra e você tesoura')
    if pc == 2:
        if esc == 1:
                print('Você perdeu pois o pc colocou papel e você pedra ')
        elif esc == 2:
                print('Empate pois as escolhas foram iguais')
                print('pc=PAPEL Sua escolha=PAPEL')
        elif esc == 3:
                print('Você ganhou pois o pc colocou papel e você tesoura')
    if pc == 3:
        if esc == 1:
            print('Você ganhou pois o pc colocou tesoura e você pedra ')
        elif esc == 2:
            print('Você perdeu pois o pc colocou tesoura e você papel')
        elif esc == 3:
            print('Empate pois as escolhas foram iguais')
            print('pc=TESOURA Sua escolha=TESOURA')
    if esc > 3:
            print('ERRO!,pois não existe essa escolha,tente novamente!')
    print('-'*50)
    per = str(input('Deseja continuar[S|N]')).strip().upper()[0]
    if per in 'N':
        break
    print('-'*50)
