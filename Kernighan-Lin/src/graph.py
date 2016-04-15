from collections import defaultdict,Counter
import random
class Gragh(object):
	def __init__(self,G,V):
		self.G=G
		self.V=V

	def adjacentList(self):
		G=defaultdict(list)
		for e1,e2,w in self.G:
			G[e1].append((e2,w))
			G[e2].append((e1,w))
		return G

	def biPartition(self):
		A=['e', 'a', 'c']
		B=[x for x in self.V if x not in A]
		return [A,B]

class Getgraph(Gragh):
	def __init__(self,G,V):
		super(Getgraph, self).__init__(G,V)

	def getG(self):
		return super(Getgraph, self).adjacentList()

	def getBipartitionedGraph(self):
		return super(Getgraph,self).biPartition()