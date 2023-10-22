#!/usr/bin/env python3

import sys
from Bio import SeqIO
import re

fasta_path = sys.argv[1]

def fa_parser(file_path):
	output_dict = {}
	for seq_record in SeqIO.parse(file_path, 'fasta'):
		gene_name = seq_record.id
		gene_description = seq_record.description
		raw_sequence = str(seq_record.seq)
		sequence = re.sub('\n', '', raw_sequence)
		output_dict[gene_name] = {'description':gene_description, 'sequence':sequence}
	return output_dict

def get_GC(seq):
	GC_count = seq.count('G') + seq.count('C')
	GC_percent = GC_count / len(seq)
	return GC_percent

Fasta_dict = fa_parser(fasta_path)
nt_count = 0
fa_lens = []
gc_vals = []
for gene_name in Fasta_dict:
	tmp_len = len(Fasta_dict[gene_name]['sequence'])
	tmp_gc = get_GC(Fasta_dict[gene_name]['sequence'])
	nt_count += tmp_len
	fa_lens.append(tmp_len)
	gc_vals.append(tmp_gc)


avg_gc = sum(gc_vals) / len(gc_vals)


print('sequence count:', len(Fasta_dict))
print('total number of nucleotides:', nt_count)
print(f'avg len: {nt_count/len(Fasta_dict)}')
print('shortest len:', min(fa_lens))
print('longest len:', max(fa_lens))
print('average GC content:', avg_gc)
print('lowest GC content:', min(gc_vals))
print('highest GC content:', max(gc_vals))
 
