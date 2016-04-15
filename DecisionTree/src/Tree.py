from collections import defaultdict, Counter
from operator import itemgetter
class DecisionTreeNode(object):
	def __init__(self):
		self.leaf=False
		self.label=''
		self.lv=0
		self.children=defaultdict(DecisionTreeNode)

class DecisionTree(object):
	def __init__(self):
		self.root=DecisionTreeNode()
		self.root.label='root'

	def construct(self, attribute_list, D, A, I):
		self.insert(self.root, D, A, I, attribute_list, 1)

	def insert(self, node, D, A, I, attribute_list, lv):
		curr_class=Counter(map(list, zip(*D))[-1])
		if len(curr_class)<=1:
			node.leaf=True
			node.label=curr_class.keys()[0]
			node=node.children[curr_class.keys()[0]]
			return
		if not I:
			node.leaf=True
			node.label=max(curr_class.iteritems(),key=itemgetter(1))[0]
			node=node.children[max(curr_class.iteritems(),key=itemgetter(1))[0]]
			return
		splitting_criterion=I[0][0]	# Apply current splitting criterion on node's label
		node.label=splitting_criterion
		column_index=[i for i,a in enumerate(A) if a==splitting_criterion][0]	# Find column index matches current splitting criterion

		# Scan the current attribute listA
		for attribute in attribute_list[splitting_criterion]:
			split_D=[D[i] for i in xrange(len(D)) if not cmp(map(list,zip(*D))[column_index][i],attribute)]
			if split_D:
				node.lv=lv
				self.insert(node.children[attribute],split_D,A,I[1:],attribute_list,lv+1)
			else:
				node=node.children[max(curr_class.iteritems(),key=itemgetter(1))[0]]
				return



