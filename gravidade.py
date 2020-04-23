from graphics import *

class Planeta:
    def __init__(self, raio, massa, cor, pontoX, pontoY):
        self.raio = raio
        self.massa = massa
        self.cor = cor
        self.corpo = Circle(Point(pontoX, pontoY), raio)
        self.corpo.setFill(cor)

class Sistema:
    def __init__(self): # Inicializa os dados do sistema (constantes, tamanho da tela, etc)
        self.win = GraphWin("Minha janela", 1000, 600)
        self.terra = Planeta(30, 1, 'blue', 200, 200)
        self.marte = Planeta(10, 1, 'red', 400, 350)

    def loop(self):
        self.terra.corpo.draw(self.win)
        self.marte.corpo.draw(self.win)
        self.win.getMouse()
        self.win.close()

def main():
    solar = Sistema()
    solar.loop()

main()