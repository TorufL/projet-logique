import pytest

#import tic_tac_toe as tt

from tic_tac_toe import (
    creer_grille,
    afficher_grille,
    verifier_victoire,
    est_pleine,
    demander_position
)

def test_creer_grille():
    grille_attendue = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    assert creer_grille() == grille_attendue

def test_est_pleine():
    grille = [
        ["x", "x", "o"],
        ["o", "x", "x"],
        ["x", "o", "o"]
    ]
    #Act
    resultat = est_pleine(grille)

    #Assert
    assert resultat == True

def test_verifier_victoire_colonne():
    grille = [
        ["x", "x", "o"],
        ["x", "o", "x"],
        ["x", "o", "o"]
    ]
    resultat = verifier_victoire(grille, "x")

    assert resultat is True

def test_verifier_victoire_ligne():
    grille = [
        ["x", "x", "x"],
        ["o", "o", "x"],
        ["x", "o", "o"]
    ]
    resultat = verifier_victoire(grille, "x")

    assert resultat is True

def test_verifier_victoire_diagonale():
    grille = [
        ["x", "x", "o"],
        ["o", "x", "x"],
        ["o", "o", "x"]
    ]
    resultat = verifier_victoire(grille, "x")

    assert resultat is True

def test_verifier_victoire_diagonale_inverse():
    grille = [
        ["o", "x", "x"],
        ["o", "x", "x"],
        ["x", "o", "o"]
    ]
    resultat = verifier_victoire(grille, "x")

    assert resultat is True

def test_verifier_pas_de_victoire():
    grille = [
        ["x", "x", "o"],
        ["o", "x", "x"],
        ["x", "o", "o"]
    ]
    resultat = verifier_victoire(grille, "x")

    assert resultat is False

def test_position_valide(monkeypatch):
    grille = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    choix_position = iter(["6"])

    monkeypatch.setattr("builtins.input", lambda _: next(choix_position))
    ligne, colonne = demander_position("x", grille)

    assert ligne == 1
    assert colonne == 2