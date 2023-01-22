#  11
# 11
def posicionar(mapa, linha, coluna):
    if coluna < 0 or coluna > len(mapa[0]) - 3:
        return -1

    # Linha 0
    condicao1 = mapa[linha][coluna] == 0
    condicao2 = mapa[linha][coluna+1] == 0
    if linha == 0 and condicao1 and condicao2:
        mapa[linha][coluna] = 5
        mapa[linha][coluna+1] = 5
        return (linha, coluna, 1)

    # Linha >= 1
    condicao3 = mapa[linha-1][coluna+1] == 0
    condicao4 = mapa[linha-1][coluna+2] == 0
    if linha >= 1 and condicao1 and condicao2 and condicao3 and condicao4:
        mapa[linha][coluna] = 5
        mapa[linha][coluna+1] = 5
        mapa[linha-1][coluna+1] = 5
        mapa[linha-1][coluna+2] = 5
        return (linha, coluna, 1)
    
    return -1

#  11
# 11
def remover(mapa, linha, coluna):
    if linha == 0:
        mapa[linha][coluna] = 0
        mapa[linha][coluna+1] = 0

    elif linha >= 1:
        mapa[linha][coluna] = 0
        mapa[linha][coluna+1] = 0
        mapa[linha-1][coluna+1] = 0
        mapa[linha-1][coluna+2] = 0

#  11
# 11
def espaco_esquerda(mapa, linha, coluna):
    if coluna == 0:
        return False

    condicao1 = mapa[linha][coluna-1] == 0
    condicao2 = mapa[linha-1][coluna] == 0

    return condicao1 and condicao2

#  11
# 11
def espaco_direita(mapa, linha, coluna):
    if coluna >= len(mapa[0]) - 3:
        return False

    condicao1 = mapa[linha][coluna+2] == 0
    condicao2 = mapa[linha-1][coluna+3] == 0

    return condicao1 and condicao2