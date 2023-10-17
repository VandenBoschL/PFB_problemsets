#!/usr/bin/env python3

import sys

input_number = sys.argv[1]
new_number = float(input_number)

print(f"We are testing the qualities of the number {input_number}")

if new_number > 0 :
	print("Positive")
	if new_number > 50 :
		print("Greater than 50")
		if new_number % 3 == 0 :
			print("It is larger than 50 and divisible by 3")
	elif new_number < 50 :
		print("Less than 50")
		if new_number % 2 == 0:
			print("It is an even number that is smaller than 50")
	else:
		print("It's 50")
elif new_number < 0 :
	print("Negative")
elif new_number == 0 :
	print("Number is zero")

