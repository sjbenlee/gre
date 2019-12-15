import csv
from constants import fieldnames


words = list()
with open ('gre2020-20191209.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for f in fieldnames:
            if f not in row:
                row[f] = ''
        words.append(row)

with open('gre2020-20191209-2.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in words:
        writer.writerow(w)

new_words = list()
with open('new_words.csv') as f:
    reader = csv.DictReader(f)
    for w in words:
        for row in reader:
            if row['word'] == w['word']:
                for f in fieldnames:
                    if w[f] == '' and row[f] != '':
                        w[f] = row[f]
        new_words.append(w)

with open('gre2020-20191209-3.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for w in new_words:
        writer.writerow(w)