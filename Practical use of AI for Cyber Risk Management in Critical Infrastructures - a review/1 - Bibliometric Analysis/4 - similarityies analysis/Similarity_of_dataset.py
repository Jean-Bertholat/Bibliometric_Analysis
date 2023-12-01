import pandas as pd

def lire_excel_et_comparer_colonnes(chemin_fichier):
    """ Lire un fichier Excel et comparer les deux premières colonnes pour les DOI. """
    try:
        # Charger le fichier Excel
        df = pd.read_excel(chemin_fichier)

        # Assurez-vous que les colonnes sont en string pour éviter les problèmes de format
        df.iloc[:, 0] = df.iloc[:, 0].astype(str)
        df.iloc[:, 1] = df.iloc[:, 1].astype(str)

            # Filtrer les DOI qui commencent par "10" pour chaque colonne
        filtered_doi1 = df.iloc[:, 0].astype(str).str.match(r'^10')
        filtered_doi2 = df.iloc[:, 1].astype(str).str.match(r'^10')
        
        # Afficher le nombre de DOI restants après le filtrage pour chaque colonne
        print(f"Nombre de DOI valides dans la première colonne: {filtered_doi1.sum()}")
        print(f"Nombre de DOI valides dans la deuxième colonne: {filtered_doi2.sum()}")

        # Appliquer le filtrage au DataFrame
        df = df[filtered_doi1 & filtered_doi2]

        if df.shape[1] < 2:
            print("Le fichier ne contient pas suffisamment de colonnes.")
            return None
        
        # Comparer les colonnes
        pourcentage = comparer_dois(df.iloc[:, 0], df.iloc[:, 1])
        return pourcentage
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier {chemin_fichier}: {e}")
        return None

def comparer_dois(doi1, doi2):
    """ Comparer deux Series de DOI et calculer le pourcentage de similarité. """
    # Supprimer les valeurs vides ou NaN
    doi1 = doi1.replace('', pd.NA).dropna()
    doi2 = doi2.replace('', pd.NA).dropna()

    # Calculer les similarités et les différences
    similaires = doi1[doi1.isin(doi2)].count()
    print(similaires)
    total = max(len(doi1), len(doi2))  # Prendre le nombre maximum de DOI entre les deux colonnes

    # Calculer le pourcentage de similarité
    pourcentage_similarite = (similaires / total) * 100
    return pourcentage_similarite

# Chemin du fichier Excel
chemin_fichier = './Cyber_security/similarities_cybersecurity.xlsx'

# Lire le fichier Excel et comparer les colonnes
pourcentage = lire_excel_et_comparer_colonnes(chemin_fichier)
if pourcentage is not None:
    print(f"Pourcentage de similarité : {pourcentage:.2f}%")

