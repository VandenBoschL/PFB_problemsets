#!/usr/bin/env python3

import sys
import re

text_file_path = sys.argv[1]

line_num = 1
with open(text_file_path, 'r') as text_file, open('Alli.txt', 'w') as fo:
	for line in text_file:
		for found in re.finditer(r'Nobody', line):
			print(f'in line {line_num}, match at position: {found.start()}')
		new_line = re.sub(r'Nobody', r'Alli', line)
		fo.write(new_line)
		line_num += 1
