#!/usr/bin/env python3

import logging
import xml.etree.ElementTree as ET
import sys

class RhymeDictionary:
	myvar = 0
	
	def __init__(self, dataPath, debug=False):
		logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
		#if debug:
		#	logging.setLevel(logging.DEBUG)
		logging.debug(f'[!] Building a RhymeDictionary from {dataPath}')

def parse_volume(vol, output):

	rhyme_count = 0
	voice_count = 0
	word_count = 0

	#output.write("---VOL---\r\n")

	for rhyme in vol:
		rhyme_count = rhyme_count + 1
		embed()
		for vp in rhyme.findall('voice_part'):
			voice_count = voice_count + 1
			words = vp.findall('word_head')
			word_list = ""
			for character in words:
				word_count = word_count + 1
				word_list += character.text
			output.write(word_list + "\r\n")	
		output.write("\r\n")	# Extra space after rhyme group
	
	return rhyme_count, voice_count, word_count	

def stats(r, h, c, string):

	print("\n{} totals:".format(string))
	print("\trhyme groups = {}".format(r))
	print("\thomophone groups = {}".format(h))
	print("\tcharacters = {}".format(c))

def main():

	fail = RhymeDictionary('test.xml')
	gy = RhymeDictionary('data/sbgy.xml', True)
	sys.exit()

	# Read in the XML tree
	tree = ET.parse('data/sbgy.xml')
	root = tree.getroot()

	# Store each volume: Shang Ping, Xia Ping, Shang, Qu, and Ru
	volumes = root.findall('volume')
	sping1 = volumes[0]
	xping2 = volumes[1]
	shang3 = volumes[2]
	qu4 = volumes[3]
	ru5 = volumes[4]

	# Variables for total stats
	rhyme_groups = 0				# Yun
	homophone_groups = 0			# Xiaoyun
	characters = 0					# Zi

	# Run each individual volume through parser
	# TODO: refactor, has excessive redundant code

	# 28 rhyme groups expect in Shang Ping
	sping_rhymes = sping1.findall('rhyme')	
	r1,h1,c1 = parse_volume(sping_rhymes, f) 	

	rhyme_groups += r1
	homophone_groups += h1
	characters += c1

	# 29 rhyme groups expected in Xia Ping
	xping_rhymes = xping2.findall('rhyme')	
	r2,h2,c2 = parse_volume(xping_rhymes, f) 

	rhyme_groups += r2
	homophone_groups += h2
	characters += c2

	# 55 rhyme groups expected in Shang
	shang_rhymes = shang3.findall('rhyme')	
	r3,h3,c3 = parse_volume(shang_rhymes, f)

	rhyme_groups += r3
	homophone_groups += h3
	characters += c3

	# 60 rhyme groups expected in Qu
	qu_rhymes = qu4.findall('rhyme') 	
	r4,h4,c4 = parse_volume(qu_rhymes, f)

	rhyme_groups += r4
	homophone_groups += h4
	characters += c4

	# 34 rhyme groups expected in Ru
	ru_rhymes = ru5.findall('rhyme')	
	r5, h5, c5 = parse_volume(ru_rhymes, f)

	rhyme_groups += r5
	homophone_groups += h5
	characters += c5

	# Display per volume and overall totals
	stats(r1, h1, c1, "Shang Ping")
	stats(r2, h2, c2, "Xia Ping")
	stats(r3, h3, c3, "Shang")
	stats(r4, h4, c4, "Qu")
	stats(r5, h5, c5, "Ru")
	stats(rhyme_groups, homophone_groups, characters, "GUANG YUN")

	sys.exit()

if __name__ == "__main__":
	main()
