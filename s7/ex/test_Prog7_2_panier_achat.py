import pytest
from prog7_2_panier_achat import (
    initiliser_panier,
    calculer_total,
    extraire_articles_premium,
    appliquer_promotion_safe
)

def test_calculer_total():
    panier = {
         "ordinateur": {"prix": 1000.0, "quantite": 2},
        "souris": {"prix": 100.0, "quantite": 2},
        "tapis_souris": {"prix": 10.0, "quantite": 1},
    }

    assert calculer_total(panier) == 2210


@pytest.mark.parametrize("panier, total_attendu", [
    (
    {
         "ordinateur": {"prix": 1000.0, "quantite": 2},
        "souris": {"prix": 100.0, "quantite": 2},
        "tapis_souris": {"prix": 10.0, "quantite": 1},
    },
        2210
    ),
    (

{
         "ordinateur": {"prix": 2000.0, "quantite": 1},
        "souris": {"prix": 100.0, "quantite": 5},
        "tapis_souris": {"prix": 100.0, "quantite": 1},
    },
        2600
    )
])

def test_calculer_total2(panier, total_attendu):
    assert calculer_total(panier) == total_attendu