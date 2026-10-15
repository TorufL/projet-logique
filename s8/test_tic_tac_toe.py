# ==============================
# Programme : Tic Tac Toe (Morpion)
# Auteur : Dalica Bouallouche
# ==============================
from tic_tac_toe import est_pleine, demander_position, verifier_victoire

# ============================
# Tests pour est_pleine
# ============================
def test_grille_vide():
    grille = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]
    resultat = est_pleine(grille)

    assert resultat is False

def test_grille_partiellement_pleine():
    grille = [["x", "o", "x"],
              ["o", "x", "o"],
              [" ", " ", " "]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is False

def test_grille_pleine():
    grille = [["x", "o", "x"],
              ["o", "x", "o"],
              ["o", "x", "o"]]
    resultat = est_pleine(grille)
    assert resultat is True

# ============================
# Tests pour verifier_victoire
# ============================
def test_victoire_ligne():
    grille = [["x", "x", "x"],
              ["o", " ", "o"],
              [" ", " ", " "]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is True

def test_victoire_colonne():
    grille = [["x", "o", "x"],
              ["x", "o", "o"],
              ["x", " ", " "]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is True

def test_victoire_diagonale():
    grille = [["x", "o", " "],
              ["o", "x", " "],
              [" ", " ", "x"]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is True

def test_victoire_diagonale_inverse():
    grille = [[" ", "o", "x"],
              ["o", "x", " "],
              ["x", " ", " "]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is True

def test_pas_de_victoire():
    grille = [["x", "o", "o"],
              ["o", "x", "x"],
              ["x", "x", "o"]]
    resultat = verifier_victoire(grille, "x")
    assert resultat is False

# ============================
# Tests pour demander_position
# ============================
def test_position_valide(monkeypatch):
    grille = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

    # Permet de simuler une lecture sur la console.
    # Le joueur choisit la case 5
    input = iter(["5"])
    monkeypatch.setattr('builtins.input', lambda _: next(input))

    ligne, col = demander_position("x", grille)

    # Position 5 correspond à ligne=1, col=1
    assert ligne == 1
    assert col == 1
    # Ou assert (ligne, col) == (1, 1)

def test_position_deja_occupee(monkeypatch):
    grille = [["x", " ", " "],
              [" ", "o", "o"],
              [" ", " ", " "]]

    inputs = iter(["1", "7"])  # 1 est occupé, 5 est libre
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    ligne, col = demander_position("x", grille)

    assert ligne == 2
    assert col == 0
    # Ou assert (ligne, col) == (2, 0)

def test_position_hors_limites(monkeypatch):
    grille = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

    inputs = iter(["10", "3"])  # 10 invalide, 3 valide
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    ligne, col = demander_position("o", grille)

    assert (ligne, col) == (0, 2)  # Position 3 correspond à ligne=0, col=2

def test_position_non_entier(monkeypatch):
    grille = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]

    inputs = iter(["a", "2"])  # "a" invalide, "2" valide
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    ligne, col = demander_position("x", grille)

    assert (ligne, col) == (0, 1)  # Position 2 correspond à ligne=0, col=1
