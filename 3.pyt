#jogo de pedra-papel-tesoura

#Tesoura>papel
#Papel>pedra
#Pedra>tesoura

jog1=input("Pedra, papel ou tesoura?")
jog2=input("Pedra, papel ou tesoura? \n")

if jog1==jog2:
    print("Empate")

elif jog1=="pedra":
    if jog2=="tesoura":
        print("jogador 1 venceu")
    else:
        print("jogador 2 venceu")

elif jog1=="tesoura":
    if jog2=="papel":
        print("jogador 1 venceu")
    else:
        print("jogador 2 venceu")

elif jog1=="papel":
    if jog2=="pedra":
        print("jogador 1 venceu")
    else:
        print("jogador 2 venceu")
    
    