#reino de dragones

import random
import time

def mostrarIntroduccion():
    print('Estas en una tierra llena de dragones. Frente a ti')
    print('hay dos cuevas. En una de ellas, el dragon es generoso y')
    print('amigable y compartira su tesoro contigo. El otro dragon')
    print('es codicioso y esta hambriento, y te devorara inmediatamente.')
    print()

def elegirCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print('A que cueva quieres entrar? (1 o 2)')
        cueva = input()

    return cueva

def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva...')
    time.sleep(4)
    print('Es oscura y espeluznante...')
    time.sleep(4)
    print('!Un gran dragon aparece subitamente frente a ti! Abre sus fauces y...')
    print()
    time.sleep(4)

    cuevaAmigable = random.randint(1,2)

    if cuevaElegida == str(cuevaAmigable):
       print('!Te regala su tesoro!')
    else:
        print('!Ten engulle de un bocado!')

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

             mostrarIntroduccion()

             numeroDeCueva = elegirCueva()

             explorarCueva(numeroDeCueva)

             print('¿Quieres jugar de nuevo? (si o no)')
             jugarDeNuevo = input()



    
