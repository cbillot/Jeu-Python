import os
import time

##CREATION DE COULEUR

RESET = "\033[0m"
ROUGE = "\033[31m"
VERT = "\033[32m"

##FONCTIONS CLEAR

def console_clear():
    os.system('cls')

##FONCTIONS CREATION MAP + CREATION POSITIONS

victoire = False
map = []

for b in range(12):
    ligne = []
    for i in range(12):
        ligne.append(" ")
    map.append(ligne)

player_pos = [5, 5]
boite_pos = [9, 4]
case_pos = [8, 7]

def create_map():
    for i in range(12):
        map[0][i] = '#'
        map[11][i] = '#'
    j = 1
    while j < 11:
        map[j][0] ='#'
        map[j][11] ='#'
        j += 1
    
    map[player_pos[1]][player_pos[0]] = 'P'
    map[boite_pos[1]][boite_pos[0]] = 'X'
    map[case_pos[1]][case_pos[0]] = 'o'

##Fonction de check pour déterminer la victoire

def check_victoire():
    global victoire
    if map[case_pos[1]][case_pos[0]] == 'X':
        victoire = True


##Fonction d'affichage de la map

def print_map():
    for count in map:
        print(" ".join(count))

##FONCTIONS EXPLICATION DU JEU + LANCEMENT

def explication_jeu():
    print(f"\n{VERT}Bienvenue sur le jeu des boîtes !\n")
    print("Le but est très simple : ")
    print(f"Poussez les boîtes {ROUGE}'X'{VERT} vers leurs emplacements {ROUGE}'O'{VERT} en déplaçant votre personnage {ROUGE}'P'{VERT} contre celles-ci")
    print("Pour gagner il suffit simplement de ranger toutes les boîtes !")
    print(f"Utilisez {ROUGE}'ZQSD'{VERT} pour vous déplacer,")
    print(f"Si vous souhaitez quitter la partie appuyez sur {ROUGE}'V'{VERT}.")
    print(f"Si vous voulez reset la partie appuyez sur {ROUGE}'R'{VERT}.")

    lancement_jeu()

def lancement_jeu():
    print("Êtes-vous prêt à jouer ? (Appuyez sur 'Y' pour Oui, 'N' pour Non)")

    reponse = input().strip().upper()

    if reponse == 'Y':
        print("Lancement du jeu...")
        boucle_jeu()
    elif reponse == 'N':
        console_clear()
        print("Dommage... à bientôt !")
    else:
        console_clear()
        print("Erreur vous avez rentré la mauvaise lettre !")
        lancement_jeu()

##FONCTIONS BOUCLE DU JEU + GESTION DES TOUCHES

def boucle_jeu():
    global victoire
    console_clear()
    print("Chargement...")
    time.sleep(1)
    create_map()

    while True:
        console_clear()
        print_map()
        check_victoire()

        if victoire == True:
            print("Victoire !!!\n")
            break

        try:
            key = input("Déplacez vous : ").strip().upper()
        except KeyboardInterrupt:
            print("\nJeu interrompu.")
            break

        if key == 'V':
            console_clear()
            print("Vous avez quitté le jeu !")
            break
        elif key == 'R':
            console_clear()
            print("Map reset")
            create_map()
        elif key == 'Z':
            deplacement_haut()
        elif key == 'S':
            deplacement_bas()
        elif key == 'Q':
            deplacement_gauche()
        elif key == 'D':
            deplacement_droite()

##FONCTIONS DEPLACEMENTS DU JOUEUR

def deplacement_haut():
    global victoire
    if map[player_pos[1] - 1][player_pos[0]] != '-' and map[player_pos[1] - 1][player_pos[0]] != '|':
        if map[player_pos[1] - 1][player_pos[0]] == ' ':
            map[player_pos[1]][player_pos[0]] = ' '
            player_pos[1] -= 1
            map[player_pos[1]][player_pos[0]] = 'P'
        elif map[player_pos[1] - 1][player_pos[0]] == 'X':
            if map[player_pos[1] - 2][player_pos[0]] == ' ':
                map[player_pos[1]][player_pos[0]] = ' '
                boite_pos[1] -= 1
                map[boite_pos[1]][boite_pos[0]] = 'X'
                player_pos[1] -= 1
                map[player_pos[1]][player_pos[0]] = 'P'
            elif map[player_pos[1] - 2][player_pos[0]] == 'o':
                map[player_pos[1]][player_pos[0]] = ' '
                map[boite_pos[1]][boite_pos[0]] = ' '
                map[case_pos[1]][case_pos[0]] = 'X'
                player_pos[1] -= 1
                map[player_pos[1]][player_pos[0]] = 'P'
                victoire = True
                return

