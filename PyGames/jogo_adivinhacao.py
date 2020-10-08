from random import randint
print('''Sou Seu Computador
Acabei de Pensar em um Número Entre 0 e 10
Será que Voçe Consegue Adivinhar Qual Foi? ''')
cont = 0
num = int(randint(0, 10))
acertou = False
while not acertou:
    resp = int(input('Seu Palpite: '))
    cont += 1
    if resp == num:
        acertou = True
    else:
        if resp < num:
            print('Mais... Tente Mais uma Vez')
        elif resp > num:
            print('Menos... Tente Mais uma Vez')
print(f'Voçe Acertou Com {cont} Tentativas')