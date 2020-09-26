#!/usr/bin/env python3

import sys

# We will keep statistics
semvar = 0
zvar = 0
spoofvar = 0
tradvar = 0
simpvar = 0
specvar = 0
error = 0

def print_global_stats():

	global semvar
	global zvar
	global spoofvar
	global tradvar
	global simpvar
	global specvar
	global error

	print("Processing Statistics:")
	print("======================")
	print("{} kSemanticVariant".format(semvar))
	print("{} kZVariant".format(zvar))
	print("{} kSpoofingVariant".format(spoofvar))
	print("{} kTraditionalVariant".format(tradvar))
	print("{} kSimplifiedVariant".format(simpvar))
	print("{} kSpecializedSemanticVariant".format(specvar))
	print("{} Errors".format(error))

# Input: e.g. U+31347, U+4DB1
# Output: two Hanzi separated by a comma, ending in newline
def text2bytes(one, two):
	return bytes(one, "utf-8") + b',' + bytes(two, "utf-8") + b'\n'

def process_line(data, sem_out, z_out):

	global semvar
	global zvar
	global spoofvar
	global tradvar
	global simpvar
	global specvar
	global error

	parsed = data.split()	# split on whitespace
	# note that last element in line may contain "<kFenn" or sth. similar
	if parsed[1] == "kSemanticVariant":
		semvar += 1
		sem_out.write(text2bytes(parsed[0], parsed[2].split('<')[0]))
	elif parsed[1] == "kZVariant":
		zvar += 1
		z_out.write(text2bytes(parsed[0], parsed[2].split('<')[0]))
	elif parsed[1] == "kSpoofingVariant":
		spoofvar += 1
	elif parsed[1] == "kTraditionalVariant":
		tradvar += 1
	elif parsed[1] == "kSimplifiedVariant":
		simpvar += 1
	elif parsed[1] == "kSpecializedSemanticVariant":
		specvar += 1
	else:
		print("[-] {} unrecognized!".format(parsed[1]))
		error += 1

def main():

	# Open files for input and output
	unihan = open("data/Unihan_Variants.txt", "r")
	s_var = open("data/s_variants.csv", "wb")
	z_var = open("data/z_variants.csv", "wb")

	line_count = 1

	for line in unihan:
		if line[0] == "#":
			# first 21 lines are header comments, last line is EOF
			pass
		elif line[0] == "U":
			# Do not know yet if it is a semantic variant, zVariant,
			#  or something else that we don't care about
			process_line(line, s_var, z_var)
		elif line[0] == '\n':	
			# penultimate line
			pass
		else:
			print("[!] Unexpected input on line {}".format(line_count))

		line_count += 1

	print_global_stats()

	# We are done
	unihan.close()
	s_var.close()
	z_var.close()

if __name__ == "__main__":
	main()
