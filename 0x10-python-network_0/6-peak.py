#!/usr/bin/python3
""" it has a function that find peak number """


def find_peak(list_of_integers):
	""" Find the number highest of a array """
	if not list_of_integers:
		return None

	num = 0
	for elem in list_of_integers:
		if elem > num:
			num = elem
	return num
