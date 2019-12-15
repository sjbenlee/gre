import csv
from crawl_functions import crawl_en_pof_example, crawl_ko
from torrequest import TorRequest
from constants import fieldnames
tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)

words = list()
with open('gre2020-20191210-3.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		words.append(row)

new_words = list()
for w in words:
	if w['example'] == '' or w['en'] == ''  or w['pof'] == '':
		print(w['word'], 'en is empty, start crawling...')
		en, pof, example = crawl_en_pof_example(w['word'], tr)
		if example != '':
			w['example'] = example
		if w['en'] == '' and en != '':
			w['en'] = en
		if w['pof'] == '' and pof != '':
			w['pof'] = pof
		print(w['example'], w['en'], w['pof'])
		
	if w['ko'] == '' or w['pof_ko'] == '' or w['example_ko'] == '':
		print(w['word'], 'ko is empty, start crawling...')
		ko, pof_ko, example_ko = crawl_ko(w['word'], tr)
		if w['ko'] == ''  and ko != '':
			w['ko'] = ko
		if w['pof_ko'] == '' and pof_ko != '':
			w['pof_ko'] = pof_ko
		if w['example_ko'] == '' and example_ko != '':
			w['example_ko'] = example_ko
	new_words.append(w)


with open('gre2020-20191210-4.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames=fieldnames)
	writer.writeheader()
	for w in new_words:
		writer.writerow(w)

