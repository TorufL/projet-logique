try:
    nombre = int(input("Entrer un nombre: "))
    resultat = 10 / nombre
except ZeroDivisionError:
    print("Erreur. La valeur doit être différente de 0")

except ValueError:
    print("La valeur doit etre un nombre entier")
except:
    print("une erreur est survenue")
else:
    print(resultat)