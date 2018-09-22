# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-21 02:55:50
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-22 12:43:16
# @Reference: https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

"""Day 4
This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

def firstMissingPositive(array):
	p = 0
	n = len(array)

	# find index of the first positive element in array
	while (p < n) and (array[p] <= 0):
		p += 1

	# move all non-positive to the left of the first positive element
	i = p+1
	while (i < n):
		if array[i] <= 0:
			array[p], array[i] = array[i], array[p]
			p += 1
		i += 1

	"""
	In positive subset, mark presence of an element x:
	- use array elements as index
	- change the value at the index x to negative.
	Example
	Index:           p  p+1  p+2  p+3  p+4 (= n-1)
	Array elements:  3   2    5    6    4
	Marked elements: 3  -2   -5    6   -4
	"""
	i = p
	while i < n:
		x = abs(array[i])
		if 1 <= x <= n-p:
			array[p+x-1] *= -1
		i += 1

	# get first missing positive integer
	i = p
	while i < n:
		x = array[i]
		if x > 0:
			return i-p+1
		i += 1
	return i-p+1

def main():
	input_array = [3, 4, -1, 1]
	print("input array: " + str(input_array))
	print("first missing positive integer: %d" % firstMissingPositive(input_array))

if __name__ == '__main__':
	main()