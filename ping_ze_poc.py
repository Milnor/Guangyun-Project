#!/usr/bin/env python3

import sys

def ping_ze(zi, shujuku):
	if zi in shujuku[1]:
		return "-"			# Shang Ping
	elif zi in shujuku[2]:
		return "-"			# Xia Ping
	else:
		return "~"			# Shang, Qu, or Ru

def main():

	# Open our Guang Yun database
	gy = open("data/sbgy.txt", "r")

	# Read it into a string
	data = gy.read()

	volumes = data.split("---VOL---")
	#print("There are {} volumes".format(len(volumes)))
	#print(volumes[5])
	# volumes[0] = (blank)
	# volumes[1] = ping1 // dong
	# volumes[2] = ping1 // xian
	# volumes[3] = shang // chong?
	# volumes[4] = qu // song	
	# volumes[5] = ru // wu 

	# TODO: make this acommand line argument
	poem = open("test_inputs/libai.txt", "r")

	i = 0
	for line in poem:
		print("{} = {}".format(i, line))
		i += 1
		for char in line.strip():
			print("\t{} ({})".format(char, ping_ze(char, volumes)))

	gy.close()
	poem.close()
	
	sys.exit()

if __name__ == "__main__":
	main()
