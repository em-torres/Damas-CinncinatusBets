class Deck:
    def __init__(self, color):
        if color == "x":
            self.deck = [[' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                         ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                         [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                         [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                         ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' ']]
        else:
            self.deck = [[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                         ['x', ' ', 'x', ' ', 'x', ' ', 'x', ' '],
                         [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' '],
                         [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                         ['o', ' ', 'o', ' ', 'o', ' ', 'o', ' ']]

    def output(self):
        letra = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
        numero = ('1', '2', '3', '4', '5', '6', '7', '8')
        print('    ' + ' '.join(letra))
        for index, i in enumerate(self.deck):
            print(f'{numero[index]}  ' + '|' + '|'.join(i) + '|' + f'  {numero[index]}')
        print('    ' + ' '.join(letra))

    def update(self, coords, movimiento, target=None):
        self.deck[movimiento[0]][movimiento[1]] = self.deck[coords[0]][coords[1]]
        self.deck[coords[0]][coords[1]] = ' '
        return self.deck
