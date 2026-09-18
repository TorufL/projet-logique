notes_eleves = [
    [14,16,18],
    [10,12,11],
    [20,19,18]
]

print(notes_eleves)
print(notes_eleves[0][0])

#Moyenne

numero_eleve = 1
for notes in notes_eleves:
    somme = sum(notes)
    moyenne = somme / len(notes)
    print(f"Élève {numero_eleve} - Moyene : {moyenne:.2f}")
    numero_eleve += 1