from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from constants import BLANK
import time

driver = webdriver.Chrome()

words = list()
with open('ko-failed.csv') as f:
	for line in f:
		words.append(line.strip())

ko = list()

failed = list()

for i, w in enumerate(words):
	print(i, i/len(words), w)
	driver.get("https://endic.naver.com/?sLn=en")
	i = driver.find_element_by_id("ac_input")
	i.send_keys(w)
	i.send_keys(Keys.RETURN)
	time.sleep(1.0)
	try:
		s = BeautifulSoup(driver.page_source, 'lxml')
		dl = s.find('dl', {'class':'list_e2'})
		dd = dl.find('dd')
		span = dd.find('span', {'class': 'fnt_k05'})
		print(span.text)
		ko.append('%s/:/%s' % (w, span.text))
		time.sleep(1.0)
		with open('ko2-temp.csv', 'w') as f:
			f.write('\n'.join(ko))
	except:
		failed.append(w)
		with open('ko-failed2-temp.csv', 'w') as f:
			f.write('\n'.join(failed))
		print(w, 'is failed')