from bs4 import BeautifulSoup
from Word import Word
from constants import BLANK, browsers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


# headers = {'User-Agent': random.choice(browsers)}

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)


words = list()
with open('gre2020.csv') as f:
	for l in f:
		words.append(Word(l.strip()))

for w in words:
	print(w.word)
	driver.get("https://endic.naver.com/search.nhn?sLn=en&query=%s&searchOption=all&isOnlyViewEE=Y" % w.word.replace(' ', BLANK))
	s = BeautifulSoup(driver.page_source, 'lxml')

	# part_of_speech = s.find('span', {'data-type': 'ore', 'data-lang': 'en'})
	content_div = s.find('div', {'id': 'content'})
	dl_e2 = content_div.find('dl', {'class': 'list_e2'})
	dd = dl_e2.find('dd')
	k09 = dd.find('span', {'class': 'fnt_k09'})
	# k05 = k09.find_next_sibling()
	# m = dd.find('m')  
	# print(part_of_speech)
	# print(len(m.children))
	# for child in m.children:
	# 	print(child)
	# part_of_speech = k09.find('span')
	# print(part_of_speech.text)
	print(dd)
	break
