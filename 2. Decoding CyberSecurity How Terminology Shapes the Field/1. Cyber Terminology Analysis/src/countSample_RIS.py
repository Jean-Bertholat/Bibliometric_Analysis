# In order to check the dl from scopus is good
# If the number match the number of results in the scopus search it's good

def count_samples_in_ris_file(filename):
    """
    Compte le nombre d'échantillons dans un fichier RIS.
    Un échantillon est considéré comme terminé lorsqu'une ligne commence par 'ER  -'.
    """
    count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # On vérifie si la ligne correspond exactement à la fin d'un échantillon.
            if line.strip() == "ER  -":
                count += 1
    return count

if __name__ == "__main__":
    # Nom du fichier RIS à analyser
    filename = "dataset/scientific_researches/scopus 1980-2025.ris"  # Remplacez par le nom de votre fichier RIS
    total_samples = count_samples_in_ris_file(filename)
    print(f"Nombre d'échantillons dans le fichier : {total_samples}")
