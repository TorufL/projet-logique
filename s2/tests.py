nombre = 10
print(nombre)
nombre = nombre + 1
print(nombre)
nombre += 1
print(nombre)
nombre += 25
print(nombre)
#-----------------------------------------------------------------------------------------------------------------------
somme1=int(input("entrer le nombre #1:"))
somme2=int(input("entrer le nombre #2:"))
total= somme1 + somme2
print(total)
#-----------------------------------------------------------------------------------------------------------------------
t5=float(input("gg:"))
t4=float(input("gg:"))
total2= t4 + t5
print(total2)
#-----------------------------------------------------------------------------------------------------------------------
nom = "Cloutier"
prenom = "Olan"
nom_entier = nom + " " + prenom
print(nom_entier)
#-----------------------------------------------------------------------------------------------------------------------
nom = "Olan"
nomc = "logique de prog"
numg = 2
message1 = "Mon prénom est " + nom + " j'étudie en " + nomc + " dans le groupe " + str(numg)
message2 = f"Mon prénom est {nom} j'étudie en {nomc} dans le groupe {str(numg)}"
message3 = "Mon prénom est {} j'étudie en {} dans le groupe {}".format(nom,nomc,str(numg))

print(message1)
print(message2)
print(message3)
print(message3.upper())