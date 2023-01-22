import i1, i2

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1

    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return i1.posicionar(mapa, linha, coluna)
        case 2:
            return i2.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return i1.remover(mapa, linha, coluna)
        case 2:
            return i2.remover(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return i1.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return i2.espaco_esquerda(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return i1.espaco_direita(mapa, linha, coluna)
        case 2:
            return i2.espaco_direita(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            # 1
            # 1 -> 1111
            # 1
            # 1
            if linha - 2 < 0:
                return (linha, coluna, 1)

            i1.remover(mapa, linha, coluna)
            resultado = i2.posicionar(mapa, linha-2, coluna-1)
            if resultado == -1:
                resultado = i2.posicionar(mapa, linha-2, coluna-3)
            if resultado == -1:
                resultado = i2.posicionar(mapa, linha-2, coluna)
            if resultado == -1:
                return i1.posicionar(mapa, linha, coluna)
            return resultado
        case 2:
            #         1
            # 1111 -> 1
            #         1
            #         1
            if linha >= len(mapa) - 2:
                return (linha, coluna, 2)
            
            i2.remover(mapa, linha, coluna)
            resultado = i1.posicionar(mapa, linha+2, coluna+1)
            if resultado == -1:
                return i2.posicionar(mapa, linha, coluna)
            return resultado