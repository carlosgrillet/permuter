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

class bgColor:
    Blue = '\033[36m'
    Purple = '\033[95m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Red = '\033[91m'
    End = '\033[0m'
    Underline = '\033[4m'
    Bold = '\033[1m'

class info:
    version = "\t\tVersion 0.1\n\n"
    author = "\t\tCarlos Grillet"


def main():
	Graph = Figlet(font='rounded')
	GraphRender = Graph.renderText('Permuter')
	print(bgColor.Purple + bgColor.Bold + GraphRender + bgColor.End)
	print(bgColor.Red + bgColor.Bold + info.author + bgColor.End)
	print(bgColor.Underline + bgColor.Red + info.version + bgColor.End)
	
	if len(sys.argv) == 1:
		helpBanner()
		sys.exit()

	if str(sys.argv[1]) == "--help":
		helpBanner()
		sys.exit()

	if len(sys.argv) < 4:
		print(bgColor.Red + bgColor.Bold + "\n\n[X]Need at least 3 items to generate the passwords" + bgColor.End)
		print(bgColor.Yellow + bgColor.Bold + "[!]Try " + bgColor.End + bgColor.Blue + "python permuter.py --help" + bgColor.Yellow + bgColor.Bold + " to see the help banner")
		time.sleep(4)
		sys.exit()

	gtr8chr = ''

	try:
		espChars = input(bgColor.Yellow + "[?]Add special chars[" + bgColor.End + " - _ . ! * " + bgColor.Yellow + "][y/n]:" + bgColor.End)
		gtr8chr = input(bgColor.Yellow + '\033[1A' + '\033[36D' +"[?]Generate only passwords greater than 8 chars?[y/n]:" + bgColor.End)
		
		if espChars.lower() == 'y':
			n = len(sys.argv) + 4
			data = ['-', '_', '.', '!', '*']
		else :
			n = len(sys.argv) - 1
			data = []

	except KeyboardInterrupt as e:
		print(bgColor.Red + bgColor.Bold + "\n\n[X]User abort" + bgColor.End)
		time.sleep(1)
		sys.exit()

	point = 1
	while len(data) < n:
		data.append(sys.argv[point])
		point += 1

	if gtr8chr == 'y':
		r = numOfPerms(n) - permsLess(data)
	else:
		r = numOfPerms(n)
	
	print("\n" + bgColor.Blue + "[+]Num of items to be permuted: " + bgColor.End + str(n))
	print(bgColor.Blue + "[+]Num of possible permutations: " + bgColor.End + str(r) + "\n")
	time.sleep(2)

	print(bgColor.Yellow + "[!]Creating file of passwords" + bgColor.End)
	time.sleep(2)

	f = open('passw.txt', 'w')
	print(bgColor.Yellow + "[!]File locate in: " + bgColor.Blue + os.getcwd() + "/" + bgColor.End + "passw.txt")
	time.sleep(2)
	print(bgColor.Yellow + "[!]Writing..." + bgColor.End + "\n")

	for r in range(2,4):
            perms = itertools.permutations(data, r)
            for x in perms:
                if gtr8chr.lower() == 'n':
                    f.write(str(''.join(x)) + "\n")
                else:
                    if len(str(''.join(x))) >= 8:
                        f.write(str(''.join(x)) + "\n")

	f.close()
	time.sleep(6)
	print(bgColor.Green + bgColor.Bold + "[!]File generated successfully" + bgColor.End)
	print("\n\n")

def permsLess(data):
    count = 0
    for r in range(2,4):
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
    print(bgColor.Purple + "Permuter" + bgColor.End + " allows you to create a password list based")
    print("on personal data about a person, like the name, the")
    print("born date, the id permuting these data to generate a")
    print("password list\n")
    print("Usage: pyhton permuter.py [data 1] [data 2] [data 3] [data 4]... [data n]\n")
    print("Example:")
    print("pyhton permuter.py Carlos Grillet C G 07 1996 Ren       The order doesn't matter")
    print("pyhton permuter.py --help                               Show this banner \n")

if __name__ == "__main__" :
    main()

#Grillet
