import peca_i, peca_l, peca_o, peca_s, peca_t

def desenhar_peca(mapa, linha, coluna, id_peca, posicao):
    if id_peca == 1:
        return peca_t.posicionar(mapa, linha, coluna, posicao)
    if id_peca == 2:
        return peca_o.posicionar(mapa, linha, coluna)
    if id_peca == 3:
        return peca_l.posicionar(mapa, linha, coluna, posicao)
    if id_peca == 4:
        return peca_i.posicionar(mapa, linha, coluna, posicao)
    if id_peca == 5:
        return peca_s.posicionar(mapa, linha, coluna, posicao)

def remover_peca(mapa, linha, coluna, id_peca, posicao):
    if id_peca == 1:
        peca_t.remover(mapa, linha, coluna, posicao)
    elif id_peca == 2:
        peca_o.remover(mapa, linha, coluna)
    elif id_peca == 3:
        peca_l.remover(mapa, linha, coluna, posicao)
    elif id_peca == 4:
        peca_i.remover(mapa, linha, coluna, posicao)
    elif id_peca == 5:
        peca_s.remover(mapa, linha, coluna, posicao)
    

def rotacionar_peca(mapa, linha, coluna, id_peca, posicao_atual):
    if id_peca == 1:
        return peca_t.rotacionar(mapa, linha, coluna, posicao_atual)
    if id_peca == 2:
        return (linha, coluna, posicao_atual)
    if id_peca == 3:
        return peca_l.rotacionar(mapa, linha, coluna, posicao_atual)
    if id_peca == 4:
        return peca_i.rotacionar(mapa, linha, coluna, posicao_atual)
    if id_peca == 5:
        return peca_s.rotacionar(mapa, linha, coluna, posicao_atual)

def mover_baixo(mapa, linha_atual, coluna, id_peca, posicao):
    remover_peca(mapa, linha_atual, coluna, id_peca, posicao)
    if desenhar_peca(mapa, linha_atual+1, coluna, id_peca, posicao) == -1:
        desenhar_peca(mapa, linha_atual, coluna, id_peca, posicao)
        return (-1, coluna, posicao)
    return (linha_atual + 1, coluna, posicao)


def mover_esquerda(mapa, linha, coluna_atual, id_peca, posicao):
    remover_peca(mapa, linha, coluna_atual, id_peca, posicao)
    if desenhar_peca(mapa, linha, coluna_atual-1, id_peca, posicao) == -1:
        desenhar_peca(mapa, linha, coluna_atual, id_peca, posicao)
        return (linha, -1, posicao)
    return (linha, coluna_atual - 1, posicao)

def mover_direita(mapa, linha, coluna_atual, id_peca, posicao):
    remover_peca(mapa, linha, coluna_atual, id_peca, posicao)
    if desenhar_peca(mapa, linha, coluna_atual+1, id_peca, posicao) == -1:
        desenhar_peca(mapa, linha, coluna_atual, id_peca, posicao)
        return (linha, -1, posicao)
    return (linha, coluna_atual + 1, posicao)

def espaco_esquerda(mapa, linha, coluna, id_peca, posicao):
    match id_peca:
        case 1:
            return peca_t.espaco_esquerda(mapa, linha, coluna, posicao)
        case 2:
            return peca_o.espaco_esquerda(mapa, linha, coluna)
        case 3:
            return peca_l.espaco_esquerda(mapa, linha, coluna, posicao)
        case 4:
            return peca_i.espaco_esquerda(mapa, linha, coluna, posicao)
        case 5:
            return peca_s.espaco_esquerda(mapa, linha, coluna, posicao)

def espaco_direita(mapa, linha, coluna, id_peca, posicao):
    match id_peca:
        case 1:
            return peca_t.espaco_direita(mapa, linha, coluna, posicao)
        case 2:
            return peca_o.espaco_direita(mapa, linha, coluna)
        case 3:
            return peca_l.espaco_direita(mapa, linha, coluna, posicao)
        case 4:
            return peca_i.espaco_direita(mapa, linha, coluna, posicao)
        case 5:
            return peca_s.espaco_direita(mapa, linha, coluna, posicao)

