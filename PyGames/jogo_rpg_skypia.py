from time import sleep

TempInimigoHeal = 0
TempProtaHeal = 0


#Poderes Base Servant
PowerServant = {
'PowerProtaHeal': 50,
'PowerProtaAtq': 20}

#Poderes Base Logia
PowerLogia = {
'PowerProtaHeal': 80,
'PowerProtaAtq': 10}

#Poderes Base Arcanne
PowerArcanne = {
'PowerProtaHeal': 60,
'PowerProtaAtq': 15}

#Inimigo 1
PowerFirstInimigo = {
'InimigoName': 'FairGil',
'PowerInimigoHeal': 40,
'PowerInimigoAtq': 5}

#Inimigo 2
PowerSecondInimigo = {
'InimigoName': 'Illya-san',
'PowerInimigoHeal': 80,
'PowerInimigoAtq': 15}

print('Bem Vindo ao Jogo de RPG Skypia')
PrimeiroInimigo = {'Nome':'FairGil', 'Classe':'Inimigo1'}
Protagonista = {'Nome':' ','Classe':''}
Protagonista['Nome'] = input(str('Digite Seu Nome:'))
sleep(1)
print('Escolha uma classe:\n'
      'Digite 1 para>> Servant: Você será como um Summoner, Invocara um Servo para que lute por você\n'
      'Digite 2 para>> Logia: Você será o seu próprio poder, Se tornará o Proprio Poder\n'
      'Digite 3 Para>> Arcanne: Você Será Como um Encantador, Poderá se Tornar um Servo')
ProtaTempClass = input(str('Escolha uma Classe: '))
if ProtaTempClass == '1':
    Protagonista['Classe'] = 'Servant'
if ProtaTempClass == '2':
    Protagonista['Classe'] = 'Logia'
if ProtaTempClass == '3':
    Protagonista['Classe'] = 'Arcanne'


def Battle(Prota, Inimigo,):
            RoundCont = 0
            TempInimigoHeal = Inimigo['PowerInimigoHeal']
            TempProtaHeal = Prota['PowerProtaHeal']
            while TempInimigoHeal or TempProtaHeal == 0:
                if RoundCont ==  0:
                    input('Press Enter To Start Battle')

                TempInimigoHeal -= Prota['PowerProtaAtq']
                #Dano Protagonista
                print(f'{Protagonista["Nome"]} Deu {Prota["PowerProtaAtq"]}'
                      f' de Dano no {Inimigo["InimigoName"]} que Agora Está com {TempInimigoHeal} de Vida')
                if TempInimigoHeal <= 0:
                    return print(f'Parabéns Você ({Protagonista["Nome"]}) Ganhou, A batalha durou {RoundCont} Rodadas ')
                input('Press Enter to Continue')
                sleep(1)

                TempProtaHeal -= Inimigo['PowerInimigoAtq']
                #Dano Inimigo
                print(f'{Inimigo["InimigoName"]} Deu {Inimigo["PowerInimigoAtq"]}'
                      f' de Dano no {Protagonista["Nome"]} que Agora Está com {TempProtaHeal} de Vida')
                RoundCont += 1
                if TempProtaHeal <= 0:
                    return print(f'Você perdeu, A Batalha durou {RoundCont} Rodadas')
                input('Press Enter to Continue')
                sleep(1)
            if TempInimigoHeal == 0:
                print(f'Parabéns Você ({Protagonista["Nome"]}) Ganhou, A batalha durou {RoundCont} ')
            else:
                print('Você perdeu')



Action = input(str('Agora que Você Criou seu Personagem Pode Fazer Algumas Açoes:\n'
        'Digite Pro Para>> Visualizar o Próprio Perfil\n'
        'Digite Battle Para>> Lutar com algum Inimigo ')).capitalize()
if Action == 'Pro':
    print(Protagonista)
if Action == 'Battle':
    TempInimigo = input(str('Escolha algum Inimigo:\n'
                            'Digite 1 Para>> Inimigo Fraco\n'
                            'Digite 2 Para>> Inimigo Medio'))
    if TempInimigo == '1':
        if Protagonista['Classe'] == 'Servant':
            Battle(PowerServant, PowerFirstInimigo)
        if Protagonista['Classe'] == 'Logia':
            Battle(PowerLogia, PowerFirstInimigo)
        if Protagonista['Classe'] == 'Arcanne':
            Battle(PowerArcanne, PowerFirstInimigo)
    if TempInimigo == '2':
        if Protagonista['Classe'] == 'Servant':
            Battle(PowerServant, PowerSecondInimigo)
        if Protagonista['Classe'] == 'Logia':
            Battle(PowerLogia, PowerSecondInimigo)
        if Protagonista['Classe'] == 'Arcanne':
            Battle(PowerArcanne, PowerSecondInimigo)