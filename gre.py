import random
import sys


words = list()
if len(sys.argv) > 1:
	f_name = sys.argv[1]
	with open(f_name) as f:
		for line in f:
			words.append(line.strip())
else:
	with open('gre.csv') as f:
		for line in f:
			words.append(line.strip())

print('Total num:', len(words))
s = random.sample(words, 10)
for ss in s:
	print(ss)