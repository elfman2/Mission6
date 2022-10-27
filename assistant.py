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
