"""bulletin_dynamique.py - Gestionnaire de Bulletin de Notes Interactif"""

etudiant: dict[str, str] = {"nom": "Alex Smith", "classe": "Informatique 1"}
cours_info: tuple[str, str] = ("INF101", "Programmation & Algorithmique")
sessions_noms: list[str] = ["Session Automne", "Session Hiver"]
notes_grille: list[list[float]] = [[80.0, 85.0, -1.0, 90.0], [88.0, 92.0, 95.0, 100.0]]

def calculer_moyenne_session(notes: list[float]) -> float:
    """Calcule la moyenne d'une session en ignorant les absences (-1.0)."""
    somme = 0.0
    compte = 0
    for note in notes:
        if note == -1.0:
            continue
        somme += note
        compte += 1
    if compte == 0:
        return 0.0
    return somme / compte

def analyser_grille_notes(grille: list[list[float]]) -> tuple[list[float], float, str]:
    """Parcourt la liste 2D, calcule les moyennes et détermine la mention."""
    moyennes_sessions: list[float] = []
    for i, session in enumerate(grille):
        for note in session:
            if note > 100.0:
                print(f"⚠ Avertissement : Note > 100 décelée session {i + 1} ({note})")
                break
            else:
                pass
        moyenne_s = calculer_moyenne_session(session)
        moyennes_sessions.append(moyenne_s)
    moyenne_generale = sum(moyennes_sessions) / len(moyennes_sessions) if moyennes_sessions else 0.0
    if moyenne_generale >= 90.0:
        mention = "Excellence (A+)"
    elif moyenne_generale >= 80.0:
        mention = "Très Bien (A)" if moyenne_generale >= 85.0 else "Bien (B)"
    elif moyenne_generale >= 60.0:
        mention = "Passable (C)"
    else:
        mention = "Échec (F)"
    return moyennes_sessions, moyenne_generale, mention

def saisir_session_valide(max_sessions: int) -> int:
    """Demande et valide le numéro de session saisi par l'utilisateur."""
    while True:
        saisie = input(f"Sélectionnez la session (1 à {max_sessions}) : ").strip()
        if saisie.isdigit():
            num = int(saisie)
            if 1 <= num <= max_sessions:
                return num - 1
        print("❌ Saisie invalide. Veuillez entrer un numéro valide.")

def saisir_note_valide() -> float:
    """Demande et valide la saisie d'une note (entre 0 et 100 ou -1 pour absence)."""
    while True:
        try:
            valeur = float(input("Entrez la note (0 à 100, ou -1 pour absence) : "))
            if valeur == -1.0 or (0.0 <= valeur <= 100.0):
                return valeur
            else:
                print("❌ La note doit être entre 0 et 100 (ou -1).")
        except ValueError:
            print("❌ Veuillez entrer un nombre valide (ex: 85.5).")

def ajouter_note(grille: list[list[float]], sessions: list[str]) -> None:
    """Ajoute une nouvelle note dans la session choisie."""
    print("\n--- AJOUT D'UNE NOTE ---")
    idx_session = saisir_session_valide(len(sessions))
    nouvelle_note = saisir_note_valide()
    grille[idx_session].append(nouvelle_note)
    print(f"☑ Note {nouvelle_note} ajoutée à la session {sessions[idx_session]}.")

