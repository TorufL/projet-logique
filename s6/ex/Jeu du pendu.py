import random

print("="*50)

def choisir_mot(liste_mots):
    """
    Choisit un mot au hasard dans la liste de mots.

    :param liste_mots: Liste de mots
    :return: Le mot choisi
    """
    return random.choice(liste_mots)


def afficher_mot(mot_cache):
    """
    Affiche l’état actuel du mot (avec lettres et tirets bas).

    :param mot_cache: mot caché avec lettres et tirets
    :return: None
    """
    print(" ".join(mot_cache))


def demander_lettre(lettres_tentees):
    """
    Permet d'entrer une lettre valide.

    :param lettres_tentees: Toutes les lettres déjà entrées auparavant
    :return: La lettre entrée valide
    """
    while True:
        lettre = input("Entre une lettre : ")

        if len(lettre) != or not lettre.insalpha():
            print("wawa")
        elif lettre in lettres_tentees:
            print(f"efwefwef:{lettre}")
        else:
            return lettre



def maj_mot_cache(mot_secret, mot_cache, lettre):
    """
    Met à jour le mot caché avec la lettre trouvée.

    :param mot_secret: Le mot secret
    :param mot_cache: Le mot caché
    :param lettre: La lettre trouvée
    :return: None
    """
    for i in range(len(mot_cache)):
        if mot_secret[i] == lettre:
            mot_cache[i] = lettre


def verifier_lettre(mot_cache, mot_secret, lettre, vies):
    """
    Vérifie si la lettre est dans le mot ou non.

    :param mot_cache: Mot caché
    :param mot_secret: Mot secret
    :param lettre: Lettre à vérifier
    :param vies: nombre de vies restantes
    :return: nombre de vies restantes
    """
    if lettre in mot_secret:
        print("La lettre est dans le mot.")
        print("=" * 50)
        maj_mot_cache(mot_secret, mot_cache, lettre)
    else:
        vies -= 1
        print("Cette lettre n'est pas dans le mot.")
        print("Vies restantes :", vies)
        print("=" * 50)

    return vies


def mot_trouve(mot_cache):
    """
    Retourne True si le mot est entièrement découvert.

    :param mot_cache: mot caché
    :return: True si le mot est découvert, False sinon
    """
    return "_" not in mot_cache


def jouer():
    """
    Boucle principale du jeu du pendu.
    """
    liste_mots = ["python", "programmation", "ordinateur", "pendu", "liste", "etudiant", "allo", "bonjour", "cegep"]

    mot_secret = choisir_mot(liste_mots)
    mot_cache = ["_"] * len(mot_secret)
    lettres_tentees = []
    vies = 3*len(mot_secret)

    print("🎮 Bienvenue au jeu du pendu ! 🎮")
    print("Devine le mot secret :")

    afficher_mot(mot_cache)


    while vies > 0 and not mot_trouve(mot_cache):

        print("\nVies restantes :", vies)

        lettre = demander_lettre(lettres_tentees)

        if lettre not in lettres_tentees:
            lettres_tentees.append(lettre)
        vies = verifier_lettre(mot_cache, mot_secret, lettre, vies)

        print(f"Mot actuel: {mot_cache}")
        print(f"Lettres tentées: {lettres_tentees}")



    if mot_trouve(mot_cache):
        print("\n Bravo ! Tu as trouvé le mot :", mot_secret)
    else:
        print("\nTu as perdu !")
        print("Le mot secret était :", mot_secret)


# Lancer le jeu
jouer()