# ==============================
# Programme : Chasse au trésor avec Zigomar
# Auteur : E.M
# ==============================

import random


def ajouter_objets(sac: list, objets: list) -> None:
    """
    Ajoute plusieurs objets dans le sac de Zigomar.

    :param sac: Le sac contenant les objets.
    :param objets: Les nouveaux objets à ajouter.
    :return: None
    """
    for objet in objets:
        sac.append(objet)


def contient_chiffre(texte: str) -> bool:
    """
    Vérifie si une chaîne contient au moins un chiffre.

    :param texte: Texte à vérifier.
    :return: True si un chiffre est présent, False sinon.
    """
    for caractere in texte:
        if caractere.isdigit():
            return True

    return False


def doit_etre_retire(objet: str) -> bool:
    """
    Détermine si un objet doit être retiré automatiquement (chiffre ou lettre 'b').

    :param objet: Nom de l'objet.
    :return: True si l'objet doit être retiré.
    """
    nom = objet.lower()

    if contient_chiffre(nom):
        return True

    if "b" in nom:
        return True

    return False


def tri_automatique(sac: list) -> list:
    """
    Retire du sac tous les objets interdits.

    :param sac: Le sac de Zigomar.
    :return: Le sac après le tri.
    """
    nouveau_sac = []

    for objet in sac:
        if not doit_etre_retire(objet):
            nouveau_sac.append(objet)

    return nouveau_sac


def retirer_objet(sac: list) -> None:
    """
    Demande à l'utilisateur quel objet retirer du sac et gère les erreurs.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    if len(sac) == 0:
        print("Le sac est vide.")
        return

    print("\nObjets présents dans le sac :")

    for i in range(len(sac)):
        print(i + 1, "-", sac[i])

    try:
        choix = input("Quel objet ou numéro de case veux-tu retirer ? ")

        if choix.isdigit():
            numero = int(choix) - 1
            if 0 <= numero < len(sac):
                objet_retire = sac.pop(numero)
                print(objet_retire, "a été retiré du sac.")
            else:
                print("Ce numéro de case n'existe pas.")

        elif choix in sac:
            sac.remove(choix)
            print(choix, "a été retiré du sac.")
        else:
            print("Cet objet n'est pas dans le sac.")

    except (KeyboardInterrupt, EOFError):
        print("\nAction annulée.")


def verifier_taille_sac(sac: list) -> None:
    """
    Vérifie la taille du sac et déclenche un tri si nécessaire.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    if len(sac) >= 15:
        print("\nZigomar a trop d'objets !")
        print("Elle effectue un tri automatique...")

        ancien_nombre = len(sac)

        sac[:] = tri_automatique(sac)

        nouveau_nombre = len(sac)

        print(
            ancien_nombre - nouveau_nombre,
            "objet(s) retiré(s)."
        )


def melanger_sac(sac: list) -> None:
    """
    Mélange aléatoirement les objets du sac.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    random.shuffle(sac)


def quiz(sac: list) -> None:
    """
    Choisit un objet au hasard et lance le mini-quiz.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    if len(sac) == 0:
        print("Impossible de faire le quiz : le sac est vide.")
        return

    objet = random.choice(sac)

    print("\n--- MINI-QUIZ ---")
    print("Zigomar a choisi un objet au hasard.")

    try:
        reponse = input("À ton avis, quel objet a-t-elle choisi ? ")

        if reponse.lower() == objet.lower():
            print("Bravo ! Zigomar saute de joie !")
            print("Merci ! Tu as trouvé :", objet)
        else:
            print("Mauvaise réponse !")
            print("Zigomar te lance un regard noir...")
            print("L'objet était :", objet)

    except (KeyboardInterrupt, EOFError):
        print("\nQuiz annulé.")


def trier_sac(sac: list) -> None:
    """
    Trie le sac par ordre alphabétique.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    sac.sort()


def afficher_sac(sac: list) -> None:
    """
    Affiche tous les objets du sac ainsi que leur quantité totale.

    :param sac: Le sac de Zigomar.
    :return: None
    """
    print("\n--- SAC DE ZIGOMAR ---")

    if len(sac) == 0:
        print("Le sac est vide.")
    else:
        for objet in sac:
            print("-", objet)

    print("Nombre d'objets :", len(sac))


def chasse_au_tresor() -> None:
    """
    Fonction principale qui simule la chasse au trésor de Zigomar.

    :return: None
    """
    sac = [
        "potion scintillante",
        "clé mystérieuse",
        "boule brillante",
        "squelette miniature"
    ]

    print("Bienvenue dans la chasse au trésor de Zigomar !")

    afficher_sac(sac)

    objets_trouves = [
        "diamant",
        "rubis",
        "boussole",
        "épée",
        "carte",
        "pièce d'or",
        "cristal",
        "bouclier",
        "lampe",
        "livre",
        "couronne",
        "perle"
    ]

    print("\nZigomar part explorer les environs...")

    for objet in objets_trouves:
        print("\nZigomar trouve :", objet)

        ajouter_objets(sac, [objet])

        print("Nombre d'objets :", len(sac))

        verifier_taille_sac(sac)

    afficher_sac(sac)

    melanger_sac(sac)
    quiz(sac)

    print("\nZigomar veut maintenant ranger son sac.")
    trier_sac(sac)

    print("Sac trié par ordre alphabétique :")
    afficher_sac(sac)


if __name__ == "__main__":
    try:
        chasse_au_tresor()
    except (KeyboardInterrupt, EOFError):
        print("\n\nPartie quittée. À bientôt !")