# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan, Pham Hong Nhung
# @Date:   2018-09-20 12:09:57
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-20 13:08:21

"""Day 2
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

input_array = [1, 2, 3, 4, 5]
print('input array: ' + str(input_array))

n = len(input_array)
asc = [1]*n; desc = [1]*n

for i in range(n-1): # O(n)
	asc[i+1] = asc[i]*input_array[i]
for i in range(2, n+1): # O(n)
	desc[-i] = desc[-i+1]*input_array[-i+1]

import numpy as np
output_array = np.array(asc)*np.array(desc)
print('output array: ' + str(list(output_array)))