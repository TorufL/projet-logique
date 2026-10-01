def afficher_info(info):
    print(info["nom"]),
    print(info["prenom"]),
    print(info["age"]),
    print(info["ville"])

def afficher_info2(nom, prenom, age, ville):
    print(f"{nom} {prenom} a {age}, et habite à {ville}")

def ajouter_pays(info):
    info["pays"] = "Canada"

info_client = {
    "nom": "Alex",
    "prenom": "Bob",
    "age": 30,
    "ville": "Gatineau"
}

if __name__ == "__main__":
    afficher_info(info_client)
    afficher_info2(**info_client)
    ajouter_pays(info_client)
    print(info_client)