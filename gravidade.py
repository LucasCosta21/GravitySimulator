import pygame, math
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
pygame.init()
COMPRIMENTO_TELA = 1024
ALTURA_TELA = 700

class Planeta:
    def __init__(self, raio, massa, cor, pontoX, pontoY):
        self.raio = raio
        self.massa = massa
        self.cor = cor
        self.posX = pontoX
        self.posY = pontoY

    def Mover(self, modulo, angulo):
        self.velX = modulo * math.sin(angulo)
        self.velY = modulo * math.cos(angulo)
        self.posX += self.velX
        self.posY += self.velY        

    def Desenhar(self, screen):
        print(self.posX)
        print(math.floor(self.posX))
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
            planeta.Mover(0.5, 80)
            planeta.Desenhar(self.win)

    #def calculaModulo(planeta):


    def finaliza(self):
        pygame.quit()

def main():
    terra = Planeta(20, 10, (0,0,255), 200, 350)
    marte = Planeta(20, 10, (255,0,0), 800, 350)
    rodando = True
    solar = Sistema([terra, marte])
    while rodando:
        solar.loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

main()