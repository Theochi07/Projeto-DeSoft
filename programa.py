from funcoes import *
import random

embarcacoes = {"porta-aviões": [1, 4], "navio-tanque": [2, 3], "contratorpedeiro": [3, 2], "submarino": [4, 1]}

frota = {}

for nome in embarcacoes:
    quantidade = embarcacoes[nome][0]
    tamanho = embarcacoes[nome][1]

    for i in range(quantidade):
        valida = False

        while not valida:
            print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')

            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            orientacao = 'vertical'
            escolha = 1

            if tamanho > 1:
                escolha = int(input('[1] Vertical [2] Horizontal >'))

                if escolha == 1:
                    orientacao = 'vertical'
                elif escolha == 2:
                    orientacao = 'horizontal'

            if escolha == 1 or escolha == 2:
                valida = posicao_valida(
                    frota, linha, coluna, orientacao, tamanho
                )

            if not valida:
                print('Esta posição não está válida!')

        frota = preenche_frota(
            frota, nome, linha, coluna, orientacao, tamanho
        )

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

total_navios = 0
for tipo in frota_oponente:
    total_navios += len(frota_oponente[tipo])

posicoes_atacadas = []
jogando = True

total_navios_jogador = 0
for tipo in frota:
    total_navios_jogador += len(frota[tipo])

posicoes_oponente = []

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_nova = False
    while not posicao_nova:
        linha_ataque = int(input('Jogador, qual linha deseja atacar? '))
        while linha_ataque < 0 or linha_ataque > 9:
            print('Linha inválida!')
            linha_ataque = int(input('Jogador, qual linha deseja atacar? '))

        coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))
        while coluna_ataque < 0 or coluna_ataque > 9:
            print('Coluna inválida!')
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar? '))

        if [linha_ataque, coluna_ataque] in posicoes_atacadas:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente!')
        else:
            posicoes_atacadas.append([linha_ataque, coluna_ataque])
            posicao_nova = True

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    else:
        posicao_oponente_nova = False
        while not posicao_oponente_nova:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)
            if [linha_oponente, coluna_oponente] not in posicoes_oponente:
                posicoes_oponente.append([linha_oponente, coluna_oponente])
                posicao_oponente_nova = True

        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == total_navios_jogador:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False


    