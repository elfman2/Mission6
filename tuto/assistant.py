import sys
import ast
from optparse import OptionParser

def prompt():
    sys.stdout.write('> ')
    sys.stdout.flush()

def CLI_interactive(dummy=None):
    """
    Command line interface interactive generator

      yields: a line from stdin
    """
    prompt()
    for line in sys.stdin:
      yield line
      prompt()


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

''' file descriptor '''
file = None


def file_command(args):
    """
    Try  to open the file in args
      Args args[0] file name
      post  file global var set with file descriptor
         error cases: file name unspecified, file not found
    """
    global file
    try:
      if len(args)!=1:
        print ('please specify file name')
        help()
      else:
        file = open(args[0],'r')
        print('opened '+args[0])
    except:
      print ("Cannot open file " + args[0])
      help()

def help():
    help_command(None)

def is_file_opened():
    global file
    if file is None:
      print("Please call file command to select a file")
      help()
      return False
    return True

def info_command(args):
    global file
    if is_file_opened():
      lines = file.readlines()
      print('Number of lines: '+str(len(lines)))

dico = dict()

def dictionary_command(args):
    global file
    global dico
    if is_file_opened():
      for l in file:
        dico[l.split(',')[0]]=''

def search_command(args):
    global dico
    print ('{name} {presence} in dictionary'.format(name=args[0],presence='is present' if args[0] in dico else 'is absent'))

def sum_list(args):
    return sum([ ast.literal_eval(num) for num in args ])

def sum_command(args):
    print('The sum {expression} = {result}'.format(expression='+'.join(args),result=str(sum_list(args))))

def avg_command(args):
    print('The average of {expression} = {result}'.format(expression='+'.join(args),result=str(sum_list(args)/len(args))))

def help_command(args):
    h = '''
  This is the assistant MI-6 your majesty
	file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment
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
  if file is not None:
    file.close()
  print ('bye!')
  sys.exit(0)

Commands = {
  "exit": exit_command,
  "bye": exit_command, #alias for exit
  "quit": exit_command, # alias for exit
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
        print("unrecognized command "+cmd[0] if len(cmd)!=0 else '')


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


