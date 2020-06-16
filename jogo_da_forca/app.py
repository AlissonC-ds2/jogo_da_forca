from pacotes.modulos.modulo_inputs import definir_jogador, definir_desafiador, escolher_palavra, adivinhar_letras,chutar_palavra
from pacotes.modulos.modulos_tela import mostrar_forca, desenha_forca, jogador_enforcado, mostrar_pontuacao, inicio, opcoes, cor
from pacotes.modulos.Verificacao_e_regras import verificar_letras, alternar_jogadores, ler_regras

def jogo():
    jogador_1 = definir_jogador()
    jogador_2 = definir_desafiador()
    jogador1_pontos = 0
    jogador2_pontos = 0

    for rodadas in range(0, 3):
        mostrar_pontuacao(jogador_1, jogador_2, jogador1_pontos, jogador2_pontos)
        vidas = 7 #7 vidas para cada jogador em cada rodada
        jogador_da_vez = alternar_jogadores(rodadas, jogador_1, jogador_2)
        palavra_secreta = escolher_palavra(jogador_da_vez)
        tamanho_palavra = "_" * len(palavra_secreta)
        lista_palavra = list(tamanho_palavra)#unica maneira que encontrei para dar .join nas letras corretas
        rodada_finalizada = False

        while not rodada_finalizada:
            adivinhar = adivinhar_letras()
            if len(adivinhar) > 1:
                chute = chutar_palavra(palavra_secreta)
                if not chute:
                    if jogador_da_vez == jogador_1:
                        jogador2_pontos += 1#se o jogador1 errar o ponto vai pro jogador 2
                        rodada_finalizada = True
                    elif jogador_da_vez == jogador_2:#mesma lógica só muda o player
                        jogador1_pontos += 1
                        rodada_finalizada = True
                if chute is True:
                    if jogador_da_vez == jogador_1:
                        jogador1_pontos += 1
                        rodada_finalizada = True
                    elif jogador_da_vez == jogador_2:
                        jogador2_pontos += 1
                        rodada_finalizada = True
                else:
                    continue
            elif adivinhar in palavra_secreta:
                desenha_forca(vidas)
                letras = mostrar_forca(lista_palavra, adivinhar, palavra_secreta)#mostra as letras inseridas
                palavra_descoberta = verificar_letras(letras, palavra_secreta)#verifica se a palavra foi descoberta
                if palavra_descoberta:
                    if jogador_da_vez == jogador_1:
                        jogador1_pontos += 1
                        rodada_finalizada = True
                        print(cor.VERDE + f'Parabéns "{jogador_da_vez}" você venceu a {rodadas}º rodada.' + cor.FIM)
                    else:
                        jogador2_pontos += 1
                        rodada_finalizada = True
                        print(cor.VERDE + f'Parabéns "{jogador_da_vez}" você venceu a {rodadas}º rodada.' + cor.FIM)
            else:
                vidas -= 1
                desenha_forca(vidas)#desenha o bonequinho
                mostrar_forca(lista_palavra, adivinhar, palavra_secreta)
                if vidas == 0:
                    if jogador_da_vez == jogador_1:
                        jogador2_pontos += 1
                        jogador_enforcado(jogador_da_vez, palavra_secreta)
                        rodada_finalizada = True
                    elif jogador_da_vez == jogador_2:
                        jogador1_pontos += 1
                        jogador_enforcado(jogador_da_vez, palavra_secreta)#printa uma mensagem
                        rodada_finalizada = True
                else:
                    print(cor.AMARELO + f'Essa letra não está contida na palavra.Você ainda tem {vidas} vidas.' + cor.FIM)

        if jogador1_pontos == 2:
            mostrar_pontuacao(jogador_1, jogador_2, jogador1_pontos, jogador2_pontos)
            print(cor.VERDE + f'Parabéns: {jogador_1} você ganhou a partida.' + cor.FIM)
            break
        elif jogador2_pontos == 2:
            mostrar_pontuacao(jogador_1, jogador_2, jogador1_pontos, jogador2_pontos)
            print(cor.VERDE + f'Parabéns: {jogador_2} você ganhou a partida.' + cor.FIM)
            break

def menu():
    inicio(cor)
    while True:
        opcoes()
        escolha = int(input(cor.X + 'O que deseja fazer? ' + cor.FIM))
        if escolha == 1:
            jogo()
        elif escolha == 2:
            ler_regras()
        elif escolha == 3:
            print(cor.PRETO + 'Até...' + cor.FIM)
            exit()

menu()