#!/usr/bin/env python3

import sys
import re

fasta_file = sys.argv[1]

def split_codons(seq):
	codons = re.findall(r'[ATGC]{3}', seq)
	return codons

def translate_codons(frame):
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
	translation = []
	for codon in frame:
		amino_acid = translation_table[codon]
		translation.append(amino_acid)
	polypeptide = ''.join(translation)
	return polypeptide



fasta_dict = {}
# Alter fasta_dict to be a complex dictionary
# fasta_dict[gene_name] = {'seq':''}
# room for later additions
with open(fasta_file,'r') as fa:
  for line in fa:
    line = line.rstrip()
    found = re.search(r'^>(\S+)\s?(.*)', line)
    if found:
      gene_name = found.group(1)
      fasta_dict[gene_name] = {'seq':''}
    else:
      fasta_dict[gene_name]['seq'] += line


# Iterate through genes and print codons to fasta_dict[gene_name][frames] = []
for gene_name in fasta_dict:
	seq = fasta_dict[gene_name]['seq']
	rc_seq = seq[::-1].lower().replace('t','A').replace('c','G').replace('g','C').replace('a','T')
	seq_2 = seq[1:]
	seq_3 = seq[2:]
	rc_seq_2 = rc_seq[1:]
	rc_seq_3 = rc_seq[2:]	
	frames = []
	frames.append(split_codons(seq))
	frames.append(split_codons(seq_2))
	frames.append(split_codons(seq_3))
	frames.append(split_codons(rc_seq))
	frames.append(split_codons(rc_seq_2))
	frames.append(split_codons(rc_seq_3))
	fasta_dict[gene_name]['frames'] = frames

# Write frames of each to a fasta file
# Commented out when printing complete
	# I don't feel like taking this in the command line, but I know how

#for gene_name in fasta_dict:
#	pos = 1
#	for frame in fasta_dict[gene_name]['frames']:
#		header = print(f'>{gene_name} frame{pos}')
#		joined_codons = ''.join(frame)
#		print(joined_codons)
#		print('\n')
#		pos +=1	
#	print('\n')


# Make list of peptides or add to dictionary
for gene_name in fasta_dict:
	polypeptides = []
	pos = 1
	for frame in fasta_dict[gene_name]['frames']:
		#print(f'{gene_name} position{pos}')
		translation = translate_codons(frame)
		#print(translation, '\n')
		polypeptides.append(translation)
		pos += 1
	fasta_dict[gene_name]['polypeptides'] = polypeptides


# Find longest peptide
for gene_name in fasta_dict:
	for polypeptide in fasta_dict[gene_name]['polypeptides']:
		pattern = r'M\w+\*'
		proteins = re.findall(pattern, polypeptide)
		protein_lengths = [len(x) for x in proteins]
# This is where the errors start. need to find longest protein per frame

		largest_protein_pos = protein_lengths.index(max())
		print(protein_lengths)

# currentle working on:
# for peptide list in gene_name:
	# regex (M[A-Z]+\*) using finditer
	# put found objects into a list
	# get longest peptide for each frame
	# write peptide to .aa file (maybe include positions from next step)
	# get position of logest peptide
	# pull positions of longest peptide in codon list
	# join codons to sequence and write to fasta







