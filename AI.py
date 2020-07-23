import random


class Player:
    def __init__(self, color, deck):
        self.color = color
        self.enemigo = []
        self.paso = []
        self.deck = deck

    def jugador_enemigo(self):
        for x in range(len(self.deck.deck)):
            for y in range(len(self.deck.deck[x])):
                if self.deck.deck[x][y] == self.color:
                    self.enemigo.append((x, y))
        return self.enemigo


class Usuario(Player):
    def coordenadas(self, UsuarioCoordinadas):
        letra = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        numero = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        x = letra[UsuarioCoordinadas[0]]
        y = numero[UsuarioCoordinadas[1]]
        ccordinadas = (x, y)
        return ccordinadas

    def validacion(self, damas_coordenadas):
        condicion1 = (damas_coordenadas[0] + 1, damas_coordenadas[1] + 1)
        condicion2 = (damas_coordenadas[0] - 1, damas_coordenadas[1] - 1)
        return condicion1, condicion2


class Bot(Player):
    def validacion(self, damas_coordenadas):
        condicion1 = (damas_coordenadas[0] + 1, damas_coordenadas[1] + 1)
        condicion2 = (damas_coordenadas[0] - 1, damas_coordenadas[1] - 1)
        return condicion1, condicion2

    def paso_jugador(self):
        nada = []
        botdamas = []
        botpasos = []
        for x in range(len(self.deck.deck)):
            for y in range(len(self.deck.deck[x])):
                if self.deck.deck[x][y] == ' ':
                    nada.append((x, y))
        for i in self.enemigo:
            for ef in nada:
                if ef == self.validacion(i)[0] or ef == self.validacion(i)[1]:
                    botdamas.append(i)
                    botpasos.append(ef)
        unicodamas = list(set(botdamas))
        unicopasos = list(set(botpasos))
        print('Bot decision correcta', unicodamas)
        botpasos = random.choice(unicodamas)
        print('Bot Damas pasos ', botpasos)
        # while True:
        #     botpasos = random.choice(unicodamas)
        #     print('Bot decision pasos 1', botpasos)
        #     if botpasos in self.paso_jugador():
        #         break
        # print('Confirmacion de bot', botpasos)
        return [botpasos, botdamas]
