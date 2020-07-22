#!/usr/bin/env python3

from xml.dom import minidom
import xml.etree.ElementTree as ET
import sys

def main():
	'''
	gy = minidom.parse('data/sbgy.xml')
	#items = gy.getElementsByTagName('volume_title')
	items = gy.getElementsByTagName('volume')
	print("volume_title:\n")
	for each in items:
		print(each)

	sys.exit()
	'''
	'''
	volume id="v1"	// v1 = shangping1 , v2 = xiaping2, v3 = shang3
		volume_title
		catalog
			rhythmic_entry
				fanqie
		rhyme id="sp01"	// xp05, 
			voice_part ipa="..." onyomi="..."
				word_head id="...."

	'''


	tree = ET.parse('data/sbgy.xml')
	root = tree.getroot()

	print("00={}".format(root[0][0].text))	

	print("01={}".format(root[0][1].text))	
	#print("10={}".format(root[1][0].text))	
	#print("11={}".format(root[1][1].text))	
	
	#for volumes in root.iter('volume'):
	#	print("v={}".format(volumes))

	volumes = root.findall('volume')
	print("v0={}".format(volumes[0].attrib))

	sping1 = volumes[0]

	rhymes = sping1.findall('rhyme')
	for rhyme in rhymes:
		vp = rhyme.findall('voice_part')
		for v in vp:
			head = v.findall('word_head')
			#print("head word: {}".format(head))
			for w in head:
				print("w={}".format(w.text))

	sys.exit("done")

	# rhyme id "sp01" == first rhyme group in shang ping
	#	... sp28 is the last rhyme group in that volume

	# word_head's within the same voice_part tags
	#	belong to the same xiaoyun 'homophone group'	

	for each in rhymes:
		#print("rhyme: ", each.attrib)
		head_words = each.findall('word_head')
		print("head words: ", head_words)
	sys.exit("stop here.")

	xping2 = volumes[1]
	shang = volumes[2]
	qu = volumes[3]
	ru = volumes[4]

	print(sping1.text, sping1.attrib)

	for child in sping1:
		print(child.text, child.attrib)
		for subitem in child:
			print(subitem.text, subitem.attrib)
			#words = subitem.findall('word_head')
			#print("words={}".format(words))


	

	sys.exit("pause...")

	#print(root.tag)
	for child in root:
		print(child.tag, child.attrib)
		#print(dir(child))


	


	sys.exit("pause here for now")

	for elem in root:
		for subelem in elem:
			print(subelem.text)

	

if __name__ == "__main__":
	main()
