from Deck import Deck as Decker
from Juego import juego as Game

import AI
import random


def game_init():
    color      = select_user()
    my_deck    = Decker(color)

    while True:
        print_game_header()         # Prints the game Header
        my_deck.output()            # Prints the actual Deck
        while True:
            usuario = AI.Usuario(color, my_deck)
            usuario.jugador_enemigo()
            try:
                usercoordsPara = usuario.coordenadas(input('Entra la coordenada de la dama:'))
                usercoordsto = usuario.coordenadas(input('Entra los movimientos coordenadas:'))
            except KeyError or IndexError:
                continue

            user_pasos_validacion_1 = usuario.paso.append(usercoordsPara[0])
            user_pasos_validacion_2 = usuario.paso.append(usercoordsPara[1])

            # user_pasos_validacion_1 = usuario.paso(usercoordsPara[0])
            # user_pasos_validacion_2 = usuario.paso(usercoordsPara[1])
            usuario_damas = Game(usercoordsPara, color, Decker)

            if usuario_damas.ataqueEnemigo():
                usercoordsPara = usuario.coordenadas(input('Entra la coordenada de la dama:'))
                usercoordsto = usuario.coordenadas(input('Entra los movimientos coordenadas:'))
                usuario_damas.ataque(usercoordsto)
                break
            user_paso = usuario_damas.paso(usercoordsto, user_step_validation_1, user_step_validation_2)
            if user_paso:
                Decker.update(usercoordsPara, usercoordsto)
            else:
                print('Usuario input-Incorrecto!!')

        bot = AI.Bot(color, my_deck)
        bot.jugador_enemigo()
        bot_pasos = bot.paso_jugador()
        bot_damas_choice = bot_pasos[0]
        bot_movimiento = bot_pasos[1]

        bot_damas = Game(color, bot_damas_choice, Decker)
        my_deck.update(bot_damas_choice, bot_movimiento)


def print_game_header():
    encabezado = """
            ____                                _______            _                   __            
           / __ \____ _____ ___  ____ ______   / ____(_____  _____(_____  ____  ____ _/ /___  _______
          / / / / __ `/ __ `__ \/ __ `/ ___/  / /   / / __ \/ ___/ / __ \/ __ \/ __ `/ __/ / / / ___/
         / /_/ / /_/ / / / / / / /_/ (__  )  / /___/ / / / / /__/ / / / / / / / /_/ / /_/ /_/ (__  ) 
        /_____/\__,_/_/ /_/ /_/\__,_/____/   \____/_/_/ /_/\___/_/_/ /_/_/ /_/\__,_/\__/\__,_/____/  by Rom's                                                                                         
        """
    print(encabezado)
    return


def select_user():
    usuario = random.choice(['black', 'white'])

    if usuario == 'black':
        color = 'x'
    else:
        color = 'o'

    print('\nYou will play for', usuario + '!\n')
    return color


if __name__ == "__main__":
    game_init()
