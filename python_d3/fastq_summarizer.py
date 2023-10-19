#!/usr/bin/env python3

import sys

fastq_file = sys.argv[1]

line_count = 0
character_count = 0

with open(fastq_file, 'r') as fq:
	for line in fq:
		line_count += 1
		tmp_char_count = len(line)
		character_count += tmp_char_count

average_characters = character_count / line_count

print(f'''{line_count} lines
{character_count} characters
{average_characters} average line length''')
