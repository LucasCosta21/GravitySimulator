import pygame, math
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()
COMPRIMENTO_TELA = 1024
ALTURA_TELA = 700
G = 0.06

class Planeta:
    def __init__(self, nome, raio, massa, cor, pontoX, pontoY, angulo, modulo):
        self.nome = nome,
        self.raio = raio
        self.massa = massa
        self.cor = cor
        self.posX = pontoX
        self.posY = pontoY
        self.angulo = angulo
        self.modulo = modulo
        self.velX = modulo * math.sin(math.radians(angulo))
        self.velY = modulo * math.cos(math.radians(angulo))

    def Mover(self, modulo, angulo):
        self.velX += modulo * math.sin(math.radians(angulo + 90))
        self.velY += modulo * math.cos(math.radians(angulo + 90))
        self.posX += self.velX
        self.posY += self.velY

    def Desenhar(self, screen):
        pygame.draw.circle(screen, self.cor, (int(math.floor(self.posX)), int(math.floor(self.posY))), self.raio)

class Sistema:
    def __init__(self, planetas): # Inicializa os dados do sistema (constantes, tamanho da tela, etc)
        self.win = pygame.display.set_mode([COMPRIMENTO_TELA, ALTURA_TELA])
        self.planetas = planetas

    def loop(self):
        self.win.fill((0, 0, 0))
        self.movimentaPlanetas()
        pygame.display.update()
        pygame.display.flip()

    def movimentaPlanetas(self):
        for planeta in self.planetas:
            vetor = self.calculaVetor(planeta)
            planeta.Mover(vetor[0], vetor[1])
            planeta.Desenhar(self.win)

    def calculaVetor(self, planeta):
        forca = 0.0
        angulo = 0.0
        for outroPlaneta in self.planetas:
            if planeta.nome != outroPlaneta.nome:
                distancia = self.calculaDistancia(planeta, outroPlaneta)
                forca = (G * planeta.massa * outroPlaneta.massa)/distancia
                angulo = self.calculaAngulo(planeta, outroPlaneta)
        return [forca, angulo]

    def calculaAngulo(self, corpo1, corpo2):
        catetoAdjacente = corpo1.posX - corpo2.posX
        catetoOposto = corpo1.posY - corpo2.posY
        if catetoAdjacente > 0:
            if catetoOposto > 0:
                return math.atan(catetoAdjacente/catetoOposto) + 270
            elif catetoOposto == 0:
                return 180
            elif catetoOposto < 0:
                return math.atan(catetoAdjacente/catetoOposto)
        elif catetoAdjacente == 0:
            if catetoOposto > 0:
                return 90
            elif catetoOposto == 0:
                return corpo1.angulo
            elif catetoOposto < 0:
                return 270
        elif catetoAdjacente < 0:
            if catetoOposto > 0:
                return math.atan(catetoAdjacente/catetoOposto) + 180
            elif catetoOposto == 0:
                return 0
            elif catetoOposto < 0:
                return math.atan(catetoAdjacente/catetoOposto) + 90

    def calculaDistancia(self, corpo1, corpo2):
        x1 = corpo1.posX
        x2 = corpo2.posX
        y1 = corpo1.posY
        y2 = corpo2.posY
        return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

    def finaliza(self):
        pygame.quit()

def main():
    terra = Planeta('terra', 20, 10, (0,0,255), 200, 350, 0, 0)
    marte = Planeta('marte', 20, 10, (255,0,0), 800, 350, 0, 0)
    rodando = True
    solar = Sistema([terra, marte])
    while rodando:
        solar.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

main()