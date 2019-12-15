import csv
from constants import fieldnames

words = list()
with open('gre2020.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		row['syn'] = row['syn'][2:]
		words.append(row)

with open('gre2020-trim.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames)
	writer.writeheader()
	for row in words:
		writer.writerow(row)