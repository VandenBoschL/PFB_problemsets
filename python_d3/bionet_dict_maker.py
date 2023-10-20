#!/usr/bin/env python3

import sys
import re

file_path = sys.argv[1]
fasta_path = sys.argv[2]

restriction_dict = {}
cut_dict = {}
IUPAC_dict = {'R':'[AG]',
'Y':'[CT]',
'S':'[GC]',
'W':'[AT]',
'K':'[GT]',
'M':'[AC]',
'B':'[CGT]',
'D':'[AGT]',
'H':'[ACT]',
'V':'[ACG]',
'N':'[ACGT]'}


with open(file_path, 'r') as bionet_file:
	line_num = 1
	for line in bionet_file:
		if line_num <= 10:
			line_num += 1
		elif line_num < 30: 
			line_num += 1
			line = line.rstrip()
			enzyme,rec_site = re.split(r" {3,}", line)
			cut_dict[enzyme] = rec_site


# for later identification use, find all ^ characters and replace with ''
	# save to restriction_dict
for enzyme in cut_dict:
	site = cut_dict[enzyme]
	clean_site = site.replace('^','')
	for code in IUPAC_dict:
		clean_site = clean_site.replace(code, IUPAC_dict[code])
	restriction_dict[clean_site] = site


fasta_dict = {}

# read in fasta, make dict
with open(fasta_path,'r') as fa:
	for line in fa:
		line=line.rstrip()
		found_header = re.search(r'^>(\S+)\s?(.*)', line)
		if found_header:
			header = found_header
			fasta_dict[header] = ''
		else:
			fasta_dict[header] += line




# for gene in dict, make cuts to sequence, write to cut_seq_dict
for gene in fasta_dict:
	sequence = fasta_dict[gene]
	for site in restriction_dict:
		primed_seq = sequence.replace(site, restriction_dict[site])
		#print(f'cut sequence:\n{primed_seq}\n')# write seq with cut sites
		diced = primed_seq.split('^') # split the sequence
		print(f'There are {len(diced)}') # number of fragments
		print(f'These are the fragments: {diced}') # print fragments as they originally appeared
		print(f'# print sorted(split_list, key=len, reverse=True)




##### Optional Question
bonus_dict = {}

#with open(user_fasta, 'r') as bonus_seq:
	#for line in bonus_seq:
	#line = line.strip()
#	use some regex to identify sequence id and sequence, write to bonus_dict
#
# nest some for loops here
# outer loop, for enzyme in restriction_dict:
	#for gene in bonus_dict:
	#print(gene)
	#print(enzyme)
	#new_seq = re.sub(restriction_dict[enzyme], cut_dict[enzyme], bonus_dict[gene])
	#digested_seq = new_seq.split('^')
	#print(len(digested_seq))
	#stats_list = [len(x) for x in digested_seq]
	#print(sum(stats_list)/len(stats_list))
	#print(max(stats_list))
	#print(min(stats_list))

# add some fstrings to make it prettier



