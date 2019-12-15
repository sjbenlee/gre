class Word:
	def __init__(self, word):
		self.word = word
		self.syn = ''
		self.ant = ''
		self.ko = ''
		self.zh = ''
		self.en = ''
		self.etym_zh = ''
		self.pron_uk = ''
		self.pron_us = ''

	def set_syn(self, syn):
		self.syn = syn

	def set_ant(self, ant):
		self.ant = ant

	def set_ko(self, ko):
		self.ko = ko

	def set_zh(self, zh):
		self.zh = zh

	def set_en(self, en):
		self.en = en

	def set_etym_zh(self, etym_zh):
		self.etym_zh = etym_zh

	def set_pron_uk(self, pron_uk):
		self.pron_uk = pron_uk

	def set_pron_us(self, pron_us):
		self.pron_us = pron_us



words = list()
with open('gre.csv') as f:
	for l in f:
		words.append(Word(l.strip()))