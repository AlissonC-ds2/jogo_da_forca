from pacotes.modulos.modulos_tela import desenha_forca, cor
from unicodedata import normalize

def definir_jogador():
    jogador1 = str(input(cor.X + 'Nome do jogador: ' + cor.FIM)).upper()
    return cor.VERMELHO + jogador1 + cor.FIM

def definir_desafiador():
    jogador2 = str(input(cor.X + 'Nome do desafiador: ' + cor.FIM)).upper()
    return cor.AZUL + jogador2 + cor.FIM

def escolher_palavra(jogador):
    while True:
        escolher = str(input(cor.X + f'Escolha uma palavra para o "{jogador}" adivinhar: ' + cor.FIM)).lower()
        if not escolher.isalpha():
            print(cor.VERMELHO + 'Não utilize símbolos ou números para formar uma palavra.' + cor.FIM)
        elif len(escolher) <= 1:
            print(cor.AMARELO + 'Por favor digite uma "PALAVRA" maior para o jogador adivinhar.' + cor.FIM)
        else:
            break
    return normalize('NFKD',escolher).encode('ASCII', 'ignore').decode('ASCII')#retorna o valor sem os acentos

def chutar_palavra(palavra_secreta):
    while True:
        escolha = str(input(cor.X + 'Tem certeza que deseja chutar uma palavra? S/N ' + cor.FIM))
        if escolha in 'Nn':
            return 'Nn' #retorna qualquer coisa apenas para cair no else da main function
        else:
            chutar = str(input(cor.X + 'Chutar a palavra: ' + cor.FIM)).lower()
            if chutar == palavra_secreta:
                print(cor.PRETO + f'Parabéns você acertou na mosca.\nA palavra é: {palavra_secreta} \nVocê ganhou a rodada.' + cor.FIM)
                chutar = True
                return chutar
            else:
                desenha_forca(vidas=0)#retorna o bonequinho enforcado indicando que o jogador perdeu.
                print(cor.VERMELHO + f'Você errou o seu chute e perdeu a rodada.\nA palavra era: {palavra_secreta}' + cor.FIM)
                chutar = False#aqui é true, só to testando uma coisa
                return chutar

def adivinhar_letras():
    while True:
        adivinhar_letra = str(input(cor.X + 'Tente adivinhar a letra: ' + cor.FIM)).lower()
        if not adivinhar_letra.isalpha():
            print(cor.PRETO + 'Por favor informe uma "LETRA".\nTente novamente, isso não te custou uma vida.' + cor.FIM)
        else:
            break
    return adivinhar_letra
