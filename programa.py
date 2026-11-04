    #exercício 7 
embarcacoes = {"porta-aviões": [1,4], 'navio-tanque': [2,3], 'contratorpedeiro': [3,2], 'submarino': [4,1]}

frota = {}

for nome in embarcacoes:
    quantidade = embarcacoes[nome][0]
    tamanho = embarcacoes[nome][1]

    for i in range (quantidade):


        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        
        valida = False

        while not valida:
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

        posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
        frota = preenche_frota(frota, nome, posicoes)

print(frota)



    