from random import randint
from time import sleep
esc=int(input('Escolha entre: \n[1]PEDRA\n[2]PAPEL\n[3]TESOURA\n '))
pc=randint(1,3)
print('O pc está escolhendo...')
sleep(5)
print('-'*50)
if pc==1:
    if esc==1:
        print('Empate pois as escolhas foram iguais ')
        print('pc=PEDRA Sua escolha=PEDRA')
    elif esc==2:
        print('Vc ganhou pois o pc colocou pedra e vc papel')
    elif esc==3:
        print('Vc perdeu pois o pc colocou pedra e vc tesoura')
if pc==2:
    if esc==1:
        print('Vc perdeu pois o pc colocou papel e vc pedra ')
    elif esc==2:
        print('Empate pois as escolhas foram iguais')
        print('pc=PAPEL Sua escolha=PAPEL')
    elif esc==3:
        print('Vc ganhou pois o pc colocou papel e vc tesoura')
if pc==3:
    if esc==1:
        print('Vc ganhou pois o pc colocou tesoura e vc pedra ')
    elif esc==2:
        print('Vc perdeu pois o pc colocou tesoura e vc papel')
    elif esc==3:
        print('Empate pois as escolhas foram iguais')
        print('pc=TESOURA Sua escolha=TESOURA')
if esc>3:
    print('ERRO!,pois não existe essa escolha,tente novamente!')
print('-'*50)

