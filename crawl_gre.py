from torrequest import TorRequest
import random
from bs4 import BeautifulSoup
from Word import Word
from constants import BLANK, browsers


tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)



headers = {'User-Agent': random.choice(browsers)}






words = list()
with open('gre.csv') as f:
	for l in f:
		words.append(Word(l.strip()))


for w in words:
	print(w.word)
	re_ko = tr.get("https://endic.naver.com/search.nhn?sLn=en&searchOption=all&query=%s" % w.word.replace(' ', BLANK), headers=headers)
	s_ko = BeautifulSoup(re_ko.text, 'lxml')
	dl = s_ko.findAll('dl', {'class': 'list_e2'})
	print(dl)

	break
