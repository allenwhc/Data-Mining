import collections
class Parsing(object):
	"""docstring for Parsing"""
	def __init__(self, data, compressed_catagory):
		self.data=data[1:]
		self.determine_compressed_catagory={}
		for i in range(len(data[0])): 
			self.determine_compressed_catagory[i]=True if data[0][i] in compressed_catagory else False
		self.group=map(list,zip(*self.data))
		self.counter=[collections.defaultdict()]*len(map(list,zip(*data)))
		self.index=[collections.defaultdict(list)]*len(map(list,zip(*data)))
		self.compressData()

	""" Group data by column """
	def compressData(self):
		# group age from isolated integer to range
		def divideIntoChunks(t,n,idx,row):
			d=collections.defaultdict(int)
			idx['unknown']=[i for i, x in enumerate(t) if x=='unknown']
			trimed_list=[x for x in t if x!='unknown']
			lower,upper=sorted(map(float,trimed_list))[0],sorted(map(float,trimed_list))[-1]
			for x,item in enumerate(trimed_list):
				i=lower
				while i+(upper-lower)/n<=upper:
					new_range=str(i)+'-'+str((i+(upper-lower)/n))
					if i<=float(item)<i+(upper-lower)/n:
						idx[new_range].append(x)
						d[new_range]+=1
					i+=(upper-lower)/n
			return d
		for i in range(len(self.group)):
			if i==2: 
				self.counter[i]=collections.defaultdict(int,collections.Counter(self.group[i]))
				continue
			idx=collections.defaultdict(list)
			self.group[i]=[x if x!='?' else 'unknown' for x in self.group[i]]
			self.counter[i]['unknown']=self.group[i].count('unknown')
			if self.determine_compressed_catagory[i]:
				self.counter[i]=divideIntoChunks(self.group[i],4,idx,i)
			self.index[i]=idx

	def getNeedCompressedCounter(self):
		return self.counter

	def getNeedCompressedIndex(self):
		return self.index

	def getNeedCompressedCatagory(self):
		return self.determine_compressed_catagory

