

from Bio import SeqIO
import sys
import re
import pandas as pd

### Usage ###
# python3 better_BC_finder.py barcodes_table.txt output_table.txt
# I am lazy so I'm hard coding the fastq paths into the code for now. 
# Yes, I can make this work later to input them into the command line usage.
# I don't have the data or time to test it right now so there will be bugs

barcodes_table = sys.argv[1]
output_table - sys.argv[2]

# Function to count the barcodes and output a dictionary that matches the original counts dict
def BC_counts(path, counts_dict):
	for record in SeqIO.parse(path, 'r'):
		read = str(record.seq)
		# Find BC by adjacent seq
		# Edit adjacent seq as needed
		# Edit BC RegEx as needed
		findBC = re.search(r'ggcagagggaaaaagatc(([AT][GC]){9})', read)
		if findBC:
			BC = findBC.group(1)
		if BC in counts_dict:
			counts_dict[BC]['count'] += 1
	return counts_dict

# Building counts dict framework
Barcodes_dict_count = {}
with open(barcodes_table, 'r') as bc:
	for line in bc:
		line = line.rstrip
		(Barcode, ID) = line.split()
		Barcodes_dict_count[Barcode]['ID'] = ID
		Barcodes_dict_count[Barcode]['count'] = 0

# This is where you hard code your paths to fastqs
counts_1 = BC_counts('path/to/file.fastq', Barcodes_dict_count)
counts_2 = BC_counts('path/to/file.fastq', Barcodes_dict_count)
counts_3 = BC_counts('path/to/file.fastq', Barcodes_dict_count)
counts_4 = BC_counts('path/to/file.fastq', Barcodes_dict_count)		

# There's a better way to do this but for now:
Summary_dict = {}
For BC in Barcodes_dict_count:
	Summary_dict[BC]['ID'] = Barcodes_dict_count[BC]['ID']
	Total_counts = counts_1[BC]['count'] + counts_2[BC]['count'] + counts_3[BC]['count'] + counts_4[BC]['count']
	Summary_dict[BC]['count'] = Total_counts

# I'm not sure if this will work to make a valid dataframe
out_counts = pd.DataFrame(Summary_dict)
out_counts.to_csv(output_table, sep='\t', index=False)
