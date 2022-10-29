import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
import ast

error = False
file_handle = None
dico = None

def file1(args):
    global file_handle
    try:
        if len(args) != 1:
            return "Il ne faut entrer qu'un seul argument "
        else:
            file_handle = open(args[0], 'r')
            return f"Fichier {args} défini comme fichier de travail "
    except:
        return f"Impossible de trouver le fichier {args} "

def prompt():
    sys.stdout.write('>')
    sys.stdout.flush()

def CLI_interactive():
    prompt()
    for line in sys.stdin:
        if line == 'exit':
            break
    else:
        prompt()
        yield line

def dictionary(args):
    global dico
    global file_handle
    global error
    dictionary2 = {}
    dico = dictionary2
    try:
        if len(args) != 1:
            return "N'entrez qu'un seul argument "
        else:
            f = file_handle        
            for line in f:
                key, value = line.split(',')
                dictionary2[key] = value
            return 'Fichier définit comme dictionnaire '
    except:
        return f"Impossible de trouver le fichier {args}"
        error = True

def search(args):
    if args in dico:
        return f"{args} se trouve dans le dictionnaire"
    else:
        return f"{args} ne se trouve pas dans le dictionnaire"
        
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

def calcul():
    global error
    list = []
    try:
        user_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace pour calculer les nombres.
Faites 'Entrer' pour afficher le resulat.""" ))
        tableau = user_input.split()
        convert = [ast.literal_eval(i) for i in tableau]
        return sum(convert), len(convert)
    except ValueError:
        print('Veuillez entrer des numéro')
        error = True

def sum1():
    global error
    sum_result = calcul()
    if error == False:
        return sum_result[0]
    else:
        error = False
        
def avg1():
    global error
    sum_result = calcul()
    if error == False:   
        return sum_result[0]/sum_result[1]
    else:
        error = False
    
    

        
    
    
CLI_interactive()


