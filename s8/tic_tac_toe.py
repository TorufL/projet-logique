# ==============================
# Programme : Tic Tac Toe (Morpion)
# Auteur : Dalica Bouallouche
# ==============================
import random

def creer_grille():
    """
    Permet de créer la grille de départ (vide) pour le jeu Tic Tac Toe
    :return: La grille de départ
    """

    grille_depart = []

    # La variable _ (underscore) est utilisée dans une boucle for
    # lorsqu’on n’a pas besoin de la valeur de la variable dans le code.
    for _ in range(3):
        ligne = []
        for _ in range(3):
            ligne.append(" ")
        grille_depart.append(ligne)

    return grille_depart


def afficher_grille(grille):
    """
    Affiche la grille du jeu.
    :param grille: La grille qu'on veut afficher.
    :return: None
    """
    print("\n")
    for i in range(3):
        print(" | ".join(grille[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def est_pleine(grille):
    """
    Retourne de vérifier si la grille est pleine (ne contient que des 'o' et des 'x') ou non.
    :param grille: La grille du Tic Tac Toe
    :return: Retourne True si la grille est pleine et False sinon.
    """
    for ligne in grille:
        if " " in ligne:
            return False
    return True

def demander_position(joueur, grille):
    """
    Demande une position valide au joueur (1 à 9)
    :param joueur: Le symbole du joueur (x ou o)
    :param grille: la grille actuelle du tic tac toe
    :return: les numéros de ligne et de colonne déduites de la position entrée.
    """
    while True:
        try:
            position = int(input(f"{joueur}, choisis une case (1 à 9) : ")) - 1
            if position < 0 or position > 8:
                print("Entrez un nombre entre 1 et 9.")
                continue

            ligne = position // 3
            col = position % 3

            if grille[ligne][col] != " ":
                print("Case déjà occupée !")
                continue

            return ligne, col

        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

# ligne = position // 3
# colonne = position % 3

def verifier_victoire(grille, symbole):
    """
    Vérifie si le joueur avec le symbole donné a gagné.
    :param grille: La grille actuelle du jeu de Tic Tac Toe
    :param symbole: Le symbole du joueur à vérifier.
    :return: True si le joueur a gagné, False sinon.
    """
    # Vérifier les lignes
    for ligne in grille:
        if ligne.count(symbole) == 3:
            return True

    # Vérifier les colonnes
    for col in range(3):
        if grille[0][col] == symbole and grille[1][col] == symbole and grille[2][col] == symbole:
            return True

    # Vérifier les diagonales
    if grille[0][0] == symbole and grille[1][1] == symbole and grille[2][2] == symbole:
        return True
    if grille[0][2] == symbole and grille[1][1] == symbole and grille[2][0] == symbole:
        return True

    return False

if __name__ == "__main__":
    print("Bienvenue dans le jeu du Morpion (Tic Tac Toe) !")
    print("Les positions sont numérotées ainsi :")
    print("1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n")

    grille = creer_grille()

    symboles = ["x", "o"]

    joueur_actuel = random.choice(symboles)

    while True:
        afficher_grille(grille)
        ligne, col = demander_position(f"Joueur {joueur_actuel}", grille)

        grille[ligne][col] = joueur_actuel

        if verifier_victoire(grille, joueur_actuel):
            afficher_grille(grille)
            print(f"Félicitations ! Joueur {joueur_actuel} a gagné !")
            break

        if est_pleine(grille):
            afficher_grille(grille)
            print("Match nul !")
            break

        # Changer de joueur
        if joueur_actuel == "o":
            joueur_actuel = "x"
        else:
            joueur_actuel = "o"