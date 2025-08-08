import os
import tkinter as tk
from tkinter import filedialog, scrolledtext

def compter_fichiers(dossier):
    """Compte les fichiers dans un dossier (non récursif)."""
    return len([f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))])

def generer_arborescence(dossier, niveau=0):
    """Génère une chaîne représentant l'arborescence avec indentation et nombre de fichiers."""
    indent = "    " * niveau
    nb_fichiers = compter_fichiers(dossier)
    result = f"{indent}- {os.path.basename(dossier)} (fichiers: {nb_fichiers})\n"

    try:
        for item in sorted(os.listdir(dossier)):
            chemin_item = os.path.join(dossier, item)
            if os.path.isdir(chemin_item):
                result += generer_arborescence(chemin_item, niveau + 1)
    except PermissionError:
        result += f"{indent}  [Permission refusée]\n"

    return result

def parcourir_dossier():
    dossier = filedialog.askdirectory(title="Sélectionne le dossier racine")
    if dossier:
        resultat = generer_arborescence(dossier)
        zone_texte.delete('1.0', tk.END)
        zone_texte.insert(tk.END, f"Arborescence de : {dossier}\n\n{resultat}")

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Explorateur d'arborescence")
fenetre.geometry("700x500")

# Bouton de sélection
bouton_selection = tk.Button(fenetre, text="Choisir un dossier", command=parcourir_dossier)
bouton_selection.pack(pady=10)

# Zone de texte avec défilement
zone_texte = scrolledtext.ScrolledText(fenetre, wrap=tk.WORD, width=80, height=25)
zone_texte.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Lancer la boucle principale
fenetre.mainloop()
