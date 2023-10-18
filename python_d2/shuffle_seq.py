#!/usr/bin/env python3
import random

seq = 'ACTCAGCGAGTTACTAGTGTA'
seq_list = list(seq)
max_index = len(seq) - 1
print(seq)
for i in range(len(seq_list)):
	posA = random.randrange(max_index)
	posB = random.randrange(max_index)
	nt_A = seq_list[posA]
	nt_B = seq_list[posB]
	seq_list[posA] = nt_B
	seq_list[posB] = nt_A

shuf_seq = ''.join(seq_list)

print(shuf_seq)
