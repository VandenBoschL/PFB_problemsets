#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}


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

peptide_dict = {}
for gene_name in fasta_dict:
	peptide_list = []
	seq = fasta_dict[gene_name]
	rev_seq = seq[::-1].lower()
	rc_seq = rev_seq.replace('t','A').replace('c','G').replace('g','C').replace('a','T')
	frame_1_codons = re.findall(r'[ATGC]{3}+', seq)
	frame_1_translation = []
	for codon in frame_1_codons:
		amino_acid = translation_table[codon]
		frame_1_translation.append(amino_acid)
	frame_1_protein = ''.join(frame_1_translation)
	#print(frame_1_protein)
	peptide_list.append(frame_1_protein)
	#rf_2
	seq_2 = seq[1:]
	frame_2_codons = re.findall(r'[ATGC]{3}+', seq_2)
	frame_2_translation = []
	for codon in frame_2_codons:
		amino_acid = translation_table[codon]
		frame_2_translation.append(amino_acid)
	frame_2_protein = ''.join(frame_2_translation)
	peptide_list.append(frame_2_protein)
	# rf 3
	seq_3 = seq_2[1:]
	frame_3_translation = []
	frame_3_codons = re.findall(r'[ATGC]{3}+', seq_3)
	frame_3_translation = []
	for codon in frame_3_codons:
		amino_acid = translation_table[codon]
		frame_3_translation.append(amino_acid)
	frame_3_protein = ''.join(frame_3_translation)
	peptide_list.append(frame_3_protein)
	# rf 4
	frame_4_codons = re.findall(r'[ATGC]{3}+', rc_seq)
	frame_4_translation = []
	for codon in frame_4_codons:
		amino_acid = translation_table[codon]
		frame_4_translation.append(amino_acid)
	frame_4_protein = ''.join(frame_4_translation)
	peptide_list.append(frame_4_protein)
	# rf 5
	rc_seq_2 = rc_seq[1:]
	frame_5_codons = re.findall(r'[ATGC]{3}+', rc_seq_2)
	frame_5_translation = []
	for codon in frame_5_codons:
		amino_acid = translation_table[codon]
		frame_5_translation.append(amino_acid)
	frame_5_protein = ''.join(frame_5_translation)
	peptide_list.append(frame_5_protein)
	# rf 6
	rc_seq_3 = rc_seq_2[1:]
	frame_6_codons = re.findall(r'[ATGC]{3}+', rc_seq_3)
	frame_6_translation = []
	for codon in frame_6_codons:
		amino_acid = translation_table[codon]
		frame_6_translation.append(amino_acid)
	frame_6_protein = ''.join(frame_6_translation)
	peptide_list.append(frame_6_protein)
	peptide_dict[gene_name] = peptide_list
#	print(peptide_list)
	print('/n/n')


print(peptide_dict)
