import sys
from optparse import OptionParser


def CLI_interactive(dummy):
    """
    Command line interface interactive generator

      yields: a line from stdin
    """
    for line in sys.stdin:
        if line != "exit":
            yield line


def CLI_batch(file):
    """
   Command line interface batch generator
     'exit' command ignored in batch mode. Existing at
     end of batch file.

      Args: file input batch command file

      yields: a file line

    """
    with open(file, 'r') as f:
        for line in f:
            yield line


def template_command(args):
    print(args)


Commands = {"command": template_command}


def parse_command(line):
    '''
       parse a command line.
       lookup command in Commands dictionary, and call the corresponding function.
        if not found error message displayed
       Args: line
    '''
    try:
        cmd = line.split()
        Commands[cmd[0]](cmd[1:])
    except:
        print("unrecognized command "+cmd[0])


if __name__ == '__main__':
    """
     Parse arguments and activate interactive or batch mode
    """
    # https://docs.python.org/3/library/optparse.html
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="batch file of commands")
    (options, args) = parser.parse_args()

    CLI = CLI_batch if options.filename is not None else CLI_interactive
    for l in CLI(options.filename):
        parse_command(l)

user_input  = input("Choississez une commande. Pour voir toutes les commandes disponibles, entrez 'help'")

def help():
    if user_input == 'help':
        print("""("file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment")
        ("info: montre le nombre de lignes et de caractères du fichier")
        ("file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment")
        ("dictionary: utilise le fichier comme dictionnaire à partir de maintenant")
        ("search <word>: détermine si le mot est dans le dictionnaire")
        ("sum <number1> ... <numbern>: calcule la somme des nombres spécifiés")
        ("avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés")
        ("help: montre des instructions à l'utilisateur")
        ("exit: arrête l'outil")""")
        
    

def sum():
    if user_input == "sum":
        run2 = True
        total = 0
        num2 = 0
        while run2:
            user_number = int(input("Entrez un numéro "))
            user_number2 = int(input("Entrez un numéro "))
            total = total + user_number + user_number2
            ask = input("Voulez-vous continuez? Entrez 'oui' si vous souhaitez continuer, sinon entrez 'non'")
            yes = True
            if ask == "oui":
                while yes:
                    user_number3 = int(input("Entrez un numéro "))
                    total += user_number3
                    ask2 = input("Si vous voulez continuer, entrez oui. Sinon entrez non")
                    if ask2 == 'yes':
                        continue
                    elif ask2 == 'non':
                        print(total)
                        yes = False
                        run2 = False
                break
                
            elif ask == "non":
                print(total)
                run2 = False


help()
sum()