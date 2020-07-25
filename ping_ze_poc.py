#!/usr/bin/env python3

import sys

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
		return "* "			# Not Found

def main():

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
	#poem = open("test_inputs/libai.txt", "r")
	poem = open("test_inputs/dufu.txt", "r")	

	i = 0
	for line in poem:
		i += 1
		tones = ""
		for char in line.strip():
			tones += ping_ze(char, volumes)
		print("{} \t{} \t{}".format(str(i).zfill(4), line.strip(), tones))

	gy.close()
	poem.close()
	
	sys.exit()

if __name__ == "__main__":
	main()
