
words = list()

with open('gre.csv') as f:
	for line in f:
		words.append(line.strip())

words = list(set(words))

with open('gre_no_duplicate.csv', 'w') as f:
	f.write('\n'.join(words))