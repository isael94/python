#Juego de adivinar numeros
import random

intentos = 0

print('Hola!, ¿Como te llamas?')
nom = input()

numero = random.randint(1,20)
print('Bueno, ' + nom + ', estoy pensando en un numero entre 1 y 20')

while intentos < 6:
        print('intenta adivinar.')
        estimacion = input()
        estimacion = int(estimacion)

        intentos = intentos + 1

        if estimacion < numero:
            print('Es mayor mijo')

        if estimacion > numero:
                print('Es menor mijo')

        if estimacion == numero:
                    break

if estimacion == numero:
        intentos = str(intentos)
        print('Buen trabajo,' + nom + '! !Has adivinado el numero en ' + intentos     + ' intentos!')

if estimacion != numero:
            numero = str(numero)
            print('Pues no, el numero era ' + numero)
