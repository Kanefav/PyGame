from time import sleep


#Poderes Base Servant
PowerServant = {
'PowerServantHeal': 50,
'PowerServantAtq': 20}

#Poderes Base Logia
PowerLogia = {
'PowerLogiaHeal': 80,
'PowerLogiaAtq': 10}

#Poderes Base Arcanne
PowerArcanne = {
'PowerArcanneHeal': 60,
'PowerArcanneAtq': 15}

#Inimigo 1
PowerFirstInimigo = {
'PowerInimigoHeal': 40,
'PowerInimigoAtq': 5}

print('Bem Vindo ao Jogo de RPG Skypia')
PrimeiroInimigo = {'Nome':'FairGil', 'Classe':'Inimigo1'}
Prota = {'Nome':' ','Classe':''}
Prota['Nome'] = input(str('Digite Seu Nome:'))
sleep(1)
print('Escolha uma classe:\n'
      'Digite 1 para>> Servant: Você será como um Summoner, Invocara um Servo para que lute por você\n'
      'Digite 2 para>> Logia: Você será o seu próprio poder, Se tornará o Proprio Poder\n'
      'Digite 3 Para>> Arcanne: Você Será Como um Encantador, Poderá se Tornar um Servo')
ProtaTempClass = input(str('Escolha uma Classe: '))
if ProtaTempClass == '1':
    Prota['Classe'] = 'Servant'
if ProtaTempClass == '2':
    Prota['Classe'] = 'Logia'
if ProtaTempClass == '3':
    Prota['Classe'] = 'Arcanne'


def Battle(Prota, Inimigo):
    for c in range(0, 1):
         Inimigo['PowerInimigoHeal'] -= Prota['PowerServantAtq']
    print(f'Você Deu {Prota["PowerServantAtq"]} De ATQ no FairyGil(Inimigo1) que Agora está com {Inimigo["PowerInimigoHeal"]} de Vida')


Action = input(str('Agora que Você Criou seu Personagem Pode Fazer Algumas Açoes:\n'
        'Digite Pro Para>> Visualizar o Próprio Perfil\n'
        'Digite Battle Para>> Lutar com algum Inimigo')).capitalize()
if Action == 'Pro':
    print(Prota)
if Action == 'Battle':
    TempInimigo = input(str('Escolha algum Inimigo:'
                            'Digite 1 Para>> Inimigo Mais Fraco'))
    if TempInimigo == '1':
        Battle(PowerServant, PowerFirstInimigo)