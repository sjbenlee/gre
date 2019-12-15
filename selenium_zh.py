from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from constants import BLANK
import time

driver = webdriver.Chrome()

words = list()
with open('gre.csv') as f:
	for line in f:
		words.append(line.strip())

zh = list()

failed = list()
succeed = list()

for i, w in enumerate(words):
	print(i, i/len(words), w)
	driver.get("https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%B9%81%E4%BD%93/")
	i = driver.find_element_by_id("searchword")
	i.send_keys(w)
	i.send_keys(Keys.RETURN)
	time.sleep(1.0)
	s = BeautifulSoup(driver.page_source, 'lxml')
	try:
	# title = s.find('div', {'class': 'di-title'})
	# wordspan = s.find('span', {'class': ['headword', 'hdb', 'tw-bw', 'dhw', 'dpos-h_hw']})
		titlespan = s.find('span', {'class': ['hw', 'dhw']})
		span_uk = s.find('span', {'class': ['uk', 'dpron-i']})
		span_us = s.find('span', {'class': ['us', 'dpron-i']})
		pron_uk = span_uk.find('span', {'class': ['ipa', 'dipa', 'lpr-2', 'lpl-1']})
		pron_us = span_us.find('span', {'class': ['ipa', 'dipa', 'lpr-2', 'lpl-1']})
		def_div = s.find('div', {'class': ['def-body', 'ddef_b']})
		def_zh = def_div.find('span', {'class': ['trans', 'dtrans', 'dtrans-se']})
		def_en = s.find('div', {'class':['def', 'ddef_d', 'db']})

		succeed.append(titlespan.text)
		print(titlespan.text, def_zh.text)
		with open('zh-succeed.csv', 'w') as f:
			f.write('\n'.join(succeed))

		zh.append('%s/:/%s/:/%s/:/%s/:/%s' % (titlespan.text, def_zh.text, def_en.text, pron_us, pron_uk))
		with open('zh.csv', 'w') as f:
			f.write('\n'.join(zh))

	except:
		failed.append(w)
		with open('zh-failed.csv', 'w') as f:
			f.write('\n'.join(failed))
		print(w, 'is failed')
