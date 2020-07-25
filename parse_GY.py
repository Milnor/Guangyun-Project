#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

def parse_volume(vol):
	#for i in range(1, last + 1):
		#key = tag +	str(i).zfill(2) # e.g. sp01 .. sp26
	rhyme_count = 0
	voice_count = 0
	word_count = 0
	#print("===rhyme group {}:{}===".format(i, key))
	#current_rhyme = vol.find(key)
	for rhyme in vol:
	#for rhyme in vol.findall(key):
		rhyme_count = rhyme_count + 1
		print("==========rhyme group {}============".format(rhyme_count))
		for vp in rhyme.findall('voice_part'):
			voice_count = voice_count + 1
			#print("\txiaoyun {}".format(vp.attrib))
			# line above gives IPA/onyomi of homophone group
			words = vp.findall('word_head')
			word_list = ""
			for character in words:
				word_count = word_count + 1
				word_list += character.text
			print("\t{}".format(word_list))
	#print("final rhyme count = {}".format(rhyme_count))
	#print("final voice count = {}".format(voice_count))
	#print("final word count = {}".format(word_count))
	return rhyme_count, voice_count, word_count	

def stats(r, h, c, string):
	print("{} totals:".format(string))
	print("\trhyme groups = {}".format(r))
	print("\thomophone groups = {}".format(h))
	print("\tcharacters = {}".format(c))

def main():

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
	sping_rhymes = sping1.findall('rhyme')	# 28 rhyme groups in Shang Ping
	r1,h1,c1 = parse_volume(sping_rhymes) 	

	rhyme_groups += r1
	homophone_groups += h1
	characters += c1


	xping_rhymes = xping2.findall('rhyme')	# 29 rhyme groups in Xia Piang
	r2,h2,c2 = parse_volume(xping_rhymes) 

	rhyme_groups += r2
	homophone_groups += h2
	characters += c2

	shang_rhymes = shang3.findall('rhyme')	# 55 rhyme groups in Shang
	r3,h3,c3 = parse_volume(shang_rhymes)

	rhyme_groups += r3
	homophone_groups += h3
	characters += c3

	qu_rhymes = qu4.findall('rhyme') 		# 60 rhyme groups in Qu
	r4,h4,c4 = parse_volume(qu_rhymes)

	rhyme_groups += r4
	homophone_groups += h4
	characters += c4

	ru_rhymes = ru5.findall('rhyme')		# 34 rhyme groups in Ru
	r5, h5, c5 = parse_volume(ru_rhymes)

	rhyme_groups += r5
	homophone_groups += h5
	characters += c5

	stats(r1, h1, c1, "Shang Ping")
	stats(r2, h2, c2, "Xia Ping")
	stats(r3, h3, c3, "Shang")
	stats(r4, h4, c4, "Qu")
	stats(r5, h5, c5, "Ru")
	stats(rhyme_groups, homophone_groups, characters, "GUANG YUN")

	sys.exit("stop here for now")

if __name__ == "__main__":
	main()
