#!/usr/bin/env python3

import sys
import re
from Bio import SeqIO

contig_file = sys.argv[1]

sequences_lengths = []
for seq_record in SeqIO.parse(contig_file, 'fasta'):
	sequence = seq_record.seq
	length = len(sequence)
	sequences_lengths.append(length)

sequences_lengths.sort(reverse=True)
total_size = sum(sequences_lengths)
print(total_size)
counter=0
length_sum = 0
for length in sequences_lengths:
	if length_sum < (total_size / 2):
		length_sum += length
		counter += 1
	else:
		break
print('counter:', counter)
N50 = sequences_lengths[counter]



print(f'There are {len(sequences_lengths)} contigs')
print(f'The shortest contig is {min(sequences_lengths)} bp long')
print(f'The longest contig is {max(sequences_lengths)} bp long')
print(f'The total contig length is {total_size} bp')
print(f'The N50 is {N50}')
print(f'The L50 is {counter +1}')
