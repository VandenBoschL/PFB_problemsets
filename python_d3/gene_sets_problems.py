#!/usr/bin/env python3

gene_set = set()
with open('alpaca_all_genes.tsv', 'r') as genes:
	for line in genes:
		gene_set.add(line.rstrip())

with open('alpaca_stemcellproliferation_genes.tsv', 'r') as genes:
	sc_prolif_set = set()
	line_num = 1
	for line in genes:
		if line_num == 1:
			line_num += 1
			continue
		else:
			sc_prolif_set.add(line.strip())

with open('alpaca_pigmentation_genes.tsv', 'r') as genes:
	pigmentation_set = set()
	for line in genes:
			pigmentation_set.add(line.strip())

with open('alpaca_transcriptionfactors.tsv', 'r') as genes:
	TF_set = set()
	for line in genes:
			TF_set.add(line.strip())

#Find all genes not cell prolif
#print(gene_set - sc_prolif_set)
print(len(gene_set))
print(len(sc_prolif_set))
print(len(gene_set - sc_prolif_set))

# Find all genes both sc prolif and pigment
both_subsets = sc_prolif_set & pigmentation_set
print(len(both_subsets))
print(both_subsets)
print(sc_prolif_set)
