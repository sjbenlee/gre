import csv

def trim(text):
	l = text.split(',')
	l = [a.strip() for a in l]
	l = list(set(l))
	return ', '.join(l)


rows = list()
with open('gre2020-thesaurus-var.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		row['hyper'] = trim(row['hyper'])
		row['hypo'] = trim(row['hypo'])
		row['syn'] = trim(row['syn'])
		row['ant'] = trim(row['ant'])
		row['var'] = trim(row['var'])
		rows.append(row)

fieldnames = ['word', 'ko', 'zh_Hans', 'etym_zh_Hans', 'pron', 'ant', 'syn', 'etym', 'hypo', 'hyper', 'var']
with open('gre2020-trimmed.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames)
	writer.writeheader()
	for row in rows:
		writer.writerow(row)
