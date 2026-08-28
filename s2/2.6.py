def moyenne_cours(note_c1, note_c2):
    total = note_c1 + note_c2
    moyenne = total/2
    return moyenne

def salutation(nom):
    print("Hello world", nom)


nom_personne = input("Entrez ton nom: ")
note_chimie = float(input("Entrez la note de chimie: "))
note_prog = float(input("Entrez la note de prog: "))

moyenne2 = moyenne_cours(note_chimie, note_prog)
salutation(nom_personne)
print("Ta moyenne est: ", moyenne2)