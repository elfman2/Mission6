import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
import ast

file_name = None
dico = None

def file1(args):
    global file_name
    
    try:
        if len(args) != 1:
            return 'Entrez un argument correct '
        else:
            file_name = open(args[0], 'r')
            return 'Fichier défini comme fichier de travail '
    except:
        return f"File {args} not found"
        
    

def prompt():
    sys.stdout.write('>')
    sys.stdout.flush()

def dictionary(args):
    global dico
    dico = args
    
    try:
        if len(args) != 1:
            return 'Entrez un argument correct '
        else:
            file_name = open(args[0], 'r')
            return 'Fichier défini comme dictionnaire '
    except:
        return f"File {args} not found"


def CLI_interactive():
    prompt()
    for line in sys.stdin:
        if line == 'exit':
            break
    else:
        prompt()
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
    convert = [ast.literal_eval(i) for i in tableau]
    x = sum(convert)
    print(x)  
        
def avg1():
    list = []
    user_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace au lieu de 'entrer' pour additionner les nombres.
Faites 'Entrer' pour trouver la moyenne et afficher le resulat.""" ))
    tableau = user_input.split()
    convert = [ast.literal_eval(i) for i in tableau]
    x = sum(convert)
    print(x/(len(convert)))
    
def search(args):
    
    dictionary2 = {}
    with open(dico, 'r') as f:
        for line in f:
            key, value = line.split(',')
            dictionary2[key] = value
    
    if args in dictionary2:
        return f"{args} est dans le dictionnaire"
    else:
        return f"{args} n'est pas dans le dictionnaire"
        
    
    
CLI_interactive()

