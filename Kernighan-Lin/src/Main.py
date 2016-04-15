from collections import defaultdict,Counter
from operator import itemgetter
import random

from KernighanLin import KernighanLin
from graph import Getgraph
class Main(object):
	def main(self,graph):
		V=self.vertex(graph)
		g=Getgraph(graph,V)
		G=g.getG()
		A,B=g.getBipartitionedGraph()[0],g.getBipartitionedGraph()[1]	# Initial partition
		print 'Initial graph is:'
		for f,t,w in graph:
			print '%s -> %s, weight=%d'%(f,t,w)
		print 'Initial partition: A=%s, B=%s'%(A,B)
		k=KernighanLin(G,V,A,B)
		newA,newB=k.getKernighanLin()[0],k.getKernighanLin()[1]
		print 'K-L partition: A=%s, B=%s'%(newA,newB)

	def vertex(self,graph):
		return list(set((Counter(list(zip(*graph)[0])).keys())) | set(Counter(list(zip(*graph)[1])).keys()))	# Get all vertex

# Define a weight undirected graph
G=[('a','b',1),('a','c',2),('a','d',3),('a','e',2),('a','f',4),\
	('b','c',1),('b','d',4),('b','e',2),('b','f',1),\
	('c','d',3),('c','e',2),('c','f',1),\
	('d','e',4),('d','f',3),\
	('e','f',2)]
Main().main(G)

		
