import csv
import string
import sys

# Récupérer le nom du fichier source depuis la ligne de commande
if len(sys.argv) != 2:
    print("Veuillez fournir le nom du fichier source en argument.")
    sys.exit(1)
filename = sys.argv[1]

# Ouvrir le fichier texte en mode lecture
with open(filename, 'r') as f:
    # Lire la liste des mots à exclure depuis le fichier exclude.txt
    with open('exclude.txt', 'r') as ex:
        exclude_words = set(ex.read().split())
    # Créer un dictionnaire vide pour stocker les comptes de mots
    word_counts = {}
    # Parcourir chaque ligne du fichier
    for line in f:
        # Supprimer la ponctuation et les apostrophes de la ligne
        line = line.translate(str.maketrans('', '', string.punctuation + "'"))
        # Séparer la ligne en mots en utilisant l'espace comme séparateur
        words = line.strip().split()
        # Parcourir chaque mot et incrémenter son compteur dans le dictionnaire
        for word in words:
            if word not in exclude_words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
# Ouvrir le fichier CSV en mode écriture
with open('resultats.csv', 'w', newline='') as f:
    # Créer un objet writer pour écrire dans le fichier CSV
    writer = csv.writer(f)
    # Écrire l'en-tête du fichier CSV
    writer.writerow(['mot', 'nombre d\'occurence'])
    # Parcourir le dictionnaire de comptage de mots et écrire chaque entrée dans le fichier CSV
    for word, count in word_counts.items():
        writer.writerow([word, count])
