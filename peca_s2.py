import s21, s22

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1

    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s21.posicionar(mapa, linha, coluna)
        case 2:
            return s22.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s21.remover(mapa, linha, coluna)
        case 2:
            return s22.remover(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s21.espaco_direita(mapa, linha, coluna)
        case 2:
            return s22.espaco_direita(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            return s21.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return s22.espaco_esquerda(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):
    if posicao > 2:
        posicao -= 2

    match posicao:
        case 1:
            # 11      1
            #  11 -> 11
            #        1
            if linha == len(mapa)-1:
                return (linha, coluna, 1)

            s21.remover(mapa, linha, coluna)
            resultado = s22.posicionar(mapa, linha+1, coluna)
            if resultado == -1:
                return s21.posicionar(mapa, linha, coluna)
            return resultado

        case 2:
            #  1    11
            # 11 ->  11
            # 1
            s22.remover(mapa, linha, coluna)
            resultado = s21.posicionar(mapa, linha-1, coluna)
            if resultado == -1:
                resultado = s21.posicionar(mapa, linha-1, coluna-1)

            if resultado == -1:
                return s22.posicionar(mapa, linha, coluna)

            return resultado