#!/usr/bin/env python3.6


import os
import sys


try:
	from datatransfer import datalib
except ImportError:
	print("BTSOOT Server can try to load missing dependency. This requires an internet connection.")
	if input("Should i try? (y/N) ") == "y":
		os.system("git clone https://git.paukra.com/open-source/datatransfer.git")
	else:
		print("Abort. Install manually or restart the program.")
		exit()


def split(string, splitters): #MAY RESOLVE ALL PROBLEMS WITH CSV
	final = [string]
	for x in splitters:
		for i,s in enumerate(final):
			if x in s and x != s:
				left, right = s.split(x, 1)
				final[i] = left
				final.insert(i+1, x)
				final.insert(i+2, right)
	return final


def main():
    print("THIS SOFTWARE SERVERS NO PURPOSE ANYMORE.")
	print("BTSOOT SERVER")
	while 1: #ENTERING MAIN LOOP FOR CONTINUOS USAGE
		print(":: Waiting for incoming connection...")
		datalib.receive("transmit.list")
		print(":: Received transmitfile.")
		with open("transmit.list", "r") as scan:
			files = scan.readlines()
			for file in files:
				cutting_newline = file.strip('\n')
				splitted_line = split(cutting_newline[0], ",")
				if len(splitted_line) != 3:
					if not os.path.exists(splitted_line[0]):
						os.makedirs("/home/paul/btsoot/backup" + splitted_line[0])
				else:
					if splitted_line[2] == "error":
						pass
					elif splitted_line[2] == "permission_denied":
						pass
					else:
						filepath = split(splitted_line, "/")
						filepathlengh = len(filename)
						filename = filepath[filepathlengh]
						print(f"Creating file with name: {filename}")
						datalib.receive("/home/paul/btsoot/backup" + filepath)
		os.system("rm transmit.list")



if __name__ == "__main__":
	main()
