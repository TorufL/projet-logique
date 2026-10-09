print("======================================")
print("     DEVINER VOTRE JOUR D'ANNIVERSAIRE")
print("======================================")
print()

print("Pensez à votre jour d'anniversaire")
print("(entre 1 et 31), sans me le dire.")
print()

# Les 5 tableaux
tableaux = [
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
    [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
    [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
    [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
    [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
]

# Valeurs associées aux tableaux
valeurs = [1, 2, 4, 8, 16]

jour = 0

for i in range(5):
    print("Votre jour apparaît-il dans ce tableau ?")
    print(tableaux[i])

    reponse = input("Répondez par oui ou non : ")

    if reponse.lower() == "oui":
        jour = jour + valeurs[i]

    print()

print("Votre jour d'anniversaire est le", jour, "!")