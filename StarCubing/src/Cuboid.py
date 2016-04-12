from collections import defaultdict
car_make=2

class StarTreeNode(object):
	def __init__(self):
		self.leaf=False


class Process(object):
	def __init__(self,counter, threshold):
		self.counter=counter
		self.threshold=threshold
		self.data_type=['float','range','string','string','string','string',\
						'string','string','string','range','range','range', \
						'range','range','string','string','range','string', \
						'range','range','range','range','range','range', \
						'range','range']
		
	def oneDimensionalAggregates(self):
		global car_make
		table=[[] for i in xrange(len(self.counter))]
		for i in xrange(len(self.counter)):
			l=[defaultdict(int),defaultdict(int)]
			for k,v in self.counter[i].items():
				if v < self.threshold: l[0][k]=v
				else: l[1][k]=v
			table[i].append(l[0] if l[0] else [])
			table[i].append(l[1] if l[1] else [])
		return table

	def constructCompressedBaseTable(self, data, table):
		data=map(list,zip(*data))
		for i in xrange(len(data)):
			#print table[i][0].keys()
			for j in xrange(len(data[i])):
				if table[i][0] and data[i][j] in table[i][0].keys():
					data[i][j]='*'
		data=map(list,zip(*data))
		d={}
		for i in range(0,len(data)):
			if not d: 
				d[i]=1
				continue
			for j,key in enumerate(d.keys()):
				if not cmp(data[i],data[key]): 
					#print i,key
					d[key]+=1
				else:
					if j==len(list(d.keys()))-1: d[i]=1
		return [(','.join(data[k]),v) for k,v in d.items()]

	def nodeOrdering(self, compressed_table):
		compressed_table=map(list, zip(*compressed_table))
		table_item=map(list,zip(*[item.split(',') for item in compressed_table[0]]))

		def sortByCatagory(data_type, start, end, arr):
			if data_type=='float' or 'range':
				arr=sorted(arr[start:end])
			elif data_type=='string':
				arr=sorted(arr[start:end], key=lambda x: ord(x[0]))
			# else:
			# 	# arr=[float(x[:x.index('-')]) if isinstance(x,str) else x for x in arr]
			# 	# print arr
			# 	arr=sorted(arr[start:end])
			return arr

		# Replace '*' in each row for sorting
		for i in xrange(len(table_item)):
			curr_column=table_item[i]
			# For string type, replace '*' by '#';
			# For float or range type, replace '*' by '-inf'
			if '*' in table_item[i]:
				curr_column=['#' if x=='*' else x for x in curr_column] if self.data_type[i]=='string' else [-float('inf') if x=='*' else x for x in curr_column]
			table_item[i]=curr_column
		# for i in table_item[18]:
		# 	print type(i)
		print table_item[0]
		table_item=sorted(table_item, key=lambda x: x[0])
		print table_item
		# for i in table_item[19]:
		# 	print i,'ori'
		# table_item[19]=sortByCatagory(self.data_type[19],0,len(table_item[19]),table_item[19])
		# for i in table_item[19]:
		# 	print i
		#print table_item[8]

		return map(list,zip(*compressed_table))

	def starCubing(self):
		pass

class Cuboid(Process):
	def __init__(self, counter, threshold):
		super(Cuboid,self).__init__(counter, threshold)

	def getOneDimensionTable(self):
		return super(Cuboid, self).oneDimensionalAggregates()

	def getCompressedBaseTable(self, data):
		table=super(Cuboid, self).oneDimensionalAggregates()
		return super(Cuboid, self).constructCompressedBaseTable(data, table)

	def getNodeOrdering(self, compressed_table):
		return super(Cuboid, self).nodeOrdering(compressed_table)
