#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
	l = len(argv)
	if l != 1:
		print("{} arguments:".format(l - 1))
		for i in range(1, l):
			print("{}: {}".format(i, argv[i]))
	else:
		print("0 arguments.")