def modifier_note(grille: list[list[float]], sessions: list[str]) -> None:
    """Modifie une note existante dans une session."""
    print("\n--- MODIFICATION D'UNE NOTE ---")
    idx_session = saisir_session_valide(len(sessions))
    session_notes = grille[idx_session]
    if not session_notes:
        print("⚠ Aucune note présente dans cette session.")
        return

    print(f"Notes actuelles pour {sessions[idx_session]} :")
    for pos, note in enumerate(session_notes):
        print(f"  [{pos + 1}] Note : {note}")

    while True:
        choix = input(f"Entrez le numéro de la note à modifier (1 à {len(session_notes)}) : ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(session_notes):
            idx_note = int(choix) - 1
            break
        print("❌ Choix invalide.")

    nouvelle_note = saisir_note_valide()
    session_notes[idx_note] = nouvelle_note
    print("☑ Note modifiée avec succès.")

def supprimer_note(grille: list[list[float]], sessions: list[str]) -> None:
    """Supprime une note d'une session."""
    print("\n--- SUPPRESSION D'UNE NOTE ---")
    idx_session = saisir_session_valide(len(sessions))
    session_notes = grille[idx_session]
    if not session_notes:
        print("⚠ Aucune note présente dans cette session.")
        return
    print(f"Notes actuelles pour {sessions[idx_session]} :")
    for pos, note in enumerate(session_notes):
        print(f"  [{pos + 1}] Note : {note}")
    while True:
        choix = input(f"Entrez le numéro de la note à supprimer (1 à {len(session_notes)}) : ").strip()
        if choix.isdigit() and 1 <= int(choix) <= len(session_notes):
            idx_note = int(choix) - 1
            break
        print("❌ Choix invalide.")

    note_retiree = session_notes.pop(idx_note)
    print(f"🗑 Note {note_retiree} supprimée avec succès.")

def ajouter_session(grille: list[list[float]], sessions: list[str]) -> None:
    """Ajoute une nouvelle session complète dans la grille."""
    print("\n--- AJOUT D'UNE SESSION ---")
    nom_session = input("Entrez le nom de la nouvelle session : ").strip()
    if not nom_session:
        nom_session = f"Session {len(sessions) + 1}"

    sessions.append(nom_session)
    grille.append([])
    print(f"☑ Session '{nom_session}' créée avec succès.")

def afficher_bulletin(
        etudiant_info: dict[str, str],
        cours: tuple[str, str],
        noms_s: list[str],
        grille: list[list[float]]
) -> None:
    """Affiche le bulletin complet de l'élève."""
    moyennes, m_gen, mention = analyser_grille_notes(grille)
    print("\n==============================================")
    print("ÉLÈVE :", etudiant_info["nom"], "| CLASSE :", etudiant_info["classe"])
    print("COURS :", cours[0], "-", cours[1])
    print("==============================================")

    for idx, session_notes in enumerate(grille):
        print(f"{noms_s[idx]} - Notes ({len(session_notes)}) : {session_notes}")
        moy = moyennes[idx] if idx < len(moyennes) else 0.0
        print(f"   -> Moyenne : {round(moy, 2)} / 100")

    print("----------------------------------------------")
    print("🎓 MOYENNE GÉNÉRALE :", round(m_gen, 2), "/ 100")
    print("MENTION OBTENUE      :", mention)
    print("==============================================")


def menu_principal() -> None:
    """Boucle principale gérant le menu utilisateur."""
    while True:
        print("\n=== MENU DE GESTION DU BULLETIN ===")
        print("1. Afficher le bulletin")
        print("2. Ajouter une note")
        print("3. Modifier une note")
        print("4. Supprimer une note")
        print("5. Ajouter une nouvelle session")
        print("6. Quitter")

        choix = input("Choisissez une option (1-6) : ").strip()

        if choix == "1":
            afficher_bulletin(etudiant, cours_info, sessions_noms, notes_grille)
        elif choix == "2":
            ajouter_note(notes_grille, sessions_noms)
        elif choix == "3":
            modifier_note(notes_grille, sessions_noms)
        elif choix == "4":
            supprimer_note(notes_grille, sessions_noms)
        elif choix == "5":
            ajouter_session(notes_grille, sessions_noms)
        elif choix == "6":
            print("👋 Merci d'avoir utilisé le gestionnaire de bulletin. À bientôt !")
            break
        else:
            print("❌ Choix invalide. Veuillez saisir un nombre entre 1 et 6.")


if __name__ == "__main__":
    menu_principal()