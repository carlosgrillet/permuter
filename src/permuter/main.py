'''
Este codigo fue creado por Carlos Grillet
para el uso de la comunidad de seguridad Informatica
con el fin de ayudar a la creacion de
listas de contraseñas basadas en datos personales
'''

import os
import sys
import math
import time
try:
    import itertools
    from pyfiglet import Figlet
except ImportError as e:
    print(f"Error: {e}")
    print("Try this ... $ pip install -r /path/to/requirements.txt")
    sys.exit()

class Bgc:
    '''
    Esta clase contiene los colores para la terminal
    '''
    Blue = '\033[36m'
    Bold = '\033[1m'
    End = '\033[0m'
    Green = '\033[92m'
    Purple = '\033[95m'
    Red = '\033[91m'
    Underline = '\033[4m'
    Yellow = '\033[93m'

class Info:
    '''
    Esta clase contiene la Informacion del programa
    '''
    version = "\t\tVersion 0.3\n\n"
    author = "\t\tCarlos Grillet"

N = 0
STRLEN = 0

def main():
    '''
    Esta funcion es la principal del programa 
    '''
    global N
    global STRLEN

    graph = Figlet(font='rounded')
    graph_render = graph.renderText('Permuter')
    print(Bgc.Purple + Bgc.Bold + graph_render + Bgc.End)
    print(Bgc.Red + Bgc.Bold + Info.author + Bgc.End)
    print(Bgc.Underline + Bgc.Red + Info.version + Bgc.End)

    if len(sys.argv) == 1:
        help_banner()
        sys.exit()

    if str(sys.argv[1]) == "--help":
        help_banner()
        sys.exit()

    if len(sys.argv) < 4:
        print(Bgc.Red + Bgc.Bold + \
              "\n\n[X]Need at least 3 items to generate the passwords" + Bgc.End)
        print(Bgc.Yellow + Bgc.Bold + "[!]Try " + Bgc.End + Bgc.Blue + \
              "python permuter.py --help" + Bgc.Yellow + Bgc.Bold + \
              " to see the help banner")
        time.sleep(4)
        sys.exit()

    try:
        esp_chars = input(Bgc.Yellow + "[?]Add special chars[" + \
                          Bgc.End + " - _ . ! * " + Bgc.Yellow + "][y/n]: " + \
                          Bgc.End)
        STRLEN = input(Bgc.Yellow + '\033[1A' + '\033[36D' + \
                       "[?]Generate only passwords greater than n chars: n=" + \
                       Bgc.End)

        if esp_chars.lower() == 'y':
            N = len(sys.argv) + 5
            data = ['-', '_', '.', '!', '*']
        else :
            N = len(sys.argv) - 1
            data = []

    except KeyboardInterrupt:
        print(Bgc.Red + Bgc.Bold + "\n\n[X]User abort" + Bgc.End)
        time.sleep(1)
        sys.exit()

    point = 1
    while len(data) < N-1:
        data.append(sys.argv[point])
        point += 1

    print("\n" + Bgc.Blue + "[+]Num of items to be permuted: " + Bgc.End + str(N))
    time.sleep(2)

    print(Bgc.Yellow + "[!]Creating file of passwords" + Bgc.End)
    time.sleep(2)

    with open('passw.txt', 'w', encoding='utf-8') as file:
        print(Bgc.Yellow + "[!]File locate in: " + Bgc.Blue + \
              os.getcwd() + "/" + Bgc.End + "passw.txt")
        time.sleep(2)
        print(Bgc.Yellow + "[!]Writing..." + Bgc.End + "\n")

        for instanse in range(int(STRLEN),N+1):
            perms = itertools.permutations(data, instanse)
            for value in perms:
                file.write(str(''.join(value)) + "\n")

    time.sleep(2)
    print(Bgc.Green + Bgc.Bold + "[!]File generated successfully" + Bgc.End)
    print("\n\n")

def perms_less(data):
    '''
    Esta funcion genera las permutaciones de los datos
    '''
    count = 0
    for word_arange in range(2,N):
        perms = itertools.permutations(data, word_arange)
        for value in perms:
            if len(str(''.join(value))) < 8:
                count += 1
    return count

def num_of_perms(number):
    '''
    Esta funcion calcula el numero de permutaciones 
    '''
    num = 2
    result = 0
    while num <= 4:
        result += (math.factorial(number) / math.factorial(number - num))
        num += 1
    return result

def help_banner():
    '''
    Esta funcion muestra el banner de ayuda 
    '''
    print("This is the help Banner\n")
    print(Bgc.Purple + "Permuter" + Bgc.End + " allows you to create a password list based")
    print("on personal data about a person, like the name, the")
    print("born date, the id permuting these data to generate a")
    print("password list\n")
    print("Usage: pyhton permuter.py [data 1] [data 2] [data 3] [data 4]... [data n]\n")
    print("Example:")
    print("pyhton permuter.py Name petName bornDate ID             The order doesn't matter")
    print("pyhton permuter.py --help                               Show this banner \n")

if __name__ == "__main__" :
    main()

#Grillet
