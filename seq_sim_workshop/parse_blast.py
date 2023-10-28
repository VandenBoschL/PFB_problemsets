#!/usr/bin/env python3

import sys
import re

def dict_maker(line, dictionary, Big_Key):
	line_list = line.split('\t')
	percid = float(line_list[2])
	alen = int(line_list[3])
	evalue = float(line_list[10])
	sm_key = line_list[0]
	if Big_Key in dictionary:
		if sm_key in dictionary[Big_Key]:
			dictionary[Big_Key][sm_key]['percid'].append(percid)
			dictionary[Big_Key][sm_key]['alen'].append(alen)
			dictionary[Big_Key][sm_key]['evalue'].append(evalue)
		else:
			dictionary[Big_Key][sm_key] = {'percid':[], 'alen':[], 'evalue':[]}
			dictionary[Big_Key][sm_key]['percid'].append(percid)
			dictionary[Big_Key][sm_key]['alen'].append(alen)
			dictionary[Big_Key][sm_key]['evalue'].append(evalue)
	else:
		dictionary[Big_Key]={}
	return dictionary			

files_in = sys.argv[1:]

field_names = ['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits']

hits_dict = {}
for file in files_in:
	with open(file, 'r') as a_file:
		searchID = re.search(r'qfo_(\w+\d{2})\.txt', file)
		Matrix = searchID.group(1)
		for line in a_file:
			line = line.rstrip()
			if line.startswith('#'):
				continue
			dict_maker(line, hits_dict, Matrix)	

for matrix in hits_dict:
	all_the_percid = []
	all_the_alen = []
	all_the_eval = []
	for query in hits_dict[matrix]:
		all_the_percid += hits_dict[matrix][query]['percid']
		all_the_alen += hits_dict[matrix][query]['alen']
		all_the_eval += hits_dict[matrix][query]['evalue']
	all_the_percid.sort()
	all_the_alen.sort()
	all_the_eval.sort()
	percid_median_i = int(len(all_the_percid) / 2)
	alen_median_i = int(len(all_the_alen) / 2)
	eval_median_i = int(len(all_the_eval) / 2)
	print(f'Matrix: {matrix}')
	print(f' % ID\tALen\tE-Value')
	print(f'{all_the_percid[percid_median_i]}\t{all_the_alen[alen_median_i]}\t{all_the_eval[eval_median_i]}')
	

