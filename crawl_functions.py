import random
from bs4 import BeautifulSoup
from constants import BLANK, browsers

def crawl_en_pof_example(word, tr):
    headers = {'User-Agent': random.choice(browsers)}
    print('now crawling', word, 'at crawl_example of crawl_functions')
    try:
        re = tr.get("https://endic.naver.com/search.nhn?sLn=en&query=%s&searchOption=all&isOnlyViewEE=Y" % word.replace(' ', BLANK), headers=headers)
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

        if f07 != None:
            example = f07.text
        else:
            example = ''
        return (en, pof, example)
    except:
        return ('', '', '')


def crawl_ko(word, tr):
    headers = {'User-Agent': random.choice(browsers)}
    print('now crawling', word, 'at crawl_ko of crawl_functions')
    try:
        re = tr.get("https://endic.naver.com/search.nhn?sLn=en&isOnlyViewEE=N&query=%s" % word.replace(' ', BLANK), headers=headers)
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

        if f07 != None:
            example = f07.text
        else:
            example = ''
        print(en, pof, example)
        return (en, pof, example)
    except:
        return ('', '', '')
    