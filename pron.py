import csv
from bs4 import BeautifulSoup
import time
from torrequest import TorRequest
import random
from constants import BLANK, browsers

tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)


headers = {'User-Agent': random.choice(browsers)}





words = list()
with open('gre2020-temp.csv') as f:
	reader = csv.DictReader(f)
	for row in reader:
		words.append(row)


def save_words(words):
	fieldnames = ['word', 'ko', 'zh_Hans', 'etym_zh_Hans', 'pron', 'ant', 'syn']
	with open('gre2020-temp.csv', 'w') as f:
		writer = csv.DictWriter(f, fieldnames)
		writer.writeheader()
		for data in words:
			writer.writerow(data)

failed = list()
for i, r in enumerate(words):
	print(i/len(words) * 100 ,'%')
	if 'pron' in r and r['pron'] != '':
		print(r['pron'], 'is already')
	if 'pron' in r and r['pron'] == '':
		try:
			result = tr.get('https://www.lexico.com/en/definition/%s' % r['word'].replace(' ', BLANK), headers=headers)
			
			time.sleep(1)
			s = BeautifulSoup(result.text, 'lxml')
			pron = s.find('span', {'class': 'phoneticspelling'})
			print(pron.text)

			r['pron'] = pron.text

			save_words(words)
		except:
			failed.append(r['word'])
			with open('pron_failed2.csv', 'w') as f:
				f.write('\n'.join(failed))

	if 'pron' not in r:
		try:

			headers = {'User-Agent': random.choice(browsers)}
			driver.get('https://www.lexico.com/en/')
			s = BeautifulSoup(driver.page_source, 'lxml')
			pron = s.find('span', {'class': 'phoneticspelling'})
			print(pron.text)
			r['pron'] = pron.text
			save_words(words)
		except:
			failed.append(r['word'])
			with open('pron_failed2.csv', 'w') as f:
				f.write('\n'.join(failed))


	# if 'etym' not in r:
	# 	driver.get('https://en.wiktionary.org/wiki/Wiktionary:Main_Page')
	# 	i = driver.find_element_by_name('search')
	# 	i.send_keys(r['word'])
	# 	i.send_keys(Keys.RETURN)

	# 	alternative_forms = driver.find_element_by_id('Alternative_forms')
	# 	etymology = driver.find_element_by_id('Etymology')


		# break

