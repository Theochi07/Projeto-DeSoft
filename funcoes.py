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

    #exercício 4 

def posiciona_frota (frota):
    tabuleiro = []

    for i in range(10):
        linha = [0]*10
        tabuleiro.append(linha)

    for i in frota:
        navios = frota[i]

        for navio in navios:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1
        
    return tabuleiro 

    #execicio 5

def afundados(frota, tabuleiro):
    contador = 0

    for i in frota:
        navios = frota[i]

        for navio in navios:
            navio_afundado = True

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                if tabuleiro[linha][coluna] != "X":
                    navio_afundado = False

            if navio_afundado == True:
                contador += 1

    return contador

    #exercicio 6 

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    for numeros in posicoes:
        linha = numeros[0]
        coluna = numeros[1]
        if linha > 9 or coluna > 9 or linha < 0 or coluna < 0:
            return False
        
    for posicao in posicoes:           
        for tipo in frota:
            navios = frota[tipo]
            for navio in navios:
                if posicao in navio:
                    return False
    return True    
                  

