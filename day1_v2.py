# -*- coding: utf-8 -*-
# @Author: Tran Bach, VU Anh Tuan
# @Date:   2018-09-20 17:30:16
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-20 17:44:58

"""Day 1
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Can you do this in one pass?
"""

input_array = [10, 15, 3, 0, 7]
k = 10
print('input array: ' + str(input_array))
print('k = ' + str(k))

def doesExist(input_array, k): # O(n)
	d = dict()
	for x in input_array:
		if (k-x) in d:
			return True
		d[x] = 1
	return False

print(doesExist(input_array, k))