import pecas, engine
import pygame, time, random, sys

class Tetrizzz3:
    def __init__(self):
        self.tamanho_bloco = 40
        self.base_blocos = 10
        self.altura_blocos = 16
        self.altura = self.tamanho_bloco * self.altura_blocos
        self.largura = self.tamanho_bloco * self.base_blocos
        self.engine = engine.Engine(self.largura, self.altura, self.base_blocos, self.altura_blocos)
        self.matriz = []
        self.criar_matriz()
        self.isA = False
        self.isD = False
        self.isS = False
        self.isSPC = False
        self.reiniciou = False
        linha_atual = 0
        coluna_atual = int(self.base_blocos / 2)
        self.vetor2 = [linha_atual, coluna_atual]
        self.rotacao_atual = random.randint(1, 4)
        self.peca_atual = random.randint(1, 7)
        self.clock2 = 0
        self.pontos = 0
        self.clock = pygame.time.Clock()
        self.pausado = False

    def iniciar_valores(self):
        self.isA = False
        self.isD = False
        self.isS = False
        self.reiniciou = False
        linha_atual = 0
        coluna_atual = int(self.base_blocos / 2)
        self.vetor2 = [linha_atual, coluna_atual]
        self.rotacao_atual = random.randint(1, 4)
        self.peca_atual = random.randint(1, 7)
        self.clock2 = 0

    def criar_matriz(self):
        linha_vazia = []
        for i in range(self.base_blocos):
            linha_vazia.append(0)

        for i in range(self.altura_blocos):
            self.matriz.append(linha_vazia.copy())

    def desenhar_blocos(self):
        vetores2 = pecas.obter_coordenadas(self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
        for vetor2 in vetores2:
            self.engine.desenhar_bloco(vetor2, self.peca_atual)
        self.engine.update(self.pontos)

    def remover_blocos(self):
        vetores2 = pecas.obter_coordenadas(self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
        for vetor2 in vetores2:
            self.engine.remover_bloco(vetor2)

    def obter_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pausado = not self.pausado
                elif event.key == pygame.K_a:
                    self.isA = True
                    continue
                elif event.key == pygame.K_d:
                    self.isD = True
                    continue
                elif event.key == pygame.K_w:
                    if not self.pausado:
                        self.remover_blocos()
                        linha, coluna, rotacao = pecas.rotacionar_peca(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                        self.vetor2 = [linha, coluna]
                        self.rotacao_atual = rotacao
                        self.desenhar_blocos()
                        continue
                elif event.key == pygame.K_SPACE:
                    if not self.pausado:
                        self.isSPC = True
                        continue
                elif event.key == pygame.K_s:
                    self.isS = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.isA = False
                elif event.key == pygame.K_d:
                    self.isD = False
                elif event.key == pygame.K_s:
                    self.isS = False

    def verificar_linhas(self):
        range_linha = len(self.matriz) - 1
        for linha in range(range_linha, -1, -1):
            if not (self.contem_0(self.matriz[linha])):
                self.swap_baixo(linha)
                self.redesenhar()
                self.pontos += 1000
                self.verificar_linhas()
                return
            elif not self.matriz[linha]:
                return

    def redesenhar(self):
        self.engine.limpar()
        for linha in range(self.altura_blocos - 1, -1, -1):
            for coluna in range(self.base_blocos):
                self.engine.desenhar_bloco([linha, coluna], self.matriz[linha][coluna])
        self.engine.update(self.pontos)

    def swap_baixo(self, linha):
        for linha in range(linha, 0, -1):
            if self.matriz[linha] == []:
                break
            self.matriz[linha] = self.matriz[linha - 1].copy()

    def contem_0(self, linha):
        for i in linha:
            if i == 0:
                return True
        return False

    def descer_tudo(self):
        self.remover_blocos()
        linha = self.vetor2[0]
        linha_backup = self.vetor2[0]
        coluna = self.vetor2[1]
        while linha != -1:
            linha, coluna, posicao = pecas.mover_baixo(self.matriz, linha, coluna, self.peca_atual, self.rotacao_atual)
            if linha != -1:
                linha_backup = linha
            self.pontos += 30
        self.vetor2[0] = linha_backup
        self.vetor2[1] = coluna
        self.desenhar_blocos()
        self.verificar_linhas()
        self.vetor2[0] = 0
        self.reiniciou = True
        self.isSPC = False

    def perdeu(self):
        self.__init__()

    def next(self):
        if not self.pausado:
            self.obter_inputs()
            if self.vetor2[0] == 0 and self.reiniciou:
                self.peca_atual = random.randint(1, 7)
                self.rotacao_atual = random.randint(1, 4)
                self.vetor2[1] = int(self.base_blocos / 2) - 1
                self.reiniciou = False
                pecas.desenhar_peca(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                self.desenhar_blocos()

            if self.isA and pecas.espaco_esquerda(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual,
                                                  self.rotacao_atual):
                self.remover_blocos()
                self.vetor2[0], self.vetor2[1], self.rotacao_atual = pecas.mover_esquerda(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                self.desenhar_blocos()

            elif self.isD and pecas.espaco_direita(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual):
                self.remover_blocos()
                self.vetor2[0], self.vetor2[1], self.rotacao_atual = pecas.mover_direita(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                self.desenhar_blocos()

            elif self.isSPC:
                self.descer_tudo()

            if self.clock2 >= 8:
                nova_linha, coluna, rotacao = pecas.mover_baixo(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                if nova_linha == -1 and self.vetor2[0] == 0:
                    self.perdeu()
                elif nova_linha != -1:
                    self.remover_blocos()
                    self.vetor2[0] = nova_linha
                    self.desenhar_blocos()
                else:
                    self.reiniciou = True
                    self.verificar_linhas()
                    self.vetor2[0] = 0

            if self.isS:
                self.clock2 = (self.clock2 + 6) % 10
                self.pontos += 1
                time.sleep(0.007)
                return
            else:
                self.clock2 = (self.clock2 + 1) % 9

            self.clock.tick(15)
        else:
            self.obter_inputs()
            self.desenhar_blocos()
            self.clock.tick(15)

    def game_loop(self):
        while True:
            if not self.pausado:
                self.obter_inputs()
                if self.vetor2[0] == 0 and self.reiniciou:
                    self.peca_atual = random.randint(1, 7)
                    self.rotacao_atual = random.randint(1, 4)
                    self.vetor2[1] = int(self.base_blocos / 2) - 1
                    self.reiniciou = False
                    pecas.desenhar_peca(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual, self.rotacao_atual)
                    self.desenhar_blocos()

                if self.isA and pecas.espaco_esquerda(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual,
                                                      self.rotacao_atual):
                    self.remover_blocos()
                    self.vetor2[0], self.vetor2[1], self.rotacao_atual = pecas.mover_esquerda(self.matriz, self.vetor2[0],self.vetor2[1],self.peca_atual,self.rotacao_atual)
                    self.desenhar_blocos()

                elif self.isD and pecas.espaco_direita(self.matriz, self.vetor2[0], self.vetor2[1], self.peca_atual,self.rotacao_atual):
                    self.remover_blocos()
                    self.vetor2[0], self.vetor2[1], self.rotacao_atual = pecas.mover_direita(self.matriz, self.vetor2[0],self.vetor2[1],self.peca_atual,self.rotacao_atual)
                    self.desenhar_blocos()

                elif self.isSPC:
                    self.descer_tudo()

                if self.clock2 >= 8:
                    nova_linha, coluna, rotacao = pecas.mover_baixo(self.matriz, self.vetor2[0], self.vetor2[1],self.peca_atual, self.rotacao_atual)
                    if nova_linha == -1 and self.vetor2[0] == 0:
                        self.perdeu()
                    elif nova_linha != -1:
                        self.remover_blocos()
                        self.vetor2[0] = nova_linha
                        self.desenhar_blocos()
                    else:
                        self.reiniciou = True
                        self.verificar_linhas()
                        self.vetor2[0] = 0

                if self.isS:
                    self.clock2 = (self.clock2 + 6) % 10
                    self.pontos += 1
                    time.sleep(0.007)
                    continue
                else:
                    self.clock2 = (self.clock2 + 1) % 9

                self.clock.tick(15)
            else:
                self.obter_inputs()
                self.desenhar_blocos()
                self.clock.tick(5)