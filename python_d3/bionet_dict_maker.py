#!/usr/bin/env python3

import sys
import re

## Usage: Input bionet resource file (1), and a fasta of interest (2)

file_path = sys.argv[1]
fasta_path = sys.argv[2]

# Generate dictionaries for the Bionet data
# cut_dict will hold the initial cut sites associated with enzyme names
# restriction_dict will pair the "uncut" sequence with the cut site replacements
# The IUPAC dict is necessary for RegExing the recognition sites that are not absolute


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

# Open bionet, strip the 10 line header
# Pull remaining lines, split by large white space (not tabs)
# Put info direct into cut_dict

with open(file_path, 'r') as bionet_file:
	line_num = 1
	for line in bionet_file:
		if line_num <= 10:
			line_num += 1
		elif line_num > 10: 
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

# Read in fasta, make dict
# This could also just be a pandas dataframe
with open(fasta_path,'r') as fa:
	for line in fa:
		line=line.rstrip()
		found_header = re.search(r'^>(\S+)\s?(.*)', line)
		if found_header:
			header = found_header.group(1)
			fasta_dict[header] = ''
		else:
			fasta_dict[header] += line




# for gene in dict, make cuts to sequence using the restriction_dict
# The elements asked for could be saved to objects for later use
	# But presently, that's not needed, so just print out the information
# Comment out larger print statements once you prove they work because they take up a lot of space

for gene in fasta_dict:
	sequence = fasta_dict[gene]
	for enzyme in cut_dict:
		cutsite = cut_dict[enzyme]
		site = cutsite.replace('^','')
		for code in IUPAC_dict:
			site = site.replace(code, IUPAC_dict[code])
		primed_seq = sequence.replace(site, restriction_dict[site])
		#print(f'cut sequence:\n{primed_seq}\n')# write seq with cut sites
		diced = primed_seq.split('^') # split the sequence
		frag_num = len(diced)
		frag_lengths = [len(x) for x in diced]
		total_len = sum(frag_lengths)
		print(f'Cutting with enzyme: {enzyme} on sequence:{gene}') # For Bonus Question
		print(f'There are {frag_num} fragments') # number of fragments for 10 and Bonus
		print(f'The average length of fragment is {total_len / frag_num}')
		print(f'The largest fragment is {max(frag_lengths)}bp and the smallest is {min(frag_lengths)}bp') # Bonus Question 
		print(f'These are the fragments: {diced}\n') # print fragments as they originally appeared
		print(f'These are the fragments in gel order:{sorted(diced, key=len, reverse=True)}')
		print('\n\n')


