import random
import Juego as object
encabezado = """
    ____                                _______            _                   __            
   / __ \____ _____ ___  ____ ______   / ____(_____  _____(_____  ____  ____ _/ /___  _______
  / / / / __ `/ __ `__ \/ __ `/ ___/  / /   / / __ \/ ___/ / __ \/ __ \/ __ `/ __/ / / / ___/
 / /_/ / /_/ / / / / / / /_/ (__  )  / /___/ / / / / /__/ / / / / / / / /_/ / /_/ /_/ (__  ) 
/_____/\__,_/_/ /_/ /_/\__,_/____/   \____/_/_/ /_/\___/_/_/ /_/_/ /_/\__,_/\__/\__,_/____/  by Rom's                                                                                         
"""




usuario = random.choice(['black', 'white'])
print('\nYou will play for', usuario + '!\n')

my_deck = object.juego()

while True:
    print(encabezado)

    my_deck.output()

    choose_checker = input('Chose your checker to move: ')

    my_deck.ccoordenadas(choose_checker)

    user_step = input('Enter coordinate to go: ')

    my_deck.move(choose_checker, user_step)
