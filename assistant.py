import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
import ast
import os

file_handle = None
dico = None
def file_command(args):
    global file_handle
    try:
        if len(args) != 1:
            return 'Erreur 1: Il faut entrer un seul argument '
        elif len(args) == 1:
            file_handle = open(args[0], 'r')
            return f"Fichier {args} défini comme fichier de travail "
    except:
        return f"Erreur 2: Impossible de trouver le fichier {args} "

def commands_function():
        while True:
            line = input('> ')
            key = line.split()
            try:
              command = all_commands[key[0]]
              print(command(key[1:]))
            except SystemExit:
              raise
            except:
              print (f"Erreur 3: Veuillez entrer une commande valide. Pour voir toutes les commandes, entrez 'help' ")

def dictionary_command(args):
    global dico
    global file_handle
    dico = {}
    try:
        if len(args)!=0:
            return "Pas d'argment pour dictionary "
        else:
            for line in file_handle:
                key, value = line.split(',')
                dico[key] = value
            return 'Fichier définit comme dictionnaire '
    except NameError:
        return f"Error:Veuillez d'abord ouvrir un fichier. Vous pouvez le faire avec la commande file 'file_name'"
    except TypeError:
        return f"Veuillez appeler la commande file avant : Impossible de trouver le fichier"

def search_command(args):
    global dico
    if args[0] in dico:
        return f"{args} se trouve dans le dictionnaire"
    else:
        return f"{args} ne se trouve pas dans le dictionnaire"

def help_command(args):
    
    """
    Prints all the commands in the CLI to the user
    """
    text = '''usage: python assistant.py
    list_of_command:
file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
info: montre le nombre de lignes et de caractères du fichier
dictionary: utilise le fichier comme dictionnaire à partir de maintenant
search : détermine si le mot est dans le dictionnaire
sum : calcule la somme des nombres spécifiés
avg : calcule la moyenne des nombres spécifiés
help: montre des instructions à l'utilisateur
exit: arrête l'outil'''
    print(text)
    return text

def number_input(tableau):
    try:
        convert = [ast.literal_eval(i) for i in tableau]
        return convert
    except ValueError:
        return None

def sum_command(args):
    '''

    return strings which represent int or float values
    int when one input is int and float when one input is float
    int when all the input are int and float when one input is float
    '''
    num_list = number_input(args)
    if num_list == None:
        return 'Veuillez entrer des numéro'
    else:
        sum_result = sum(num_list)
        return str(sum_result)

def avg_command(args):
    '''
    calculate the average between numbers
    
    return string which represent float values

    '''
    num_list = number_input(args)
    if num_list == None:
        return 'Veuillez entrer des numéro'
    else:
        avg = sum(num_list)/len(num_list)
        return str(avg)

def info_command(args):
    f = file_handle
    num_lines = len(f.readlines())
    f.seek(0, os.SEEK_END)
    num_caracters = f.tell()
    return f"Il y a {num_lines} lignes et {num_caracters} caractères."

def exit_command(args):
    global file_handle
    if file_handle is not None:
        file_handle.close()
    print ("A la prochaine! ")
    sys.exit(0);

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
if __name__ == '__main__':
   commands_function()
