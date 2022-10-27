from tkinter import N


user_input  = input("Choississez une commande. Pour voir toutes les commandes disponibles, entrez 'help'")

def help():
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

def sum(num):
    if user_input == "sum":
        run2 = True
        total = 0
        
        num2 = 0
        while run2:
            user_number = int(input("Entrez un numéro"))
            num = user_number
            user_number2 = int(input("Entrez un second numéro"))
            num2 = user_number2
            ask = input("Voulez-vous continuez? Entrez 'oui' si vous souhaitez continuer, sinon entrez 'non'")
            total = total + num + num2
            '''if ask == "oui": 
            #elif ask == "non":
                total = total + num + num2
                print(total)
                run2 = False'''



help()
sum(0)