def categorie_age():
    """
    Fonction qui retourne une chaîne de caractères indiquant s'il
    s'agit d'un adulte ou non selon l'âge entré en paramètre.
    :param age: l'age de la personne (entier positif)
    :return: Un string indiquant la catégorie de la personne.
            Valeurs attendues : "Adulte" ou "Enfant ou Adolescent"
    """
    if age >= 18:
        categorie = "adulte"
    else:
        categorie = "adolescent"

    return categorie

if __name__ == "__main__":
nom = input("Entrez un prénom : ")
prenom = input("Entrez un nom : ")