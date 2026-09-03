n1 = float(input("Nb1: "))
op = input("Entrer l'opérateur ) +, -, *, /): ")
n2 = float(input("nb2: "))

if op == "+":
    r = n1 + n2
elif op == "-":
    r = n1 - n2
elif op == "*":
    r = n1 * n2
elif op == "/":
    if n2 != 0:
        r = n1 / n2
    else:
        r = None
        print("La division par zéro est impossible")
else:
    r = None
    print("Opérateur invalide ou inconu")

if r != None:
    print("Resultat: ", r)