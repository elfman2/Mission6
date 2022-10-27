from tkinter import N


user_input  = input("Choississez une commande. Pour voir toutes les commandes disponibles, entrez 'help'")

if user_input == 'help':
    print("file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment")
    print("info: montre le nombre de lignes et de caractères du fichier")
    print("file <name>: spécifie le nom d'un fichier sur lequel l'outil doit travailler à partir de ce moment")
    print("dictionary: utilise le fichier comme dictionnaire à partir de maintenant")
    print("search <word>: détermine si le mot est dans le dictionnaire")
    print("sum <number1> ... <numbern>: calcule la somme des nombres spécifiés")
    print("avg <number1> ... <numbern>: calcule la moyenne des nombres spécifiés")
    print("help: montre des instructions à l'utilisateur")
    print("exit: arrête l'outil")