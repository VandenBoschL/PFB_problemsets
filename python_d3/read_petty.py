#!/usr/bin/env python3

import sys

lyrics = sys.argv[1]
lyrics_output = sys.argv[2]


with open(lyrics, 'r') as lyrics_file, open(lyrics_output, 'w') as fo:
	for line in lyrics_file:
		line = line.strip().upper()
		fo.write(f'{line}\n')


