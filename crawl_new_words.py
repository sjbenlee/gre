from torrequest import TorRequest
import random
from bs4 import BeautifulSoup
from Word import Word
from constants import BLANK, browsers, fieldnames
import csv
import os
import time

if not os.path.exists('sounds'):
	os.mkdir('sounds')


words = list()
# with open('new_words.txt') as f:
#     for line in f:
#         w = dict()
#         w['word'] = line.strip()
#         words.append(w)

with open('new_words.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		words.append(row)
		# print(row)


def save_words(words, fieldnames):
	with open('new_words.csv', 'w') as f:
		writer = csv.DictWriter(f, fieldnames=fieldnames)
		writer.writeheader()
		for row in words:
			writer.writerow(row)


def crawl_en(words, tr, headers):
	new_words = list()
	for w in words:
		print(w)
		# try:
		re = tr.get("https://endic.naver.com/search.nhn?sLn=en&query=%s&searchOption=all&isOnlyViewEE=Y" % w['word'].replace(' ', BLANK), headers=headers)
		s = BeautifulSoup(re.text, 'lxml')

		# part_of_speech = s.find('span', {'data-type': 'ore', 'data-lang': 'en'})
		content_div = s.find('div', {'id': 'content'})
		dl_e2 = content_div.find('dl', {'class': 'list_e2'})
		dd = dl_e2.find('dd')
		k09 = dd.find('span', {'class': 'fnt_k09'})
		if k09 != None:
			pof = k09.text
		else:
			pof = ''

		# k05 = k09.find_next_sibling()
		k05 = dd.find('span', {'class': 'fnt_k05'})
		
		if k05 != None:
			en = k05.text
		else:
			en = ''

		f07 = dl_e2.find('span', {'class': 'fnt_e07 _ttsText'})

		w['pof'] = pof
		w['en'] = en
		if f07 != None:
			w['example'] = f07.text
		else:
			w['example'] = ''
		new_words.append(w)
		save_words(new_words, fieldnames)
		# except:
		#     pass

		dt_first = dl_e2.find('dt', {'class': 'first'})
		a_list = dt_first.findAll('a')
		for a in a_list:
			if 'playlist' in a.attrs:
				p = a['playlist']
				doc = tr.get(p)
				with open('sounds/%s.mp3' % w['word'], 'wb') as f:
					f.write(doc.content)
				break
			
		# print(len(a_list))
		# print(a_list)
		# us_span = us_string.find_parent()
		# a = span_us.find_next_sibling('a')
		# if a != None:
		#     print(a)
		# break


	return new_words

def crawl_ko(words, tr, headers):
	new_words = list()
	for w in words:
		print(w)
		re = tr.get("https://endic.naver.com/search.nhn?sLn=en&isOnlyViewEE=N&query=%s" % w['word'].replace(' ', BLANK), headers=headers)
		s = BeautifulSoup(re.text, 'lxml')

		# part_of_speech = s.find('span', {'data-type': 'ore', 'data-lang': 'en'})
		content_div = s.find('div', {'id': 'content'})
		dl_e2 = content_div.find('dl', {'class': 'list_e2'})
		dd = dl_e2.find('dd')
		k09 = dd.find('span', {'class': 'fnt_k09'})
		if k09 != None:
			pof = k09.text
		else:
			pof = ''

		# k05 = k09.find_next_sibling()
		k05 = dd.find('span', {'class': 'fnt_k05'})
		
		if k05 != None:
			en = k05.text
		else:
			en = ''

		f07 = dl_e2.find('span', {'class': 'fnt_e07 _ttsText'})

		if f07 != None:
			example = f07.text
		else:
			example = ''
		en, pof, example
		w['ko'] = en
		w['pof_ko'] = pof
		w['example_ko'] = example
		new_words.append(w)
		save_words(new_words, fieldnames)
	
	return new_words

def ant_and_syn(words, tr, headers):
	new_words = list()
	for w in words:
		print(w['word'])
		break


def crawl_etym(words,tr, headers):
	new_words = list()
	for w in words:
		print(w['word'])
		try:
			result = tr.get('https://en.wiktionary.org/wiki/%s' % w['word'].replace(' ', '_'), headers=headers)
			s = BeautifulSoup(result.text, 'lxml')
			etym = s.find('span', id='Etymology')
			print(etym.findParent().fetchNextSiblings()[0].text)
			w['etym'] = etym.findParent().fetchNextSiblings()[0].text
			new_words.append(w)
			save_words(new_words, fieldnames)
		except:
			new_words.append(w)
			save_words(new_words, fieldnames)
	
	return new_words


def crawl_pron(words, tr, headers):
	new_words = list()
	for w in words:
		print(w['word'])
		try:
			result = tr.get('https://www.lexico.com/en/definition/%s' % w['word'].replace(' ', BLANK), headers=headers)
			time.sleep(1)
			s = BeautifulSoup(result.text, 'lxml')
			pron = s.find('span', {'class': 'phoneticspelling'})
			print(pron.text)

			w['pron'] = pron.text
			new_words.append(w)
			save_words(new_words, fieldnames)
		except:
			new_words.append(w)
			save_words(new_words, fieldnames)

	return new_words


headers = {'User-Agent': random.choice(browsers)}
tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)

# words = crawl_ko(words, tr, headers)
# words = crawl_en(words, tr, headers)
# words = ant_and_syn(words, tr, headers)
# words = crawl_etym(words, tr, headers)
# words = crawl_pron(words, tr, headers)

