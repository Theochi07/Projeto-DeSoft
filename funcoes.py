#exercício 1 

def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    for i in range(tamanho):
        if orientacao == "horizontal":
            posicoes.append([linha, coluna + i])
        elif orientacao == "vertical":
            posicoes.append([linha + i, coluna])
            
    return posicoes

    #execício 2

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicao)
    else:
        frota[nome_navio]= [posicao]

    return frota 

    #exercício 3

def faz_jogada (tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro 
     




    

