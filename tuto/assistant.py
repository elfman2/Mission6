import sys
from optparse import OptionParser


def CLI_interactive(dummy=None):
    """
    Command line interface interactive generator

      yields: a line from stdin
    """
    for line in sys.stdin:
      yield line
      sys.stdout.write('> ')
      sys.stdout.flush()


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

def file_command(args):
    print(args)

def info_command(args):
    print(args)

def dictionary_command(args):
    print(args)

def search_command(args):
    print(args)

def sum_command(args):
    print(args)

def avg_command(args):
    print(args)

def help_command(args):
    h = '''file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
	info: montre le nombre de lignes et de caractères du fichier
	file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
	dictionary: utilise le fichier comme dictionnaire à partir de maintenant
	search <word>: détermine si le mot est dans le dictionnaire
	sum <number1> ... <numbern>: calcule la somme des nombres spécifiés
	avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés
	help: montre des instructions à l'utilisateur"
	exit: arrête l'outil'''
    print(h)

def exit_command(args):
  sys.exit(0)

Commands = {
  "command": template_command,
  "exit": exit_command,
  "file": file_command,
  "info": info_command,
  "dictionary": dictionary_command,
  "search": search_command,
  "sum":sum_command,
  "avg":avg_command,
  "help":help_command
}


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
    except SystemExit:
        raise
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


