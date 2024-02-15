import t1, t2, t3, t4

def posicionar(mapa, linha, coluna, posicao):
    if linha == len(mapa):
        return -1

    match posicao:
        case 1:
            return t1.posicionar(mapa, linha, coluna)
        case 2:
            return t2.posicionar(mapa, linha, coluna)
        case 3:
            return t3.posicionar(mapa, linha, coluna)
        case 4:
            return t4.posicionar(mapa, linha, coluna)

def remover(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return t1.remover(mapa, linha, coluna)
        case 2:
            return t2.remover(mapa, linha, coluna)
        case 3:
            return t3.remover(mapa, linha, coluna)
        case 4:
            return t4.remover(mapa, linha, coluna)

def espaco_esquerda(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return t1.espaco_esquerda(mapa, linha, coluna)
        case 2:
            return t2.espaco_esquerda(mapa, linha, coluna)
        case 3:
            return t3.espaco_esquerda(mapa, linha, coluna)
        case 4:
            return t4.espaco_esquerda(mapa, linha, coluna)

def espaco_direita(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            return t1.espaco_direita(mapa, linha, coluna)
        case 2:
            return t2.espaco_direita(mapa, linha, coluna)
        case 3:
            return t3.espaco_direita(mapa, linha, coluna)
        case 4:
            return t4.espaco_direita(mapa, linha, coluna)

def rotacionar(mapa, linha, coluna, posicao):
    match posicao:
        case 1:
            #         1
            # 111 -> 11
            #  1      1
            t1.remover(mapa, linha, coluna)
            resultado = t2.posicionar(mapa, linha, coluna)
            if resultado == -1:
                return t1.posicionar(mapa, linha, coluna)
            return resultado
        case 2:
            #  1     1
            # 11 -> 111
            #  1
            t2.remover(mapa, linha, coluna)
            resultado = t3.posicionar(mapa, linha-1, coluna)
            if resultado == -1:
                resultado = t3.posicionar(mapa, linha-1, coluna-1)
            
            if resultado == -1:
                return t2.posicionar(mapa, linha, coluna)

            return resultado
        case 3:
            #  1     1
            # 111 -> 11
            #        1
            if linha == len(mapa)-1:
                return (linha, coluna, 3)

            t3.remover(mapa, linha, coluna)
            resultado = t4.posicionar(mapa, linha+1, coluna+1)
            if resultado == -1:
                return t3.posicionar(mapa, linha, coluna)
            return resultado
        case 4:
            # 1 
            # 11 -> 111
            # 1      1
            t4.remover(mapa, linha, coluna)
            resultado = t1.posicionar(mapa, linha, coluna-1)
            if resultado == -1:
                resultado = t1.posicionar(mapa, linha, coluna)
            
            if resultado == -1:
                return t4.posicionar(mapa, linha, coluna)
                
            return resultado

def obter_coordenadas(linha, coluna, posicao):
    match posicao:
        case 1: return [[linha-1, coluna], [linha, coluna+1], [linha-1, coluna+1], [linha-1, coluna+2]]
        case 2: return [[linha-1, coluna], [linha, coluna+1], [linha-1, coluna+1], [linha-2, coluna+1]]
        case 3: return [[linha, coluna], [linha, coluna+1], [linha, coluna+2], [linha-1, coluna+1]]
        case 4: return [[linha, coluna], [linha-1, coluna], [linha-1, coluna+1], [linha-2, coluna]]