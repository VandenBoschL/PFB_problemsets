#!/usr/bin/env python3

import sys

fa_file = sys.argv[1]

fasta_dict = {}


with open(fa_file, 'r') as fa:
	for line in fa:
		line = line.strip()
		if line.startswith('>'):
			seq = ''
			fasta_dict[line] = ''
			header = line
		else:
			fasta_dict[header] += line

print(fasta_dict)
