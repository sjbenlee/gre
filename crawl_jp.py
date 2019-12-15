from torrequest import TorRequest
from constants import BLANK, browsers, fieldnames
from bs4 import BeautifulSoup

import random
import csv
import time

def save_words(rows, keys):
    with open('gre2020-jp.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def try_crawl_jp(word, tr, headers):
    try:
        return crawl_jp(word, tr, headers)
    except:
        return [], [], [] 
        

def crawl_jp(word, tr, headers):
    example_jp = list()
    syn_jp = list()
    jp = list()
    result = tr.get('https://jisho.org/search/%s' % word.replace(' ', BLANK), headers=headers)
    s = BeautifulSoup(result.text, 'lxml')
    exact_block = s.find('div', {'class': 'exact_block'})
    divs = exact_block.findAll('div', {'class': ['concept_light', 'clearfix']})
    print(len(divs), 'divs found')
    for i, div in enumerate(divs):
        jp_wrapper = div.find('div', {'class': 'concept_light-representation'})
        furigana = jp_wrapper.find('span', {'class': 'furigana'})
        jp_text = jp_wrapper.find('span', {'class': 'text'})
        meaning_wrappers = div.findAll('div', {'class': 'meaning-wrapper'})
        print(i, len(meaning_wrappers))
        for meaning_wrapper in meaning_wrappers:
            meaning_meaning = meaning_wrapper.find('span', {'class': 'meaning-meaning'})
            meanings = meaning_meaning.text.split(';')
            meanings = [m.strip() for m in meanings]
            if word in meanings:
                jp.append('%s/%s' % (jp_text.text.strip(), furigana.text.strip()))
                for m in meanings:
                    if m != word:
                        syn_jp.append(m.strip())

            for m in meanings:
                if word in m and word != m:
                    example_jp.append(m.strip())
    return jp, syn_jp, example_jp

keys = list()
rows = list()
with open('gre2020-20191215-trimmed.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

keys = list(rows[0].keys())
keys.extend(['jp', 'syn_jp', 'example_jp'])

start = time.time()
tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)

for row in rows:
    print('now crawling for word:', row['word']) 
    headers = { 'User-Agent': random.choice(browsers) }
    jp, syn_jp, example_jp = try_crawl_jp(row['word'], tr, headers)
    row['jp'] = '；'.join(jp)
    row['syn_jp'] = ', '.join(syn_jp)
    row['example_jp'] = ', '.join(example_jp)
    print(row['jp'])
    print(row['syn_jp'])
    print(row['example_jp'])
    print('now saving for word:', row['word'])
    save_words(rows, keys)

end = time.time()
print('crawling completed.')
print('time elapsed:', end - start, 'seconds.')
