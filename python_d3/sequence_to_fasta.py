#!/usr/bin/env python3

import sys

sequence_file = sys.argv[1]


seq_dict = {}
with open(sequence_file, "r") as seq_read:
	for line in seq_read:
		line = line.strip()
		gene_name,seq = line.split()
		seq_dict[gene_name] = seq

#print(seq_dict['test'])

nt_dict = {'A':'t', 'T':'a', 'G':'c', 'C':'g', 'N':'N'}

rc_seq_dict = {}

for gene in seq_dict:
	seq = seq_dict[gene]
	seq = seq[::-1]
	for nt in seq:
		seq = seq.replace(nt, nt_dict[nt])
	rc_seq_dict[gene] = seq.upper()

for gene in rc_seq_dict:
	print(f'{gene}\t{rc_seq_dict[gene]}')

