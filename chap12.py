#Name: Michael Krieger

#Ex 12.4

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
	d = {}
	for line in open(filename):
		word = line.strip().lower()
		t = signature(word)

		if t not in d:
			d[t] = [word]
		else:
			d[t].append(word)
	return d

def print_anagram_sets_in_order(d):
	#make a list of (length, word pairs)
	t = []
	for v in d.values():
		if len(v) > 1:
			t.append((len(v), v))

	t.sort()

	for x in t:
		print x

def filter_length(d, n):
	res = {}
	for word, anagrams in d.iteritems():
		if len(word) == n:
			res[word] = anagrams
	return res

if __name__ == '__main__':
	d = all_anagrams('words.txt')
	print_anagram_sets_in_order(d)

	eight_letters = filter_length(d, 8)
	print_anagram_sets_in_order(eight_letters)