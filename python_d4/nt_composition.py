#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

fasta_dict = {}

with open(fasta_file, 'r') as fa:
	for line in fa:
		line = line.rstrip()
		found = re.search(r'^>(\S+)\s?(.*)', line)
		if found:
			header = found.group(1)
			fasta_dict[header] = {'seq':''}
		else:
			fasta_dict[header]['seq'] += line


for gene in fasta_dict:
	for nt in fasta_dict[gene]['seq']:
		if nt not in fasta_dict[gene]:
			fasta_dict[gene][nt] = 1
		else:
			fasta_dict[gene][nt] +=1


print(fasta_dict)
