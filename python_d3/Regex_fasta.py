#!/usr/bin/env python3

import sys
import re

file_path = sys.argv[1]

with open(file_path, 'r') as fa:
	for line in fa:
		line = line.strip()
		found = re.search(r'^>(\S+)\s?(.*)', line)
		if found:
			identity = found.group(1)
			desc = found.group(2)
			print(f'id:{identity} desc:{desc}')
