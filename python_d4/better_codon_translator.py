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
# Alter fasta_dict to be a complex dictionary
# fasta_dict[gene_name] = {'seq':''}
# room for later additions
with open(fasta_file,'r') as fa:
  for line in fa:
    line = line.rstrip()
    found = re.search(r'^>(\S+)\s?(.*)', line)
    if found:
      gene_name = found.group(1)
      fasta_dict[gene_name] = ''
    else:
      fasta_dict[gene_name] += line

# Start by writing a function to get codons list
# Add each codon list to fasta_dict as fasta_dict[gene_name][codon_frame1-6][codons] = []
		# consider how much you want to nest this
# Write frames of each to a fasta file
# Write a function to get joined peptide list
# Make list of peptides or add to dictionary
# for peptide list in gene_name:
	# regex (M[A-Z]+\*) using finditer
	# put found objects into a list
	# get longest peptide for each frame
	# write peptide to .aa file (maybe include positions from next step)
	# get position of logest peptide
	# pull positions of longest peptide in codon list
	# join codons to sequence and write to fasta







