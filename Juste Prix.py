import random
import time
from termcolor import colored

# Inisialisé la valeur

essais = 0

# Fonction pour afficher le message de bienvenue

def bienvenue():
    print(colored("============================", "dark_grey"))
    time.sleep(2)  # Pause de 2 secondes
    print(colored("Bienvenue dans le Juste Prix", "white"))
    time.sleep(2)  # Pause de 2 secondes
    print(colored("Devinez un nombre !", "white"))
    time.sleep(2)  # Pause de 2 secondes
    print(colored("============================", "dark_grey"))

# Fonction pour choisir la difficulté et générer le nombre

def choisir_difficulte():
    print("Choisissez une difficulté :")
    print("1. Facile (nombre entre 1 et 50)")
    print("2. Normal (nombre entre 1 et 100)")
    print("3. Difficile (nombre entre 1 et 200)")
    
    while True:
        try:
            difficulte = int(input("Entrez 1, 2 ou 3 : "))
            if difficulte == 1:
                return random.randint(1, 50), 50
            elif difficulte == 2:
                return random.randint(1, 100), 100
            elif difficulte == 3:
                return random.randint(1, 200), 200
            else:
                print("Choix invalide, veuillez entrer 1, 2 ou 3.")
        except ValueError:
            print(colored("Veuillez entrer un nombre valide.", "light_red"))

# Fonction pour gérer la logique du jeu

def juste_prix():
    essais = 0
    
    # Choisir la difficulté et générer un nombre
    
    nombre, limite = choisir_difficulte()
    trouve = False
    start_time = time.time()  # Démarrer le chronomètre

    print(f"Devinez un nombre entre 1 et {limite}: ")

    while not trouve:
        try:
            # Demander un nombre
            
            guess = int(input(colored("Entrez un nombre : ", "magenta")))
            essais += 1

            if guess < nombre:
                print(colored("C'est plus !", "blue"))
            elif guess > nombre:
                print(colored("C'est moins !", "blue"))
            else:
                
                # Calcul du temps écoulé
                
                elapsed_time = time.time() - start_time
                print(colored(f"Félicitations ! Vous avez trouvé le bon nombre !", "green"))
                print()
                print(f"Nombre d'essais : {essais}")
                print(colored(f"Temps écoulé : {elapsed_time:.2f} secondes", "yellow"))
                trouve = True
                
                # Demander à l'utilisateur s'il veut rejouer
                
                print()
                rejouer = input("Voulez-vous rejouer ? (y/n) : ").strip().lower()
                if rejouer == 'y':
                    essais = 0  # Réinitialiser le nombre d'essais pour une nouvelle partie
                    juste_prix()  # Relancer le jeu avec un nouveau nombre
                else:
                    print("Merci d'avoir joué ! À bientôt.")
        except ValueError:
            print(colored("Veuillez entrer un nombre valide.", "light_red"))

# Lancer le jeu

bienvenue()  # Afficher une seule fois le message de bienvenue
juste_prix()  # Lancer directement la partie de jeu