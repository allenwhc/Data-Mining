from collections import defaultdict
class TreeNode(object):
	def __init__(self):
		#self.val=x
		self.count=0
		self.leaf=False
		self.children=defaultdict(TreeNode)

class Cubing(object):
	def __init__(self, table):
		self.root=TreeNode()
		self.entry=[x.split(',') for x in map(list,zip(*table))[0]]
		self.count=map(list,zip(*table))[1]

	def starCubing(self):
		for entry in self.entry:
			self.insert(entry)
		return self.root

	def insert(self, root_to_leaf):
		node=self.root
		for c in root_to_leaf:
			node=node.children[c]
		node.leaf=True
