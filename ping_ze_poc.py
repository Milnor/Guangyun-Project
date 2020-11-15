#!/usr/bin/env python3

import sys
from cihai.core import Cihai

verbose = False
debug = ""
c_dict = Cihai()

def codepoints2chars(codepoints):
	if codepoints is None:
		return None
	results = []
	temp = codepoints.split()
	for each in temp:
		num = each[2:]
		#print("num={}".format(num))
		# The [0] is to strip dictionary (e.g. Matthews) name if there is one
		results.append(f'\\u{num}'.encode().decode('unicode_escape')[0])

	return results

def slow_search(zi, shujuku):

	global verbose
	global debug
	global c_dict

	# See cihai.git-pull.com/api.html
	query = c_dict.unihan.lookup_char(zi)
	glyph = query.first()
	alternates = glyph.kZVariant
	kz_vars = codepoints2chars(alternates)
	# which of these also matter?
	sem_vars = codepoints2chars(glyph.kSemanticVariant)
	spec_vars = codepoints2chars(glyph.kSpecializedSemanticVariant) 

	if verbose:
		debug += "[!] Attempting slow search on {}".format(zi) + "\n"
		debug += "\tkZVariants = {}\n".format(kz_vars)
		debug += "\tkSemanticVariants = {}\n".format(sem_vars)
		debug += "\tkSpecializedSemanticVariants = {}\n".format(spec_vars)

	# It is a nuisance to combine lists when some may be none
	variants = []
	for each in (kz_vars, sem_vars, spec_vars):
		if each is not None:
			variants.extend(each)
	# Remove duplicates
	variants = list(dict.fromkeys(variants))

	if variants is None:
		if verbose:
			debug += "\t[-] Slow search failed.\n"
		return '*'			# Not Found
	else:
		isPing = False
		isZe = False

		for each in variants:
			if each in shujuku[1]:		# Shang Ping
				if verbose:
					debug += "\t[+] Slow search found {}!\n".format(each)
				isPing = True
			elif each in shujuku[2]:	# Xia Ping
				if verbose:
					debug += "\t[+] Slow search found {}!\n".format(each)
				isPing = True
			elif each in shujuku[3]:	# Shang
				if verbose:
					debug += "\t[+] Slow search found {}!\n".format(each)
				isZe = True			
			elif each in shujuku[4]: 	# Qu
				if verbose:
					debug += "\t[+] Slow search found {}!\n".format(each)
				isZe = True
			elif each in shujuku[5]:	# Ru
				if verbose:
					debug += "\t[+] Slow search found {}!\n".format(each)
				isZe = True

		if isPing and not isZe:
			return "平"			# Ping
		elif not isPing and isZe:
			return "仄"			# Ze
		elif isPing and isZe:
			return "?"			# Could be either
		else:
			if verbose:
				debug += "\t[-] Slow search failed.\n"
			return '*'			# Not Found

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
	global c_dict

	# Parse command line arguments
	if len(sys.argv) < 2:
		print("Usage: {} poem.txt [-v]\n".format(sys.argv[0]))
		sys.exit()

	input_file = sys.argv[1]
	if len(sys.argv) > 2:
		if sys.argv[2] == "-v":
			verbose = True

	# Install Unihan if needed
	if not c_dict.unihan.is_bootstrapped:
		c.unihan.bootstrap()

	c_dict.unihan.add_plugin(
		'cihai.data.unihan.dataset.UnihanVariants', namespace='variants'
	)	# See cihai.git-pull.com/examples.html


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

	poem = open(input_file, "r")

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
