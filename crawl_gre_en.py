from torrequest import TorRequest
import random
from bs4 import BeautifulSoup
from Word import Word
from constants import BLANK, browsers
import csv

tr = TorRequest(proxy_port=9050, ctrl_port=9051, password=None)


def save_words(words, fieldnames):
    with open('gre2020-en.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in words:
            writer.writerow(row)



headers = {'User-Agent': random.choice(browsers)}

fieldnames = []
with open('gre2020.csv') as f:
    for i, line in enumerate(f):
        if i == 0:
            fieldnames = line.split(',')

fieldnames = [f.strip() for f in fieldnames]
fieldnames.append('pof')
fieldnames.append('en')
fieldnames.append('example')


print('filednames:', fieldnames)

words = list()
with open('gre2020.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        words.append(row)

new_words = list()

for w in words:
    print(w['word'])
    try:
        re = tr.get("https://endic.naver.com/search.nhn?sLn=en&query=%s&searchOption=all&isOnlyViewEE=Y" % w['word'].replace(' ', BLANK), headers=headers)
        s = BeautifulSoup(re.text, 'lxml')
        
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
    except:
        pass


