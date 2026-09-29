etudiant={"nom":"Alex Smith","classe":"Informatique 1"}
cours_info=("INF101","Programmation & Algorithmique")
sessions_noms=["Session Automne","Session Hiver"]
notes_grille=[[80.0,85.0,-1.0,90.0],[88.0,92.0,95.0,100.0]]

def calculer_moyenne_session(notes):
    n=[x for x in notes if x!=-1.0]
    return sum(n)/len(n) if n else 0.0

def analyser_grille_notes(grille):
    moyennes=[]
    for i,s in enumerate(grille):
        for note in s:
            if note>100.0:
                print(f"⚠ Avertissement : Note > 100 décelée session {i+1} ({note})")
                break
        moyennes.append(calculer_moyenne_session(s))
    g=sum(moyennes)/len(moyennes) if moyennes else 0.0
    mention="Excellence (A+)" if g>=90 else "Très Bien (A)" if g>=85 else "Bien (B)" if g>=80 else "Passable (C)" if g>=60 else "Échec (F)"
    return moyennes,g,mention

def saisir_session_valide(max_sessions):
    while True:
        saisie=input(f"Sélectionnez la session (1 à {max_sessions}) : ").strip()
        if saisie.isdigit() and 1<=int(saisie)<=max_sessions:return int(saisie)-1
        print("❌ Saisie invalide. Veuillez entrer un numéro valide.")

def saisir_note_valide():
    while True:
        try:
            valeur=float(input("Entrez la note (0 à 100, ou -1 pour absence) : "))
            if valeur==-1.0 or 0.0<=valeur<=100.0:return valeur
            print("❌ La note doit être entre 0 et 100 (ou -1).")
        except ValueError:
            print("❌ Veuillez entrer un nombre valide (ex: 85.5).")

def ajouter_note(grille,sessions):
    print("\n--- AJOUT D'UNE NOTE ---")
    i=saisir_session_valide(len(sessions));n=saisir_note_valide()
    grille[i].append(n)
    print(f"☑ Note {n} ajoutée à la session {sessions[i]}.")

def modifier_note(grille,sessions):
    print("\n--- MODIFICATION D'UNE NOTE ---")
    i=saisir_session_valide(len(sessions));s=grille[i]
    if not s:
        print("⚠ Aucune note présente dans cette session.");return
    print(f"Notes actuelles pour {sessions[i]} :")
    for j,n in enumerate(s):print(f"  [{j+1}] Note : {n}")
    while True:
        c=input(f"Entrez le numéro de la note à modifier (1 à {len(s)}) : ").strip()
        if c.isdigit() and 1<=int(c)<=len(s):j=int(c)-1;break
        print("❌ Choix invalide.")
    s[j]=saisir_note_valide()
    print("☑ Note modifiée avec succès.")

def supprimer_note(grille,sessions):
    print("\n--- SUPPRESSION D'UNE NOTE ---")
    i=saisir_session_valide(len(sessions));s=grille[i]
    if not s:
        print("⚠ Aucune note présente dans cette session.");return
    print(f"Notes actuelles pour {sessions[i]} :")
    for j,n in enumerate(s):print(f"  [{j+1}] Note : {n}")
    while True:
        c=input(f"Entrez le numéro de la note à supprimer (1 à {len(s)}) : ").strip()
        if c.isdigit() and 1<=int(c)<=len(s):j=int(c)-1;break
        print("❌ Choix invalide.")
    print(f"🗑 Note {s.pop(j)} supprimée avec succès.")

def ajouter_session(grille,sessions):
    print("\n--- AJOUT D'UNE SESSION ---")
    nom=input("Entrez le nom de la nouvelle session : ").strip() or f"Session {len(sessions)+1}"
    sessions.append(nom);grille.append([])
    print(f"☑ Session '{nom}' créée avec succès.")

def afficher_bulletin(e,c,s,g):
    m,mg,mention=analyser_grille_notes(g)
    print("\n==============================================")
    print("ÉLÈVE :",e["nom"],"| CLASSE :",e["classe"])
    print("COURS :",c[0],"-",c[1])
    print("==============================================")
    for i,n in enumerate(g):
        print(f"{s[i]} - Notes ({len(n)}) : {n}")
        print(f"   -> Moyenne : {round(m[i],2)} / 100")
    print("----------------------------------------------")
    print("🎓 MOYENNE GÉNÉRALE :",round(mg,2),"/ 100")
    print("MENTION OBTENUE      :",mention)
    print("==============================================")

while True:
    print("\n=== MENU DE GESTION DU BULLETIN ===")
    print("1. Afficher le bulletin")
    print("2. Ajouter une note")
    print("3. Modifier une note")
    print("4. Supprimer une note")
    print("5. Ajouter une nouvelle session")
    print("6. Quitter")
    choix=input("Choisissez une option (1-6) : ").strip()
    if choix=="1":afficher_bulletin(etudiant,cours_info,sessions_noms,notes_grille)
    elif choix=="2":ajouter_note(notes_grille,sessions_noms)
    elif choix=="3":modifier_note(notes_grille,sessions_noms)
    elif choix=="4":supprimer_note(notes_grille,sessions_noms)
    elif choix=="5":ajouter_session(notes_grille,sessions_noms)
    elif choix=="6":
        print("👋 Merci d'avoir utilisé le gestionnaire de bulletin. À bientôt !");break
    else:print("❌ Choix invalide. Veuillez saisir un nombre entre 1 et 6.")