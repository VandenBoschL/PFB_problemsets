#!/usr/bin/env python3

num = 1

#while num < 101:
#	print(num)
#	num+=1

nums_list = [101,2,15,22,95,33,2,27,72,15,52]

#for num in nums_list:
#	if num % 2 == 0:
#		print(num)
#	else:
#		continue

sorted_nums_list = sorted(nums_list)
#print(sorted_nums_list)
evens = 0
odds = 0

for num in sorted_nums_list:
#	print(num)
	if num % 2 == 0:
		evens += num
	else:
		odds += num

#print(f"Sum of even numbers: {evens}")
#print(f"Sum of odd numbers: {odds}")

# Write a script to loop through a new list
#Print each element
#Print length and sequence
#tab sep

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

pos=1
for seq in seqs:
#	print(f'{pos}\t{len(seq)}\t{seq}')
	pos += 1

# List Comprehension

complex_list = [(len(seq), seq) for seq in seqs]

print(complex_list)

