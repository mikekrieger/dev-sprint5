#Name: Michael Krieger

#Ex 13.8

import sys
import string
import random

suffix_map = {}
prefix = ()

def process_file(filename, order=2):
	fp = open(filename)
	skip_utenberg(fp)

	for line in fp:
		for word in line.rstrip().split():
			process_word(word, order)

def skip_gutenberg_header(fp):
	for line in fp:
		if line.startswith('*END*THE SMALL PRINT!'):
			break

def process_word(word, order=2):
	global prefix
	if len(prefix) < order:
		prefix += (word,)
		return

	try:
		suffix_map[prefix].append(word)
	except KeyError:
		# if there is no entry for this prefix, make one suffix_map[prefix] = [word]

	prefix = shift(prefix, word)

def random_text(n=100):
	for i in range(n):
		suffixes = suffix_map.get(start, None)
		if suffixes == None:
			random_text(n-i)
			return

	word = random.choice(suffixes)
	print word,
	start = shift(start, word)

def shirt(t, word):
	