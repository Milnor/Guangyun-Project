#!/usr/bin/env python3

import xmltodict

def main():

	# 5 volumes: Shang Ping, Xia Ping, Shang, Qu, Ru
	# Rhymes by Volume: 28, 29, 55, 60, 34

	with open('data/sbgy.xml') as data:

		d = data.read()
		dic = xmltodict.parse(d)
		print("vols={}".format(len(dic['book']['volume'])))
		print("\tShang Ping rhymes={}".format(len(dic['book']['volume'][0]['rhyme'])))
		print("\tXia Ping rhymes={}".format(len(dic['book']['volume'][1]['rhyme'])))
		print("\tShang rhymes={}".format(len(dic['book']['volume'][2]['rhyme'])))
		print("\tQu rhymes={}".format(len(dic['book']['volume'][3]['rhyme'])))
		print("\tRu rhymes={}".format(len(dic['book']['volume'][4]['rhyme'])))

		for vol in dic['book']['volume']:
			print("{}".format(vol['rhyme'][0]['voice_part'][0]['word_head'][0]['#text']))

if __name__ == "__main__":
	main()
