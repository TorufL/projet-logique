# Dictionnaire: Profil étudiant

etudiant = {
    "nom":"Alex Smith",
    "technique":"Informatique"
}

# Tuple (Info du cours)

cours_info = ("INF101", "Logique de programmation")

# Liste 1D : Noms des sessions

session_noms = ["Session Automne", "Session Hiver"]

# Liste 2D : Grille des notes pour deux sessions

notes_grille = [
    [80,85,90],
    [88,92,95]
]

# Calcul moyenne deux sessions

def calculer_moyenne(grille_notes):
    moyenne_s1 = sum(grille_notes[0]) / len(grille_notes[0])
    moyenne_s2 = sum(grille_notes[1]) / len(grille_notes[1])

    moyenne_generale = (moyenne_s1 + moyenne_s2)/2
    return moyenne_s1, moyenne_s2, moyenne_generale

# appel de la fonction

moyenne_s1, moyenne_s2, moyenne_generale = calculer_moyenne((notes_grille))

# Affichage du bulletin

print("=" * 55)
print("Éleve: ", etudiant["nom"], ", Technique: ", etudiant["technique"])
print("Cours: ", cours_info[0], "- ", cours_info[1])
print("=" * 55)
print(session_noms[0], "-Notes: ", notes_grille[0])
print("Moyenne s1: ", moyenne_s1)
print(session_noms[1], "-Notes: ", notes_grille[1])
print("Moyenne s2: ", moyenne_s2)
print("=" * 55)
print("Moyenne générale: ", moyenne_generale)
print("=" * 55)
