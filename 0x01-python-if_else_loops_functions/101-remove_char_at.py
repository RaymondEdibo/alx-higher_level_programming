#!/usr/bin/python3
def remove_char_at(str, n):
	n = ""
	k = 0
	l = len(str)
	if n < 0 or l < n:
		return str
	else:
		while l > k:
			if n == k:
				k += 1
				continue
			n += str[k]
			k += 1
		return n
