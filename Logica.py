import random
from Deck import Deck as Tablero
import AI
import Juego

encabezado = """
    ____                                _______            _                   __            
   / __ \____ _____ ___  ____ ______   / ____(_____  _____(_____  ____  ____ _/ /___  _______
  / / / / __ `/ __ `__ \/ __ `/ ___/  / /   / / __ \/ ___/ / __ \/ __ \/ __ `/ __/ / / / ___/
 / /_/ / /_/ / / / / / / /_/ (__  )  / /___/ / / / / /__/ / / / / / / / /_/ / /_/ /_/ (__  ) 
/_____/\__,_/_/ /_/ /_/\__,_/____/   \____/_/_/ /_/\___/_/_/ /_/_/ /_/\__,_/\__/\__,_/____/  by Rom's                                                                                         
"""

usuario = random.choice(['black', 'white'])

if usuario == 'black':
    color = 'x'
    Enemigo = 'o'
else:
    color = 'o'
    Enemigo = 'x'

print('\nYou will play for', usuario + '!\n')

my_deck = Tablero(color)

while True:
    print(encabezado)
    my_deck.output()

    while True:
        usuario = AI.Usuario(color, my_deck)
        usuario.jugador_enemigo()
        try:
            usercoordsPara = usuario.coordenadas(input('Entra la coordenada de la dama:'))
            usercoordsto = usuario.coordenadas(input('Entra los movimientos coordenadas:'))
        except KeyError or IndexError:
            continue
        user_pasos_validacion_1 = usuario.paso(usercoordsPara[0])
        user_pasos_validacion_2 = usuario.paso(usercoordsPara[1])
        usuario_damas = Juego.juego(usercoordsPara, color, Tablero)
        if usuario_damas.ataqueEnemigo(usuario.jugador_enemigo()):
            usercoordsPara = usuario.coordenadas(input('Entra la coordenada de la dama:'))
            usercoordsto = usuario.coordenadas(input('Entra los movimientos coordenadas:'))
            usuario_damas.ataque(usercoordsto)
            break
        user_paso = usuario_damas.paso(usercoordsto, user_step_validation_1, user_step_validation_2)
        if user_paso:
            Tablero.update(usercoordsPara, usercoordsto)
        else:
            print('Usuario input-Incorrecto!!')
    bot = AI.bot(color, Tablero)
    bot.jugador_enemigo()
    bot_pasos = list(bot.paso())
    bot_damas_choice = bot_pasos[0]
    bot_movimiento = bot_pasos[1]
    bot_damas = Juego.juego(color, bot_damas_choice, Tablero)
    Tablero.update(bot_damas_choice, bot_movimiento)
