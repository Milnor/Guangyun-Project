#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import sys

def parse_volume(vol, tag, last):
	for i in range(1, last + 1):
		key = tag +	str(i).zfill(2) # e.g. sp01 .. sp26
		print("===rhyme group {}===".format(i))
		for rhyme in vol:
			for vp in rhyme.findall('voice_part'):
				print("\txiaoyun {}".format(vp.attrib))
				# line above gives IPA/onyomi of homophone group
				words = vp.findall('word_head')
				word_list = ""
				for character in words:
					word_list += character.text
				print("\t{}".format(word_list))
				
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


	# Run each individual volume through parser
	r1 = sping1.findall('rhyme')	# 28 rhyme groups in Shang Ping
	parse_volume(r1, "sp", 2) 		# TODO: set 2 to 28
	
	r2 = xping2.findall('rhyme')	# 29 rhyme groups in Xia Piang
	parse_volume(r2, "xp", 2) 		# TODO: set 2 to 29

	r3 = shang3.findall('rhyme')	# 55 rhyme groups in Shang
	parse_volume(r3, "s", 2) 		# TODO: set 2 to 55

	r4 = qu4.findall('rhyme') 		# 60 rhyme groups in Qu
	parse_volume(r4, "q", 2) 		# TODO: set 2 to 60

	r5 = ru5.findall('rhyme')		# 34 rhyme groups in Ru
	parse_volume(r5, "r", 2)		# TODO: set 2 to 34

	sys.exit("stop here for now")

if __name__ == "__main__":
	main()
