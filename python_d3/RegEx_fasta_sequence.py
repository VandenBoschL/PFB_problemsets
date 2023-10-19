#!/usr/bin/env python3

import sys
import re

file_path = sys.argv[1]
restriction = '(A|G)ATT(C|T)'
cut = r'\1^ATT\2'

seq_dict = {}

with open(file_path, 'r') as fa:
	for line in fa:
		line = line.strip()
		found = re.search(r'^>(\S+)\s?(.*)', line)
		if found:
			header = found
			seq_dict[header] = ''
			identity = found.group(1)
			desc = found.group(2)
			print(f'id:{identity} desc:{desc}')
		else:
			seq_dict[header] += line


cuttable_dict = {}
for gene in seq_dict:
	cuttable_dict[gene] = re.sub(restriction, cut, seq_dict[header])

print(seq_dict)
print(cuttable_dict)


