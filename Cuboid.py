import collections
class Cuboid(object):
	def __init__(self, data, table, index, need_compressed):
		self.data=map(list,zip(*data[1:]))
		self.table=table
		self.index=index
		self.need_compressed=need_compressed

	
	def constructStarTable(self):
		starTable,t=[],[]
		# First, substitute all data less than threshold with '*'
		"""
		Time complexity: O(size of data * k), k is # of keys in dictionary
		Extra space: O(1)
		"""
		for i in range(len(self.data)):
			if i==2:
				for j in range(len(self.data[i])):
					if self.data[i][j] in self.table[i][0]:
						self.data[i][j]='*'
				continue
			if self.need_compressed[i]:
				for j in range(len(self.data[i])):
					for key in self.index[i]:
						if j in self.index[i][key]:
							self.data[i][j]=key
							break
					if self.data[i][j] in self.table[i][0]:
						self.data[i][j]='*'
		self.data=map(list,zip(*self.data))
		x=open('star_table_output.txt','w')
		for i in self.data:
			x.write(','.join(i)+'\n')
		x.close()

		# Then, combine all duplicate list
		d={}
		for i in range(0,len(self.data)):
			if not d: 
				d[i]=1
				continue
			for j,key in enumerate(d.keys()):
				if not cmp(self.data[i],self.data[key]): 
					#print i,key
					d[key]+=1
				else:
					if j==len(list(d.keys()))-1: d[i]=1
		#print d

		return self.data
