try:
    import os
    import sys
    import math
    import time
    import itertools
    from pyfiglet import Figlet

except ImportError as e:
    print("Error: %s \n" % (e))
    print("Try this ... pip install -r /path/to/requirements.txt")
    sys.exit()

class bgc:
    Blue = '\033[36m'
    Purple = '\033[95m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    End = '\033[0m'
    Underline = '\033[4m'
    Bold = '\033[1m'

class info:
    version = "\t\tVersion 0.2\n\n"
    author = "\t\tCarlos Grillet"

n = 0
strLen = 0


def main():
    Graph = Figlet(font='rounded')
    GraphRender = Graph.renderText('Permuter')
    print(bgc.Purple + bgc.Bold + GraphRender + bgc.End)
    print(bgc.Red + bgc.Bold + info.author + bgc.End)
    print(bgc.Underline + bgc.Red + info.version + bgc.End)
	
    if len(sys.argv) == 1:
        helpBanner()
        sys.exit()

    if str(sys.argv[1]) == "--help":
        helpBanner()
        sys.exit()

    if len(sys.argv) < 4:
        print(bgc.Red + bgc.Bold + "\n\n[X]Need at least 3 items to generate the passwords" + bgc.End)
        print(bgc.Yellow + bgc.Bold + "[!]Try " + bgc.End + bgc.Blue + "python permuter.py --help" + bgc.Yellow + bgc.Bold + " to see the help banner")
        time.sleep(4)
        sys.exit()

    try:
        espChars = input(bgc.Yellow + "[?]Add special chars[" + bgc.End + " - _ . ! * " + bgc.Yellow + "][y/n]:" + bgc.End)
        strLen = input(bgc.Yellow + '\033[1A' + '\033[36D' +"[?]Generate only passwords greater than n chars n=" + bgc.End)
		
        if espChars.lower() == 'y':
            n = len(sys.argv) + 5
            data = ['-', '_', '.', '!', '*']
        else :
            n = len(sys.argv) - 1
            data = []

    except KeyboardInterrupt as e:
        print(bgc.Red + bgc.Bold + "\n\n[X]User abort" + bgc.End)
        time.sleep(1)
        sys.exit()

    point = 1
    while len(data) < n:
        data.append(sys.argv[point])
        point += 1

    #if gtr8chr == 'y':
    #    r = numOfPerms(n) - permsLess(data)
    #else:
    #    r = numOfPerms(n)
	
    print("\n" + bgc.Blue + "[+]Num of items to be permuted: " + bgc.End + str(n))
    #print(bgc.Blue + "[+]Num of possible permutations: " + bgc.End + str(r) + "\n")
    time.sleep(2)

    print(bgc.Yellow + "[!]Creating file of passwords" + bgc.End)
    time.sleep(2)

    f = open('passw.txt', 'w')
    print(bgc.Yellow + "[!]File locate in: " + bgc.Blue + os.getcwd() + "/" + bgc.End + "passw.txt")
    time.sleep(2)
    print(bgc.Yellow + "[!]Writing..." + bgc.End + "\n")

    for instanse in range(int(strLen),n+1):
        perms = itertools.permutations(data, instanse)
        for x in perms:
            f.write(str(''.join(x)) + "\n")

    f.close()
    time.sleep(2)
    print(bgc.Green + bgc.Bold + "[!]File generated successfully" + bgc.End)
    print("\n\n")

def permsLess(data):
    count = 0
    for r in range(2,n):
        perms = itertools.permutations(data, r)
        for x in perms:
            if len(str(''.join(x))) < 8:
                count += 1
    return count
		
def numOfPerms(n):
    num = 2
    result = 0
    while num <= 4:
        result += (math.factorial(n) / math.factorial(n - num))
        num += 1
    return (result)

def helpBanner():
    print("This is the help Banner\n")
    print(bgc.Purple + "Permuter" + bgc.End + " allows you to create a password list based")
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
