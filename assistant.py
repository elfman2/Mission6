import sys # systeme, permet acceder a l'entree du clavier et a la sortie sur ecran
from optparse import OptionParser # 


def CLI_interactive(dummy): #tout ce que on met sur le clavier va dans stdin
    """
    Command line interface interactive generator
      yields: a line from stdin
    """
    for line in sys.stdin:
        if line != "exit":
            yield line
        else:
            return


def CLI_batch(file):
    """
   Command line interface batch generator
     'exit' command ignored in batch mode. Existing at
     end of batch file.
      Args: file input batch command file
      yields: a file line
    """
    with open(file, 'r') as f: #va mettre dans f une reference vers le fichier file
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
    """
    Prints all the commands in the CLI to the user
    """
    if user_input == 'help':
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
        
def sum1(): # merci pour l'aide
    list = []
    user_input = (input("""
Entrez des numéros.
Note: Après chaque numéro, faites espace au lieu de 'entrer' pour additionner les nombres.
Faites 'Entrer' pour afficher le resulat.""" ))
    tableau = user_input.split()
    convert = [float(i) for i in tableau]
    x = sum(convert)
    print(x)
        
        
    
def avg():
    """
    Calculate the average of n numbers
    """
    if user_input == 'avg':
        run = True
        total = 0
        counter = 0
        while run:
            number = float(input("Entrez un nombre "))
            number2 = float(input("Entrez un nombre "))
            counter += 2
            total = total + number + number2
            ask = input("Souhaitez-vous continuer? Entrez 'oui' ou 'non'")
            if ask == 'oui':
                yes = True
                while yes:
                    number3 = float(input("Entrez un nombre "))
                    counter += 1
                    total = (total + number3)
                    ask2 = input("Souhaitez-vous continuer? Entrez 'oui' ou 'non'")
                    if ask2 == 'yes':
                        continue
                    elif ask2 == 'non':
                        print(total/counter)
                        yes = False
                        run = False
            elif ask == 'non':
                print(total/counter)
                run = False
    

help()
sum1()
avg()





