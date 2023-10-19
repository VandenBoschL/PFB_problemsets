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
	counts_dict = {'G':0, 'C':0, 'T':0, 'A':0}
	seq = seq_dict[gene]
	seq = seq[::-1]
	for nt in seq:
		counts_dict[nt] +=1
		seq = seq.replace(nt, nt_dict[nt])
	rc_seq_dict[gene] = seq.upper()
	GC_count = counts_dict['G'] + counts_dict['C']
	GC_percent = GC_count / len(seq) * 100
	print(f'{gene} nt counts: {counts_dict}')
	print(f'{gene} GC content is {GC_percent}%')




#for gene in rc_seq_dict:
	#print(f'{gene}\t{rc_seq_dict[gene]}')



