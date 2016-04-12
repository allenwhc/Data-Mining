from collections import defaultdict

class Process(object):
	def __init__(self,counter, threshold):
		self.counter=counter
		self.threshold=threshold
		self.data_type=['float','range','string','string','string','string',\
						'string','string','string','range','range','range', \
						'range','range','string','string','range','string', \
						'range','range','range','range','range','range', \
						'range','range']	# type of variable of each catagory
		
	def oneDimensionalAggregates(self):
		table=[[] for i in xrange(len(self.counter))]
		for i in xrange(len(self.counter)):
			l=[defaultdict(int),defaultdict(int)]
			for k,v in self.counter[i].items():
				if v < self.threshold: l[0][k]=v
				else: l[1][k]=v
			table[i].append(l[0] if l[0] else [])
			table[i].append(l[1] if l[1] else [])
		return table

	def constructCompressedBaseTable(self, data, table, need_compress_catagory):
		data=map(list,zip(*data))
		for i in xrange(len(data)):
			for j in xrange(len(data[i])):
				if table[i][0] and data[i][j] in table[i][0].keys():
					data[i][j]='*'
		sorted_data=self.nodeOrdering(map(list,zip(*data)), need_compress_catagory)
		d=self.countDuplicateList(sorted_data)
		return [(','.join(sorted_data[k]),v) for k,v in d.items()]

	def nodeOrdering(self, table, need_compress_catagory):
		table_item=map(list,zip(*table))

		def preSortingConfig(data_type, curr_column):
			if not curr_column: return []
			if data_type=='float':
				for i in xrange(len(curr_column)):
					if curr_column[i]=='*': curr_column[i]=-float('inf')
					elif curr_column[i]=='?': curr_column[i]=float('inf')
			elif data_type=='range':
				for i in xrange(len(curr_column)):
					if curr_column[i]=='*': curr_column[i]=-float('inf')
					elif curr_column[i]=='?': curr_column[i]=float('inf')
					else: curr_column[i]=float(curr_column[i][:curr_column[i].index('-')])
			else:
				for i in xrange(len(curr_column)):
					if curr_column[i]=='*': curr_column[i]='#'
					elif curr_column[i]=='?': curr_column[i]='~'
			return curr_column

		# For string type, replace '*' by '#', '?' by '~';
		# For float or range type, replace '*' by '-inf', '?' by 'inf'
		new_config_table=map(list,zip(*[preSortingConfig(self.data_type[i],x) for i,x in enumerate(table_item)]))

		# Sort table by catagory
		new_config_table=map(list,zip(*sorted(new_config_table, key=lambda x: tuple([x[i] for i in range(len(new_config_table[0]))]))))
		
		# Reconfigure the table
		for i in xrange(len(new_config_table)):
			for j in xrange(len(new_config_table[i])):
				if need_compress_catagory[i]:
					for key in self.counter[i]:
						if str(new_config_table[i][j]) in key:
							new_config_table[i][j]=key
							break
				if new_config_table[i][j]==-float('inf') or new_config_table[i][j]=='#':
					new_config_table[i][j]='*'
				elif new_config_table[i][j]==float('inf') or new_config_table[i][j]=='~':
					new_config_table[i][j]='?'
		return map(list, zip(*new_config_table))

	def countDuplicateList(self, table):
		i,j=0,0
		d=defaultdict(int)
		while i<len(table):
			if i==j: j+=1
			while j<len(table) and not cmp(table[i], table[j]): j+=1
			d[i]=j-i
			i=j
		return d

class Cuboid(Process):
	def __init__(self, counter, threshold):
		super(Cuboid,self).__init__(counter, threshold)

	def getOneDimensionTable(self):
		return super(Cuboid, self).oneDimensionalAggregates()

	def getCompressedBaseTable(self, data, need_compress_catagory):
		table=super(Cuboid, self).oneDimensionalAggregates()
		return super(Cuboid, self).constructCompressedBaseTable(data, table, need_compress_catagory)