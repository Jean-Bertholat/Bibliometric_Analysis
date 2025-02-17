#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def is_year_in_intervals(year_str, intervals):
    """
    Vérifie si l'année (en chaîne) se trouve dans l'un des intervalles.
    Chaque intervalle est un tuple (début, fin) avec des entiers.
    """
    try:
        y = int(year_str)
    except ValueError:
        return False

    for lower, upper in intervals:
        if lower <= y <= upper:
            return True
    return False

def process_ris_file(input_file, output_file, remove_intervals):
    """
    Lit le fichier RIS, supprime les enregistrements dont l'année (champ PY)
    est incluse dans l'un des intervalles de remove_intervals, puis écrit le
    résultat dans output_file.
    """
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Découper le fichier par enregistrement (chaque enregistrement se termine par "ER  -")
    records = content.split("ER  -")
    filtered_records = []

    for record in records:
        record = record.strip()
        if not record:
            continue
        # Reconstituer l'enregistrement en ajoutant la ligne de fin "ER  -"
        record_full = record + "\nER  -\n"
        
        # Rechercher le champ PY (année) dans l'enregistrement
        match = re.search(r'^PY\s*-\s*(\d{4})', record, re.MULTILINE)
        if match:
            year = match.group(1)
            if is_year_in_intervals(year, remove_intervals):
                print(f"Suppression de l'enregistrement avec PY - {year}")
                continue  # On ne garde pas cet enregistrement
        # Conserver l'enregistrement
        filtered_records.append(record_full)

    # Écriture du fichier RIS filtré
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(filtered_records))
    print(f"Traitement terminé. Fichier généré : {output_file}")

# =======================
# Configuration des variables
# =======================

input_file = "dataset/scientific_researches/scopus 1980-2025.ris"       # Chemin vers votre fichier RIS d'entrée
output_file = "dataset/scientific_researches/scopus 2019-2025.ris"  

# Liste des intervalles à supprimer, sous la forme (année_début, année_fin)
# Par exemple, (2010, 2020) supprimera tous les enregistrements publiés entre 2010 et 2020 inclus.
# Pour supprimer uniquement 2015, utilisez (2015, 2015).
remove_intervals = [(1980, 2018)]  

# Exécuter la fonction de traitement
process_ris_file(input_file, output_file, remove_intervals)
