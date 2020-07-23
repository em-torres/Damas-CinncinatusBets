class juego:
    def __init__(self, coordenadas, color, deck):
        self.coordenadas = coordenadas
        self.color = color
        self.deck = deck

    def paso(self, movimiento, condicion_valida1, condicion_valida2):
        destino_correcto = (movimiento == condicion_valida1 or movimiento == condicion_valida2)
        if self.deck[self.coordenadas[0]][self.coordenadas[1]] == self.color:
            if destino_correcto:
                result = True
            else:
                result = False
            return result
        else:
            print('campo vacio')
            result = False
            return result

    def Listanada(self):
        nada = []
        for x in range(len(self.deck.deck)):
            for y in range(len(self.deck.deck[x])):
                if self.deck[x][y] == ' ':
                    nada.append((x, y))
        return nada

    def EstaVacio(self, movimiento):
        if movimiento in self.Listanada():
            EstaVacio = True
        else:
            print('Campo esta vacio')
            EstaVacio = False
        return EstaVacio

    def NecesitaAtaque(self, DamasEnemigo):
        EnemyArmy = []
        for x in range(len(self.deck)):
            for y in range(len(self.tablero[x])):
                if self.deck[x][y] != '  ' and self.deck[x][y] != self.color:
                    EnemyArmy.append((x, y))
        print('Enemigo', EnemyArmy)
        PrimerChequeo = []
        SegundoChequeo = []
        for i in DamasEnemigo:
            for j in EnemyArmy:
                if j == (i[0] + 1, i[1] + 1) or j == (i[0] - 1, i[1] - 1) or j == (i[0] + 1, i[1] - 1) or j == (
                i[0] - 1, i[1] + 1):
                    PrimerChequeo.append(j)
        for i in PrimerChequeo:
            for A in self.Listanada():
                if A == (j[0] + 1, j[1] + 1) or A == (j[0] - 1, j[1] - 1) or A == (j[0] + 1, j[1] - 1) or A == (
                j[0] - 1, j[1] + 1):
                    SegundoChequeo.append(A)
        if not SegundoChequeo:
            result = False
        elif SegundoChequeo:
            print('Necesita Ataque')
            result = True
        else:
            result = False
        return result

    def ataqueEnemigo(self):
        Objetivo_1 = self.coordenadas[0] - 1, self.coordenadas[1] - 1
        Objetivo_2 = self.coordenadas[0] - 1, self.coordenadas[1] + 1
        Objetivo_3 = self.coordenadas[0] + 1, self.coordenadas[1] - 1
        Objetivo_4 = self.coordenadas[0] + 1, self.coordenadas[1] + 1

        PasosObjetivo_1 = self.coordenadas[0] - 2, self.coordenadas[1] - 2
        PasosObjetivo_2 = self.coordenadas[0] - 2, self.coordenadas[1] + 2
        PasosObjetivo_3 = self.coordenadas[0] + 2, self.coordenadas[1] - 2
        PasosObjetivo_4 = self.coordenadas[0] + 2, self.coordenadas[1] + 2
        dict_attack = {PasosObjetivo_1: Objetivo_1, PasosObjetivo_2: Objetivo_2, PasosObjetivo_3: Objetivo_3,
                       PasosObjetivo_4: Objetivo_4}
        return dict_attack

    def ataque(self, movimiento):
        dict_attack = self.ataqueEnemigo()
        if movimiento in dict_attack and self.EstaVacio(movimiento):
            Objectivo = dict_attack[movimiento]
            if self.deck[Objectivo[0]][Objectivo[1]] != self.color and self.deck[Objectivo[0]][Objectivo[1]] != ' ':
                self.deck[movimiento[0][movimiento[1]]] = self.tablero[self.coordenadas[0]][self.coordenadas[1]]
                self.deck[self.coordenadas[0]][self.coordenadas[1]]
                self.deck[movimiento[0]][self.coordenadas[1]] = ' '
                self.deck[Objectivo[0]][Objectivo[1]]
                return self.deck
            else:
                print('Pasos incorrecto haga otro paso')
