class cor:
    ROXO = '\033[1;35;48m'
    AZUL = '\033[1;34;48m'
    VERDE = '\033[1;32;48m'
    AMARELO = '\033[1;33;48m'
    VERMELHO = '\033[1;31;48m'
    PRETO = '\033[1;30;48m'
    FIM = '\033[1;37;0m'
    X = "\33[1;36m"

def opcoes():
    print(cor.ROXO + '#'*35)
    print('1. Jogar o jogo da forca.')
    print('2. Ler as regras do jogo')
    print('3. Sair')
    print('#'*35 + cor.FIM)

def mostrar_pontuacao(jogador_1, jogador_2, jogador1_pontos , jogador2_pontos):
    print(cor.VERDE + '=*'*15)
    print(f'Pontos do {jogador_1} : {jogador1_pontos}')
    print(cor.VERDE + f'Pontos do {jogador_2} : {jogador2_pontos}')
    print(cor.VERDE + '=*'*15 + cor.FIM)

def inicio(cor):
    print(cor.VERMELHO + '=*'*15 + cor.FIM)
    print(cor.VERMELHO + 'BEM VINDO AO JOGO DA FORCA' + cor.FIM)
    print(cor.VERMELHO + '=*'*15 + cor.FIM)

def jogador_enforcado(jogador_da_vez, palavra_secreta):
    print(cor.VERMELHO + f'"{jogador_da_vez}" foi enforcado e perdeu a rodada.\nA palavra secreta era: {palavra_secreta}' + cor.FIM)

def mostrar_forca(lista_palavra,adivinhar,palavra_secreta):
    for i, letra_correta, in enumerate(palavra_secreta):
        if letra_correta in adivinhar and len(adivinhar) == 1:#len precisa ser igual a 1, caso ao contrário o jogador vai tentar chutar a palavra
            lista_palavra[i] = adivinhar #se a letra for igual ao que o jogador adivinhou ele vai substituir dentro da lista palavra no Index correto

    letra = "".join(lista_palavra) #Dando .join se a letra for a correta e nomeando uma variavel para retornar um valor.
    print('    ',letra)
    return letra

def desenha_forca(vidas):
    tentativa = [
    '''
    |-----
    |    | 
    |    O 
    |   /|\\ 
    |    | 
    |   / \\ 
    |
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\\ 
    |    | 
    |   / 
    |
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\\ 
    |    | 
    |    
    |        
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /|\\ 
    |   
    |    
    |       
    ''',
    '''
    |-----
    |    | 
    |    O 
    |   /| 
    |   
    |    
    |       
    ''',
    '''
    |-----
    |    | 
    |    O 
    |    | 
    |   
    |
    |    
    ''',
     '''
    |-----
    |    | 
    |    O 
    |     
    |   
    |    
    |    
    ''',
    '''
    |-----
    |    | 
    |     
    |     
    |   
    |    
    |
    |   
    '''
    ]
    print(tentativa[vidas])
