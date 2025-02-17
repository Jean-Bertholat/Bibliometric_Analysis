#!/usr/bin/env python3

def concat_ris_files(output_file, input_files):
    """
    Concatène le contenu de plusieurs fichiers RIS en un seul fichier.
    Chaque fichier est ajouté tel quel dans le fichier de sortie.
    """
    with open(output_file, "w", encoding="utf-8") as outfile:
        for file in input_files:
            try:
                with open(file, "r", encoding="utf-8") as infile:
                    data = infile.read()
                    outfile.write(data)
                    # Ajoute une nouvelle ligne pour séparer les fichiers si besoin
                    if not data.endswith("\n"):
                        outfile.write("\n")
            except Exception as e:
                print(f"Erreur lors de l'ouverture du fichier {file} : {e}")

if __name__ == "__main__":
    # Définir ici le nom du fichier de sortie et la liste des fichiers RIS à concaténer
    output_file = "samples/scopus 1980-2025.ris"
    input_files = [
        "samples/scopus 1980-2019.ris",
        "samples/scopus 2020-2022.ris",
        "samples/scopus 2023-2025.ris"
    ]
    
    concat_ris_files(output_file, input_files)
    print(f"Les fichiers ont été concaténés dans {output_file}")
