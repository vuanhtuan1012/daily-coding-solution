# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2018-09-20 13:13:32
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2018-09-21 02:50:57
# @Reference: https://medium.com/@dimko1/serialize-and-deserialize-binary-tree-e9811ead85ed

"""Day 3
This problem was asked by Google.
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def serialize(node): # DFS
	vals = list()
	def encode(node):
		if node is not None:
			vals.append(node.val)
			encode(node.left)
			encode(node.right)
		else:
			vals.append('#')
	
	encode(node)
	return ' '.join(vals)

def deserialize(data):
	def decode(vals):
		v = next(vals)
		if v == '#':
			return None
		node = Node(v)
		node.left = decode(vals)
		node.right = decode(vals)
		return node
	
	vals = iter(data.split())
	return decode(vals)

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)).left.left.val == 'left.left')