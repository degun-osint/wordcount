import csv
import string
import sys

# get the name from CLI argument
if len(sys.argv) != 2:
    print("please enter the text file path")
    sys.exit(1)
filename = sys.argv[1]

# open exclude list
with open(filename, 'r') as f:
    # read exclude list
    with open('exclude.txt', 'r') as ex:
        exclude_words = set(ex.read().split())
    # create an empty dictionnary
    word_counts = {}
    # read every line of the file
    for line in f:
        # delete punctuation and apostrophes
        line = line.translate(str.maketrans('', '', string.punctuation + "'"))
        # separate line in words
        words = line.strip().split()
        # count each word, add them or increment the counter
        for word in words:
            if word not in exclude_words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
# Open CSV file
with open('resultats.csv', 'w', newline='') as f:
    # Create an object to fill the CSV file
    writer = csv.writer(f)
    # write headers
    writer.writerow(['word', 'occurence'])
    # add the dictionnay to csv
    for word, count in word_counts.items():
        writer.writerow([word, count])
