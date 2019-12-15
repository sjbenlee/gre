words = list()

with open('ko.csv') as f:
	for line in f:
		data = line.split('/:/')
		words.append(data[0].strip())

with open('gre.csv', 'w') as f:
	f.write('\n'.join(words))