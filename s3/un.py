age = int(input("Entrer ton age: "))

if age >= 18:
    print("Adulte")
elif age >= 13:
    print("Adolescent")
else:
    print("Enfant")

fruit = input("Saisissez le fruit: ")

if fruit == "Banane" or fruit == "Ananas":
    print(f"le fruit {fruit} est jaune")
elif fruit == "Fraise" or fruit == "Orange":
    print(f"Le fruit {fruit} est orange")
elif fruit == "Poire":
    print(f"Le fruit {fruit} et rose")
else:
    print(f"Désolé! le fruit {fruit} , je ne le reconnais pas")