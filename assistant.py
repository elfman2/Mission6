import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
from optparse import OptionParser # 


def prompt():
    sys.stdout.write('>')
    sys.stdout.flush()

def dictionary(filename):
    dictionary2 = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.split(',')
            dictionary2[key] = value
        return dictionary2

def CLI_interactive():
    for line in sys.stdin:
        yield line
def help():
    
    """
    Prints all the commands in the CLI to the user
    """
    print("""
        file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
        info: montre le nombre de lignes et de caractères du fichier
        file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
        dictionary: utilise le fichier comme dictionnaire à partir de maintenant
        search <word>: détermine si le mot est dans le dictionnaire
        sum <number1> ... <numbern>: calcule la somme des nombres spécifiés
        avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés
        help: montre des instructions à l'utilisateur
        exit: arrête l'outil""")
        
def sum1():
    list = []
    user_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace au lieu de 'entrer' pour additionner les nombres.
Faites 'Entrer' pour afficher le resulat.""" ))
    tableau = user_input.split()
    convert = [float(i) for i in tableau]
    x = sum(convert)
    print(x)  
        
def avg1():
    list = []
    user_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace au lieu de 'entrer' pour additionner les nombres.
Faites 'Entrer' pour trouver la moyenne et afficher le resulat.""" ))
    tableau = user_input.split()
    convert = [float(i) for i in tableau]
    x = sum(convert)
    print(x/(len(convert)))
    
CLI_interactive()

