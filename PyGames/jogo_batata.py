from random import randint
from time import sleep


# Chance de ganhar batata 50/50
def batata(a):
    cont = 0
    num = 0
    num = randint(1, 2)
    batata_quente = ''
    if num == 1:
        batata_quente = False
        print('Não é uma batata')
        print('Não foi dessa vez')
        print('Espere 2 segundos e tente novamente')
        sleep(2)
    elif num == 2:
        cont += 1
        batata_quente = True
        print('Hehe é uma batata')
        print(f'você ja encontrou {cont} batatas')


# Chance de ganhar batata 33.3/33.3
def batataa(a):
    cont = 0
    num1 = 0
    num1 = randint(1, 3)
    if num1 == 1:
        cont += 1
        batata = True
        print('hehe é uma batata')
        print(f'você ja encontrou {cont} batatas')
    else:
        num1 = False
        print('Não é uma batata')
        print('Espere 2 segundos e tente novamente')
        sleep(2)

# A batata
print('O seu objetivo é conseguir uma batata')

print('Para isso o senhor tem 2 escolhas que levam a tentativas diferentes')

print('Digite 1 para. Você ter 3 tentativas para tentar conseguir pegar uma batata'
    ', 50/50 (chance de conseguir a batata)')

print('Digite 2 para. Você ter 5 tentativas para tentar conseguir pegar uma batata'
    ', 33.3/33.3 (chance de conseguir uma batata)')
escolha = str(input('Escolha: '))
if escolha not in '12':
    print('Digite apenas 1 ou 2 para escolher cavalo manso, se errar de novo eu irei te morder')
    escolha = str(input('Escolha: '))
if escolha == '1':
    for c in range(0, 3):
        input('Aperte ENTER para fazer 1 tentativa')
        batata(1)

elif escolha == '2':
    for c in range(0, 4):
        input('Aperte ENTER para fazer 1 tentativa')
        batataa(1)
print('obrigado por jogar o meu jogo!')
