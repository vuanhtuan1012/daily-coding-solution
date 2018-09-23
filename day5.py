# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-22 12:58:29
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-23 18:53:05

"""
This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def func(a, b):
		return a
	return pair(func)

def cdr(pair):
	def func(a, b):
		return b
	return pair(func)

def main():
	pair = cons(3, 4)
	print(car(pair))
	print(cdr(pair))

if __name__ == '__main__':
	main()