def deplacement_bas():
    global victoire
    if map[player_pos[1] + 1][player_pos[0]] != '-' and map[player_pos[1] + 1][player_pos[0]] != '|':
        if map[player_pos[1] + 1][player_pos[0]] == ' ':
            map[player_pos[1]][player_pos[0]] = ' '
            player_pos[1] += 1
            map[player_pos[1]][player_pos[0]] = 'P'
        elif map[player_pos[1] + 1][player_pos[0]] == 'X':
            if map[player_pos[1] + 2][player_pos[0]] == ' ':
                map[player_pos[1]][player_pos[0]] = ' '
                boite_pos[1] += 1
                map[boite_pos[1]][boite_pos[0]] = 'X'
                player_pos[1] += 1
                map[player_pos[1]][player_pos[0]] = 'P'
            elif map[player_pos[1] + 2][player_pos[0]] == 'o':
                map[player_pos[1]][player_pos[0]] = ' '
                map[boite_pos[1]][boite_pos[0]] = ' '
                map[case_pos[1]][case_pos[0]] = 'X'
                player_pos[1] += 1
                map[player_pos[1]][player_pos[0]] = 'P'
                victoire = True
                return

def deplacement_gauche():
    global victoire
    if map[player_pos[1]][player_pos[0] - 1] != '-' and map[player_pos[1]][player_pos[0] - 1] != '|':
        if map[player_pos[1]][player_pos[0] - 1] == ' ':
            map[player_pos[1]][player_pos[0]] = ' '
            player_pos[0] -= 1
            map[player_pos[1]][player_pos[0]] = 'P'
        elif map[player_pos[1]][player_pos[0] - 1] == 'X':
            if map[player_pos[1]][player_pos[0] - 2] == ' ':
                map[player_pos[1]][player_pos[0]] = ' '
                boite_pos[0] -= 1
                map[boite_pos[1]][boite_pos[0]] = 'X'
                player_pos[0] -= 1
                map[player_pos[1]][player_pos[0]] = 'P'
            elif map[player_pos[1]][player_pos[0] - 2] == 'o':
                map[player_pos[1]][player_pos[0]] = ' '
                map[boite_pos[1]][boite_pos[0]] = ' '
                map[case_pos[1]][case_pos[0]] = 'X'
                player_pos[0] -= 1
                map[player_pos[1]][player_pos[0]] = 'P'
                victoire = True
                return

def deplacement_droite():
    global victoire
    if map[player_pos[1]][player_pos[0] + 1] != '-' and map[player_pos[1]][player_pos[0] + 1] != '|':
        if map[player_pos[1]][player_pos[0] + 1] == ' ':
            map[player_pos[1]][player_pos[0]] = ' '
            player_pos[0] += 1
            map[player_pos[1]][player_pos[0]] = 'P'
        elif map[player_pos[1]][player_pos[0] + 1] == 'X':
            if map[player_pos[1]][player_pos[0] + 2] == ' ':
                map[player_pos[1]][player_pos[0]] = ' '
                boite_pos[0] += 1
                map[boite_pos[1]][boite_pos[0]] = 'X'
                player_pos[0] += 1
                map[player_pos[1]][player_pos[0]] = 'P'
            elif map[player_pos[1]][player_pos[0] + 2] == 'o':
                map[player_pos[1]][player_pos[0]] = ' '
                map[boite_pos[1]][boite_pos[0]] = ' '
                map[case_pos[1]][case_pos[0]] = 'X'
                player_pos[0] += 1
                map[player_pos[1]][player_pos[0]] = 'P'
                victoire = True
                return

explication_jeu()
