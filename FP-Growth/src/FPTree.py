from collections import defaultdict, Counter, OrderedDict
from operator import itemgetter

class FPTreeNode(object):
	def __init__(self):
		self.leaf=False
		self.val=''
		self.count=0
		self.children=defaultdict(FPTreeNode)
		self.next=None

class Process(object):
	def __init__(self, dataset):
		self.root=FPTreeNode()
		self.dataset=dataset
		self.support=dict()
		self.nodes=defaultdict(FPTreeNode)

	def preConstructionConfig(self):
		self.support=dict(Counter(x for entry in self.dataset for x in entry).items())
		return [sorted(entry, key=lambda x: self.support[x], reverse=True) for entry in self.dataset]

	def FPTreeConstruction(self, data_entry):
		node=self.root
		for item in data_entry:
			node=node.children[item]
			node.val=item
			node.count+=1
		node.leaf=True

	def constructLinkedList(self, root):
		for k,v in root.children.items():
			#print lv, k
			if k in self.nodes:
				self.nodes[k].next=v
			self.nodes[k]=v
			self.constructLinkedList(v)

class FPTree(Process):
	def __init__(self, dataset):
		super(FPTree, self).__init__(dataset)

	def getReorganizedData(self):
		return super(FPTree, self).preConstructionConfig()

	def getItemSupport(self):
		return self.support

	def getFPTree(self, dataset):
		for entry in dataset:
			super(FPTree, self).FPTreeConstruction(entry)
		super(FPTree, self).constructLinkedList(self.root)
		return self.root

		