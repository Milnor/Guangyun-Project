#!/usr/bin/env python3

import sys

verbose = False
debug = ""


def add_candidates(zi, c_list, variants):

	data = variants.read()
	lines = data.split()

	for line in lines:
		characters = line.split(",")
		first = characters[0]
		second = characters[1]

		if zi == first:
			c_list.append(second)
		elif zi == second:
			c_list.append(first)

# Repeat search with variants/allographs
def slow_search(zi, shujuku):
	
	global verbose
	global debug

	sCandidates = []		# kSemanticVariants
	zCandidates = []		# zVariants

	if verbose:
		debug += "[!] Attempting slow search on {}".format(zi) + "\n"

	with open("data/s_variants.csv", 'r', encoding='utf-8') as sfile:
		add_candidates(zi, sCandidates, sfile)

	with open("data/z_variants.csv", 'r', encoding='utf-8') as zfile:
		add_candidates(zi, zCandidates, zfile)

	if verbose:
		debug += "\tsVariants: {}\n".format(sCandidates)
		debug += "\tzVariants: {}\n".format(zCandidates)

	return "*"				# Not Found

def ping_ze(zi, shujuku):

	isPing = False
	isZe = False

	if zi in shujuku[1]:	# Shang Ping
		isPing = True
	elif zi in shujuku[2]:	# Xia Ping
		isPing = True
	elif zi in shujuku[3]:	# Shang
		isZe = True			
	elif zi in shujuku[4]: 	# Qu
		isZe = True
	elif zi in shujuku[5]:	# Ru
		isZe = True

	if isPing and not isZe:
		return "平"			# Ping
	elif not isPing and isZe:
		return "仄"			# Ze
	elif isPing and isZe:
		return "?"			# Could be either
	else:
		return slow_search(zi, shujuku) # Try Harder

def main():

	global verbose
	global debug

	# Open our Guang Yun database
	gy = open("data/sbgy.txt", "r")

	# Read it into a string
	data = gy.read()

	'''
	findme = "世"
	if findme in data:
		print("found {}!".format(findme))
	else:
		print("failed to find {}...".format(findme))
	'''

	volumes = data.split("---VOL---")
	# volumes[0] = (blank)

	# TODO: make this a command line argument
	poem = open("test_inputs/libai.txt", "r")
	#poem = open("test_inputs/dufu.txt", "r")	

	# TODO: make this a command line argument
	verbose = True

	i = 0
	for line in poem:
		i += 1
		tones = ""
		for char in line.strip():
			tones += ping_ze(char, volumes)
		print("{} \t{} \t{}".format(str(i).zfill(4), line.strip(), tones))

	if verbose:
		print("\nDebug info\n----------\n{}".format(debug))

	gy.close()
	poem.close()
	
	sys.exit()

if __name__ == "__main__":
	main()
