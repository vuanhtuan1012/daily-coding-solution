# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-18 13:34:15
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-20 11:13:08

# Day 1
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Can you do this in one pass?

input_array = [10, 15, 3, 0, 7]
k = 10
print('input array: ' + str(input_array))
print('k = ' + str(k))

def doesExist(search_array, k): # O(len(search_array)^2)
	for i in search_array:
		if (k-i) in search_array: # O(n)
			return (True, i, k-i)
	return (False, None, None)

input_array.sort() # sort input array O(nlogn)
search_array = [i for i in input_array if i <= k] # get search_array
print(doesExist(search_array, k))