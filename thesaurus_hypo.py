import csv
from bs4 import BeautifulSoup
import time
from torrequest import TorRequest
import random
from constants import BLANK, browsers

tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)


headers = {'User-Agent': random.choice(browsers)}



words = list()

with open('gre2020-thesaurus-hypo.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		words.append(row)


def save_words(words):
	fieldnames = ['word', 'ko', 'zh_Hans', 'etym_zh_Hans', 'pron', 'ant', 'syn', 'etym', 'hypo', 'hyper', 'var']
	with open('gre2020-thesaurus-hypo.csv', 'w') as f:
		writer = csv.DictWriter(f, fieldnames)
		writer.writeheader()
		for data in words:
			writer.writerow(data)

failed = list()
for i, r in enumerate(words):
	# ants = r['ant'].split(',')
	# ants = [a.strip() for a in ants]
	print(r['word'], i/len(words) * 100 ,'%')


	
	# syns = r[''].split(',')
	# syns = [s.strip() for s in syns]
	# break
	# before = len(ants)

	hypos = list()
	try:
		result = tr.get('https://en.wiktionary.org/wiki/Thesaurus:%s' % r['word'].replace(' ', '_'), headers=headers)#% r['word'].replace(' ', '_'), headers=headers)
		s = BeautifulSoup(result.text, 'lxml')
		hypo = s.find('span', id='Hyponyms')
		ls = hypo.findParent().fetchNextSiblings()[0].findAll('li')
		for l in ls:
			hypos.append(l.text)

		# after = len(ants)

		# print(after - before, 'words added.')

		r['hypo'] = ', '.join(hypos)
		print(hypos)
		save_words(words)
	# break

	except Exception as e:
		print(e)
		print(r['word'])
		# failed.append(r['word'])
		# with open('pron_failed3.csv', 'w') as f:
		# 	f.write('\n'.join(failed))

	# r['etym'] = etym.findParent().fetchNextSiblings()[0].text

	# save_words(words)
		# except:
		# 	failed.append(r['word'])
		# 	with open('pron_failed3.csv', 'w') as f:
		# 		f.write('\n'.join(failed))

	# if 'etym' not in r:
	# 	driver.get('https://en.wiktionary.org/wiki/Wiktionary:Main_Page')
	# 	i = driver.find_element_by_name('search')
	# 	i.send_keys(r['word'])
	# 	i.send_keys(Keys.RETURN)

	# 	alternative_forms = driver.find_element_by_id('Alternative_forms')
	# 	etymology = driver.find_element_by_id('Etymology')


		# break

