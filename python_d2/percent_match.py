#!/usr/bin/env python3

#From an alignment, calculate match


seq1 = 'ATCG----ATCTGATAGCTACTACTGTCAATATACTATATAGCGACGAG---'
seq2 = 'ATCGATGCATCTGATAGATACTACTCTCA--ATACTATATAGCGACGAGCGA'

Seq_range = len(seq1)

num_matches = 0

for i in range(Seq_range):
	i-=1
	if seq1[i] == seq2[i]:
		num_matches += 1

Percent_identity = num_matches / Seq_range * 100

print(f"Sequence Identity: {num_matches}//{Seq_range} ({Percent_identity}%)")



