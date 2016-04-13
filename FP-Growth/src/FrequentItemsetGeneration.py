from collections import defaultdict
class ConditionalTreeNode(object):
	def __init__(self):
		self.leaf=False
		self.val=''
		self.count=0
		self.children=defaultdict(ConditionalTreeNode)

class Process(object):
	def __init__(self, root, minSup):
		self.root=root
		self.minSup=minSup
		self.P=[]
		self.Q=[]

	# @ param root: FPTreeNode
	# @ param minSup: int
	# @ return: List
	def Generation(self, root, minSup):
		pass

	def search(self, path):
		node=self.root
		for item in path:
			if item not in node.children: return False
			node=node.children[item]
		return True if node.leaf else False

class FPGrowth(Process):
	def __init__(self, root, minSup):
		super(FPGrowth, self).__init__(root, minSup)

	def getConditionalFPTree(self):
		super(FPGrowth, self).Generation(self.root, self.minSup)

