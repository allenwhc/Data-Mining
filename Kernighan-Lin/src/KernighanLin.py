from collections import defaultdict
from operator import itemgetter
class Process(object):
	def __init__(self,G,V,A,B):
		self.G=G
		self.V=V
		self.A=A
		self.B=B
		self.lock_status={v:False for v in self.V}

	def kernighanLin(self):
		G,V=self.G,self.V
		A,B=[x for x in self.A],[x for x in self.B]
		Gk,result=1,[]
		while Gk>0:
			curr_A,curr_B=[x for x in A],[x for x in B]
			I,E=self.getInternalExternalAJ(G,A,B,V)[0],self.getInternalExternalAJ(G,A,B,V)[1]
			D=self.computeCost(I,E,V)
			gain=[]
			i=0
			while False in self.lock_status.values():
				g=defaultdict(int)
				for u in A:
					for v in B:
						Cuv=G[u][list(zip(*G[u])[0]).index(v)][1]
						g[(u,v)]=D[u]+D[v]-2*Cuv
				swap_pair=max(g.items(), key=itemgetter(1))	# Get swap nodes by max cost
				gain.append((swap_pair[0],swap_pair[1]))	# Store gain
				node_A,node_B=swap_pair[0][0],swap_pair[0][1]
				self.lock_status[node_A]=self.lock_status[node_B]=True	# Lock swapped nodes
				A.remove(node_A)
				B.remove(node_B)
				for u in A:
					D[u]=D[u]+2*G[u][list(zip(*G[u])[0]).index(node_A)][1]-2*G[u][list(zip(*G[u])[0]).index(node_B)][1]
				for u in B:
					D[u]=D[u]+2*G[u][list(zip(*G[u])[0]).index(node_B)][1]-2*G[u][list(zip(*G[u])[0]).index(node_A)][1]
				i+=1
			prev_sum,curr_sum,idx,Gk=gain[0][1],0,0,gain[0][1]
			partial_sum=[gain[0][1]]
			for j in xrange(1,len(gain)):
				partial_sum.append(partial_sum[j-1]+gain[j][1])
				if partial_sum[j]>partial_sum[j-1]: 
					idx=j
			Gk=partial_sum[idx]
			need_swap=gain[idx][0]
			if Gk>0:
				# Swap target pairs
				A,B=[x for x in curr_A if x!=need_swap[0]],[x for x in curr_B if x!=need_swap[1]]
				A.append(need_swap[1])
				B.append(need_swap[0])
				result=[[x for x in A],[x for x in B]]
			self.lock_status={v:False for v in V}	# Unlock all nodes
		return result

	def computeCost(self,I,E,V):
		I={v:sum(list(zip(*I[v])[1])) for v in V}
		E={v:sum(list(zip(*E[v])[1])) for v in V}
		return {k:E[k]-I[k] for k in I.keys()}

	def getInternalExternalAJ(self,G,A,B,V):
		internal_AJ, external_AJ=defaultdict(list),defaultdict(list)
		for f in A:
			for i, t in enumerate(list(zip(*G[f])[0])):
				if t in A: internal_AJ[f].append(G[f][i])
				else: external_AJ[f].append(G[f][i])
		for f in B:
			for i, t in enumerate(list(zip(*G[f])[0])):
				if t in B: internal_AJ[f].append(G[f][i])
				else: external_AJ[f].append(G[f][i])
		return [internal_AJ,external_AJ]


class KernighanLin(Process):
	def __init__(self,G,V,A,B):
		super(KernighanLin, self).__init__(G,V,A,B)

	def getKernighanLin(self):
		return super(KernighanLin, self).kernighanLin()