import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
import ast

error = False
file_handle = None
dico = None
file1  = False
def file_command(args):
    global file_handle
    global file1
    try:
        if len(args) != 1:
            return "Il ne faut entrer qu'un seul argument "
        elif len(args) != 1 and file1 == False:
            file_handle = open(args[0], 'r')
            file1 = True
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

def dictionary_command(args):
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

def search_command(args):
    if args in dico:
        return f"{args} se trouve dans le dictionnaire"
    else:
        return f"{args} ne se trouve pas dans le dictionnaire"
        
def help_command():
    
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

def sum_command():
    global error
    sum_result = calcul()
    if error == False:
        return sum_result[0]
    else:
        error = False
        
def avg_command():
    global error
    sum_result = calcul()
    if error == False:   
        return sum_result[0]/sum_result[1]
    else:
        error = False

def info_command(args):
    f = file_handle
    num_lines = len(f.readlines())
    f.seek(0)
    num_words  = f.read()
    num_words2 = len(num_words)
    return f"Il y a {num_lines} lignes et {num_words2} mots."
    

def exit_command():
    global file1
    if file1 == True:
        file_handle.close()
        fiel1 = False
        return "A la prochaine! "
    else:
        return "Aucun fichier n'est ouvert actuellement "
    
'''all_commands ={
"help_command":
"sum_command":
"avg_command":
"search_command":
"dictionary_command":
"file_command":
"exit_command":
"info_command":


}'''
    
CLI_interactive()
