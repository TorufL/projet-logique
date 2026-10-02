import copy

def initier_panier() -> dict[str, dict[str, float]]:
    """

    :return: retourne un panier d'achat sous forme d'un dictionnaire
    """
    return{
        "ordinateur": {"prix": 1200.00, "quantitée": 1},
        "souris": {"prix": 45.50, "quantitée": 2},
        "tapis_souris": {"prix": 10.00, "quantitée": 1},

    }

def calculer_total(panier: dict[str, dict[str, float]]) -> float:
    total = 0.00
    for produit, details in panier.items():
        total += details["prix"] * details["quantitée"]
    return total

def extraire_articles_premium(panier: dict[str, dict[str, float]], seuil = 100) -> dict[str, dict[str, float]]:
    return {
        produit: details for produit, details in panier.items() if details["prix"] > seuil
    }

def appliquer_promotion_safe(panier: dict[str, dict[str, float]], reduction: float) -> dict[str, dict[str, float]]:
    """
    Appliquer une réduction sur les articles de plus de 500$
    :param panier: mon panier
    :param reduction: % de reduction
    :return: un nouveau panier contenant les nouveaux prix pour des articles premium
    """

    nouveau_panier = copy.deepcopy(panier)
    for produit, details in nouveau_panier.items():
        if details["prix"] > 500:
            details["prix"] = round(details["prix"] * (1 - reduction), 2)
    return nouveau_panier

if __name__=="__main__":
    panier = initier_panier()
    print(f"panier initial ==> {panier}")
    total = calculer_total(panier)
    print(f"Total avant promotion: {total}")
    articles_premium = extraire_articles_premium(panier)
    panier_promotion = appliquer_promotion_safe(panier, 0.5)
    print(f"Panier après la promotion ==> {panier_promotion}")
    total_apres_promotion = calculer_total(panier_promotion)
    print(f"Total apres promotion ==> {total_apres_promotion}")