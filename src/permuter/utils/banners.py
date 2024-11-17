from pyfiglet import Figlet
from utils.colors import Bgc

def app_banner() -> None:
    graph = Figlet(font='rounded')
    graph_render = graph.renderText('Permuter')
    print(Bgc.Purple + Bgc.Bold + graph_render + Bgc.End)


def help_banner() -> None:
    print(Bgc.Purple + "Permuter" + Bgc.End + " allows you to create a password list based")
    print("on personal data of a person, like the name, pet name,")
    print("born date, ID, etc permuting these data\n")
    print("Usage: pyhton main.py [data 1] [data 2] [data 3] [data 4]... [data n]\n")
    print("Example:")
    print("pyhton permuter.py Name petName bornDate ID             The order doesn't matter")
    print("pyhton permuter.py --help                               Show this banner \n")
    print("Remember to provide at least 4 items to generate the passwords\n")

def more_args_required_banner() -> None:
    print(Bgc.Red + Bgc.Bold + "\n\n[X]Need at least 3 items to generate the passwords" + Bgc.End)
    print(Bgc.Yellow + Bgc.Bold + "[!]Try " + Bgc.End + Bgc.Blue + \
          "python permuter.py --help" + Bgc.Yellow + Bgc.Bold + \
          " to see the help banner")
