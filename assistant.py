import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
import ast

file_handle = None
dico = None
def file_command(args):
    global file_handle
    global file1
    try:
        if len(args) != 1:
            return "Il ne faut entrer qu'un seul argument "
        elif len(args) == 1:
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
        prompt()
        if line == 'exit':
            break
        else:
            yield line

def commands_function():
    for line2 in CLI_interactive():
        key = line2.split()
        command = all_commands[key[0]]
        print(command(key[1:]))



def dictionary_command(args):
    global dico
    global file_handle
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
        
def help_command(args):
    
    """
    Prints all the commands in the CLI to the user
    """
    text = '''
file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
info: montre le nombre de lignes et de caractères du fichier
dictionary: utilise le fichier comme dictionnaire à partir de maintenant
search <word>: détermine si le mot est dans le dictionnaire
sum <number1> ... <numbern>: calcule la somme des nombres spécifiés
avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés
help: montre des instructions à l'utilisateur
exit: arrête l'outil'''
    return text

def number_input(args):
    try:
        num_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace pour calculer les nombres.
Faites 'Entrer' pour afficher le resulat.""" ))
        tableau = num_input.split()
        convert = [ast.literal_eval(i) for i in tableau]
        return convert
    except ValueError:
        return None

def sum_command(args):
    global error
    num_list = number_input(args)
    if num_list == None:
        return 'Veuillez entrer des numéro'
    else:
        sum_result = sum(num_list)
        return sum_result
        

        
def avg_command(args):
    num_list = number_input(args)
    if num_list == None:
        return 'Veuillez entrer des numéro'
    else:
        avg = sum(num_list)/len(num_list)
        return avg

def info_command(args):
    f = file_handle
    num_lines = len(f.readlines())
    f.seek(0)
    num_words  = f.read()
    num_words2 = len(num_words)
    return f"Il y a {num_lines} lignes et {num_words2} mots."
    

def exit_command(args):
    file_handle.close()
    return "A la prochaine! "
    
    
all_commands ={
"help": help_command,
"sum": sum_command,
"average": avg_command,
"search": search_command,
"dictionary": dictionary_command,
"file": file_command,
"exit": exit_command,
"info": info_command


}
    
commands_function()