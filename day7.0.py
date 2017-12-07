with open("day7.txt", "r") as fin:
	data = fin.read().split('\n')

class Node:
	def __init__(self, value, children):
		self.value = value
		self.children = children
		self.indegree = 0

nodes = {}

for l in data:
	name = l.split(' ')[0]
	value = int(l.split('(')[1].split(')')[0])
	children = []
	if len(l.split('->')) > 1:
		children = l.split('->')[1].replace(' ', '').split(',')
	nodes[name] = Node(value, children)

for node in nodes.values():
	for ch in node.children:
		nodes[ch].indegree += 1

for key in nodes:
	if nodes[key].indegree == 0:
		print key
