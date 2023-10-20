#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

fasta_dict = {}

with open(fasta_file,'r') as fa:
	for line in fa:
		line = line.rstrip()
		found = re.search(r'^>(\S+)\s?(.*)', line)
		if found:
			gene_name = found.group(1)
			fasta_dict[gene_name] = ''
		else:
			fasta_dict[gene_name] += line

for gene_name in fasta_dict:
	seq = fasta_dict[gene_name]
	rev_seq = seq[::-1].lower()
	rc_seq = rev_seq.replace('t','A').replace('c','G').replace('g','C').replace('a','T')
	frame_1_codons = re.findall(r'[ATGC]{3}+', seq)
	print(f'{gene_name}-frame1-codons')
	for codon in frame_1_codons:
		print(codon, end=' ')
	print('\n')
	print(f'{gene_name}-frame2-codons')
	seq_2 = seq[1:]
	frame_2_codons = re.findall(r'[ATGC]{3}+', seq_2)
	for codon in frame_2_codons:
			print(codon, end=' ')
	print('\n')
	print(f'{gene_name}-frame3-codons')
	seq_3 = seq_2[1:]
	frame_3_codons = re.findall(r'[ATGC]{3}+', seq_3)
	for codon in frame_3_codons:
			print(codon, end=' ')
	print('\n')
	frame_4_codons = re.findall(r'[ATGC]{3}+', rc_seq)
	print(f'{gene_name}-frame4-codons')
	for codon in frame_4_codons:
		print(codon, end=' ')
	print('\n')
	print(f'{gene_name}-frame5-codons')
	rc_seq_2 = rc_seq[1:]
	frame_5_codons = re.findall(r'[ATGC]{3}+', rc_seq_2)
	for codon in frame_5_codons:
			print(codon, end=' ')
	print('\n')
	print(f'{gene_name}-frame6-codons')
	rc_seq_3 = rc_seq_2[1:]
	frame_6_codons = re.findall(r'[ATGC]{3}+', rc_seq_3)
	for codon in frame_6_codons:
			print(codon, end=' ')
	print('\n\n')
