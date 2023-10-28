#!/usr/bin/env python3

import sys
import subprocess
import gzip

dbSNP_file = sys.argv[1]

# General concept: From the dbSNP database, pull vcf info from a list of snps
	# Massage the data: pull columns of interest, convert refseq chromosome accessions
sub_vcf = f"bcftools view -i'ID=@{snpid_list}' {dbSNP_file}"
#Run this through subprocess and figure out how you want to handle the output.
	# Write to new vcf and then re-read that back in I guess


# For item in vcf:
	# create dictionary
		# position
		# ref
		# alt

# For snp in vcf dictionary:
	# bedtools slop position to ~20-40 bp
	# convert position to sequence (bedtools)
	# begin printing fastas
	# pair printing a wt seq with a snp
	# for snp, check if seq[pos] = ref
		# substitute ref for var
		# if var contains commas:
			# split var by comma
			# for var in vars:
				# write wt seq with name
				# substitute ref for var
				# write var sequence with name (same as wt)
