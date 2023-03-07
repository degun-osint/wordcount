import csv
import re
import sys

# get the name from CLI argument
if len(sys.argv) != 3:
    print("Veuillez fournir le nom du fichier source et le nom du fichier d'export en arguments.")
    sys.exit(1)
filename = sys.argv[1]
export_filename = sys.argv[2]

# open exclude list
with open(filename, 'r') as f:
    # read exclude list
    with open('exclude.txt', 'r') as ex:
        exclude_words = set(ex.read().split())
    # create an empty dictionnary
    word_counts = {}
    # read every line of the file
    for line in f:
        # delete punctuation and replace them with space
        line = re.sub(r'[^\w\s\']|"', ' ', line)
        line = line.lower()
        # separate line in words
        words = line.split(" ")
        # count each word, add them or increment the counter
        for word in words:
            if word not in exclude_words and len(word) > 2:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# Open CSV file
with open(export_filename, 'w', newline='') as f:
    # Create an object to fill the CSV file
    writer = csv.writer(f)
    # write headers
    writer.writerow(['word', 'occurence'])
    # add the dictionnay to csv
    for word, count in sorted_words:
        writer.writerow([word, count])
