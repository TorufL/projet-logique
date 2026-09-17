liste_nombres = [4,8,9,1,5]
liste_mois = ["Janvier","Février","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
liste_bool = [True,True,False,True]
liste_vide = []
liste_mixte = [8,"a","b",False,0,"514",9,True]

print(len(liste_nombres))
print(len(liste_mixte))
print(len(liste_vide))

print(liste_mois[1])
print(liste_mixte[5])

print(liste_mixte[-2])

print(liste_mois[0:3])
print(liste_mois[2:6])
print(liste_mois[:5])
print(liste_mois[5:])
print(liste_mois[-1:-3])
print(liste_mois[-4:-1])

print(liste_mois[3])
liste_mois[3] = "AVRIL"
print(liste_mois[3])
print(liste_mois[:])

liste_fruits = ["Peche","Kiwi","Cerise"]
liste_fruits.append("Banane")
print(liste_fruits)

liste_legumes = ["Carotte","Aubergine"]
liste_fruits.extend(liste_legumes)
print(liste_fruits)

liste_fruits.insert(0,"Pomme")
print(liste_fruits)

liste_fruits.pop(5)
print(liste_fruits)
liste_fruits.pop(4)
print(liste_fruits)
liste_fruits.remove("Kiwi")
print(liste_fruits)