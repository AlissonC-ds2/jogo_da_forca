from pacotes.modulos.modulos_tela import cor

def verificar_letras(letras, palavra_secreta):
    if letras == palavra_secreta:
        return True
    return False

def ler_regras():
    print(cor.PRETO + '|'*140)
    print('Jogo da forca consiste em escolher uma palavra e fazer o seu adversario adivinhar ela, a cada letra errada um pedaço do corpo é desenhado.')
    print('Se todas as partes do corpo do boneco forem desenhadas, você perde.')
    print('O jogo vai ser uma melhor de 3 alternando entre o jogador desafiante e o desafiado.')
    print('Cada jogador tem 6 vidas, quem chega a 0 sem descobrir a palavra perde a rodada.')
    print('O jogador ainda pode escolher em adivinhar a palavra inteira, porém se ele errar ele perde a rodada.')
    print('|'*140 + cor.FIM)

def alternar_jogadores(rodadas, jogador_1, jogador_2):
    if rodadas == 0 or rodadas == 2:
        print(cor.ROXO + f'Vez do jogador "{jogador_1}" adivinhar.\nJogador: "{jogador_2}" sua vez de escolher uma palavra.' + cor.FIM)
        return jogador_1
    elif rodadas == 1:
        print(cor.ROXO + f'Vez do jogador "{jogador_2}" adivinhar.\nJogador: "{jogador_1}" sua vez de escolher uma palavra.' + cor.FIM)
        return jogador_2
