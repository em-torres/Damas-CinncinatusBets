class juego():
    def _init_(self,color):
        if color == 'Negro':
            self.usuario='J1'
            self.bots='J2'
            self.tablero=[['-', 'J1', '-', 'J1', '-', 'J1', '-', ''],
               ['J1', '-', 'J1', '-', 'J1', '-', 'n', '-'],
               ['-', 'J1', '-', 'J1', '-', 'J1', '-', 'J1'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['J2', '-', 'J2', '-', 'J2', '-', 'J2', '-'],
               ['-', 'J2', '-', 'J2', '-', 'J2', '-', 'J2'],
               ['J2', '-', 'J2', '-', 'J2', '-', 'J2', '-']]
        else:
            self.usuario='J2'
            self.bots='J1'
            self.tablero=[['-', 'J2', '-', 'J2', '-', 'J1', '-', ''],
               ['J2', '-', 'J2', '-', 'J2', '-', 'J2', '-'],
               ['-', 'J2', '-', 'J2', '-', 'J2', '-', 'J2'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['-', '-', '-', '-', '-', '-', '-', '-'],
               ['J1', '-', 'J1', '-', 'J1', '-', 'J1', '-'],
               ['-', 'J1', '-', 'J1', '-', 'J1', '-', 'J1'],
               ['J1', '-', 'J1', '-', 'J1', '-', 'J1', '-']]
    def output(self):
        letra =('A','B','C','D','E','F','G','H')
        numero =('1','2','3','4','5','6','7','8')
        for index, i in enumerate(self.tablero):
            print(f'{numero[index]}'+'|'+'|'+'|'.join(i)+'|'+f'{numero[index]}')
        print('   '+ ' '.join(letra))
    def ccoordenadas(self,coordenadas):
        Dletra={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
        Dnumero={'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
        x=Dletra[coordenadas[0]]
        y=Dnumero[coordenadas[1]]
        ccoordenadas=(x,y)
        print(' coordernada de l',ccoordenadas)
        return ccoordenadas
    def movimiento(self,v1,v2):
        chequeocoordenadas= self.ccoordenadas(v1)
        movi_dest=self.ccoordenadas(v2)
        vacio=self.vacio(movi_dest)
        smovimiento=self.smovimiento(chequeocoordenadas,movi_dest)
    def chequeopieza(self,coorde):
        piezacoordenada=self.juego[coord[0]][coord[1]]
        if self.usuario ==  piezacoordenada :
            resultado = True
        elif piezacoordenada == ' ':
             print('No hay ninguna pieza')
             resultado = False
        else:
             print('No es tu pieza mueve otra')
             resultado=False
        return resultado
    def reglas(self,v1,v2):
        if self.juego[v1[0]][v1[1]] == self.bots:
            if v2[0] == v1[0]+1 and (v2[1]==v2[1]+1 or v2[1]==v1[1]-1):
               return True
        elif self.juego[v1[0]][v1[1]]==self.bots:
            if v2[0] == v1[0]+1 and (v2[1]==v2[1]+1 or v2[1]==v1[1]-1):
               return True
            else:
                 print('No es posible')
                 return False
    def Chequeo(self):
         juegador=[]
         botsJ2=[]
         VacioJ2=[]
         for x in range(len(self.tablero)):
            for y in range(self.tablero[x]):
               if self.tablero[x][y]== self.bots:
                   juegador.append((x,y))
               if self.tablero[x][y]== self.bots:
                        botsJ2.append((x,y))
               if self.tablero[x][y]== '  ':
                        vacioJ2.append((x,y))
            return juegador,botsJ2,VacioJ2
