import csv

words = list()
rows = list()
with open('gre2020-20191215.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        words.append(row['word'])
        rows.append(row)

words = list(set(words))

print('number of words:', len(words))
print('number of rows:', len(rows))
print('duplicates:', len(rows) - len(words))
print('keys:', ', '.join(rows[0].keys()))

keys = list(rows[0].keys())

new_rows = list()
for word in words:
    new_rows.append({'word': word})

keys.remove('word')



for nr in new_rows:
    for key in keys:
        nr[key] = ''

    for row in rows:
        if row['word'] == nr['word']:
            for key in keys:
                if nr[key] == '' and row[key] != '':
                    nr[key] = row[key].strip()

                if nr[key] != '' and nr[key] != row[key].strip():
                    if len(row[key]) > len(nr[key]):
                        nr[key] = row[key]

with open('gre2020-20191215-trimmed.csv', 'w') as f:
    fieldnames = list(new_rows[0].keys())
    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    for nr in new_rows:
        writer.writerow(nr)

rows = list()
with open('gre2020-20191215-trimmed.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

print('number of words trimmed:', len(rows))
