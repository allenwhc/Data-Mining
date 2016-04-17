from collections import Counter
from Tree import DecisionTree
from Test import Test
import math, bisect, operator

precision=4
class Process(object):
	def __init__(self, data, attributes):
		self.input_data=data
		self.attributes=attributes
		self.class_v=['yes','no']
		# self.poker_hand=['Nothing in hand','One pair','Two pairs','Three of a kind',\
		# 				'Straight','Flush','Full house','Four of a kind','Straight flush','Royal flush']
		self.I=[]
	
	def constructTree(self):	
		D=self.parseText(self.input_data)# parse data
		#for j in xrange(len(map(list,zip(*D))[-1])): map(list,zip(*D))[-1][j]=self.poker_hand[int(map(list,zip(*D))[-1][j])]
		
		occurrence=[Counter(l) for l in map(list,zip(*D))] 	#count occurrence by attribute
		attribute_list={i:[v for v in occurrence[i].keys()] for i in xrange(len(occurrence))}	# Census all distinct partitions

		entropy_D=self.computeEntropy(Counter(map(list,zip(*D))[-1]), len(D))	# Compute class entropy
		self.I=self.computeInformationGain(D, occurrence, entropy_D, attribute_list)	# Get information gain
		tree=DecisionTree()
		root=tree.root
		A={self.attributes[i]:[v for v in occurrence[i].keys()] for i in xrange(len(occurrence))}
		tree.construct(A,D,self.attributes,self.I)
		return tree.root

	def computeInformationGain(self, D ,occurrence, entropy_D, attribute_list):
		d={}
		for i in xrange(len(occurrence)-1):
			partition=sorted(D,key=lambda x: x[i])
			# Get partitioned attributes A, and class D
			partitioned_A,partitioned_D,partition_entropy_A=map(list,zip(*partition))[i],map(list,zip(*partition))[-1],[]
			I=sorted([bisect.bisect_left(partitioned_A,v) for v in attribute_list[i]])
			I.append(len(D))
			partition_entropy_A=round(sum([(float((I[j+1]-I[j]))/float(len(D))*self.computeEntropy(Counter(partitioned_D[I[j]:I[j+1]]),I[j+1]-I[j])) for j in xrange(len(I)-1)]),precision)
			d[self.attributes[i]]=round(entropy_D-partition_entropy_A,precision)
		return sorted(d.items(), key=operator.itemgetter(1), reverse=True)

	def computeEntropy(self, attribute, total_entry):
		return round(-sum([float(v)/float(total_entry)*math.log(float(v)/float(total_entry),2) for v in attribute.values()]),precision)

	def parseText(self, data):
		return [line.split(',') for line in data.read().splitlines()]
		# D=map(list,zip(*D))
		# if len(D)==len(self.attributes):
		# 	for j in xrange(len(D[-1])): D[-1][j]=self.poker_hand[int(D[-1][j])]

		# print len(D),len(self.attributes)
		# for i in xrange(len(D)-1):
		# 	if not i%2:
		# 		for j in xrange(len(D[i])):
		# 			if D[i][j]=='1': D[i][j]='hearts'
		# 			elif D[i][j]=='2': D[i][j]='spades'
		# 			elif D[i][j]=='3': D[i][j]='diamonds'
		# 			else: D[i][j]='clubs'
		# 	else:
		# 		for j in xrange(len(D[i])):
		# 			if D[i][j]=='1': D[i][j]='A'
		# 			elif D[i][j]=='11': D[i][j]='J'
		# 			elif D[i][j]=='12': D[i][j]='Q'
		# 			elif D[i][j]=='13': D[i][j]='K'
		# return map(list,zip(*D))

	def testOutcome(self,test_data,root):
		# Rearrange test data by information gain
		def testDataPreConfig(test_data):
			labels=[self.attributes[i] for i in xrange(len(test_data))]
			revised_data=[(test_data[i],labels[i]) for i in xrange(len(labels))]
			order=sorted(map(list,zip(*self.I))[0],key=lambda x: map(list,zip(*self.I))[0].index(x))
			return map(list,zip(*sorted(revised_data, key=lambda x: order.index(x[1]))))[0]
		def dfs(root, test_data):
			node=root
			for A in test_data:
				node=node.children[A]
				for x in self.class_v:
					if x in node.children.keys(): return x
 				if not node: return "Invalid input data"
		test_data=testDataPreConfig(test_data)
		node=root
		return dfs(node,test_data)

class Main(Process):
	def __init__(self, data, attributes, test_data):
		super(Main, self).__init__(data, attributes)
		self.test_data=test_data

	def main(self):
		root=super(Main, self).constructTree()
		t=Test()
		t.outputDecisionTree(root)
		TD=super(Main, self).parseText(self.test_data)
		test_result=[super(Main, self).testOutcome(x,root) for x in TD]
		t.outputTestOutcome(TD,test_result)

t=open('../data/input_data.txt','r')
t_d=open('../data/test_data.txt','r')
#a=['Suit1','Rank1','Suit2','Rank2','Suit3','Rank3','Suit4','Hand4','Suit5','Hand5','Type']
a=['Outlook','Temperature','Humidity','Wind','PlayTennis']
Main(t,a,t_d).main()