from Word import Word
from bs4 import BeautifulSoup


words = list()
with open('gre.csv') as f:
	for line in f:
		words.append(Word(line.strip()))


with open('ko.csv') as f:
	for line in f:
		data = line.split('/:/')
		word = data[0].strip()
		ko = data[1].strip()
		for w in words:
			if w.word == word:
				w.set_ko(ko)

with open('zh.csv') as f:
	for line in f:
		data = line.split('/:/')
		word = data[0].strip()
		zh = data[1].strip()
		en = data[2].strip()
		if len(data) == 5:
			us_s = data[3].strip()
			uk_s = data[4].strip()
			us_s = BeautifulSoup(us_s,'lxml')
			uk_s = BeautifulSoup(uk_s,'lxml')
			us = us_s.text
			uk = uk_s.text
		else:
			us = ''
			uk = ''

		for w in words:
			if w.word == word:
				w.set_zh(zh)
				w.set_en(en)
				w.set_pron_us(us)
				w.set_pron_uk(uk)


import csv
csv_columns = ['word', 'ko', 'zh', 'pron_us', 'pron_uk']
dict_list = list()
for w in words:
	dict_list.append({'word': w.word, 'ko': w.ko, 'zh': w.zh, 'pron_us': w.pron_us, 'pron_uk': w.pron_uk})

with open("gre_concat2.csv", "w") as f:
	writer = csv.DictWriter(f, fieldnames=csv_columns)
	writer.writeheader()
	for data in dict_list:
		writer.writerow(data)



