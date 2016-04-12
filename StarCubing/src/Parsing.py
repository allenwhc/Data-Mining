from collections import defaultdict, Counter
symboling=0
car_make=2

class Process(object):
	def __init__(self, input_data):
		self.original_data=input_data
		self.parsed_data=self.stripText()
		self.need_compress_catagory=self.checkNeedCompress()
		self.index=[]
		self.len_valid_dataset=[0] * len(map(list, zip(*self.parsed_data))) #
		self.counter=self.groupParsedData()

	def stripText(self):
		global car_make
		s=[line for line in self.original_data.read().splitlines()]
 		data=[line.split(',') for line in s]
 		data=map(list,zip(*data))
		for j in xrange(len(data[car_make])):
			if data[car_make][j] in ['nissan','toyota','mazda','honda','isuzu','subaru','mitsubishi']: data[car_make][j]='japenese-make'
			elif data[car_make][j] in ['volkswagen','bmw','audi','mercedes-benz']: data[car_make][j]='german-make'
			elif data[car_make][j] in ['peugot','renault']: data[car_make][j]='french-make'
			elif data[car_make][j] in ['plymouth','dodge','chevrolet']: data[car_make][j]='american-make'
			else: data[car_make][j]='others-make'
		return map(list,zip(*data))

	def checkNeedCompress(self):
		catagory=defaultdict(bool)
		global symboling
		for i in xrange(len(self.parsed_data[0])):
			try:
				float(self.parsed_data[0][i])
			except ValueError, e:
				catagory[i]=False
			else:
				catagory[i]=True
		catagory[symboling]=False
		return catagory

	def groupParsedData(self):
		dataset=map(list,zip(*self.parsed_data))
		index=[defaultdict(list)]*len(dataset)
		counter=[defaultdict(int)]*len(dataset)
		global car_make

		def convertToRange(data_by_column,curr_column_idx,row,n):
			d=defaultdict(int)
			trimmed_sorted_list=sorted(map(float,[x for x in data_by_column if x!='?'])) 
			self.len_valid_dataset[row]=len(trimmed_sorted_list)
			lower,upper=min(map(float,[x for x in data_by_column if x!='?'])),max(map(float,[x for x in data_by_column if x!='?']))
			num_range,i=[],lower
			while round(i+(upper-lower)/n,2)<=upper:
				num_range.append((str(i)+'-'+str(i+(upper-lower)/n),round(i+(upper-lower)/n,2)))
				i+=(upper-lower)/n

			for x, item in enumerate(data_by_column):
				for _range, _max in num_range:
					if item=='?': d['?']+=1
					elif item!='?' and float(item)<=_max:	
						d[_range]+=1
						curr_column_idx[_range].append(x)
						break
			return d

		for i in xrange(len(dataset)):
			if i==car_make or not self.need_compress_catagory[i]:
				counter[i]=defaultdict(int,Counter(dataset[i]))
			else:
				curr_column_idx=defaultdict(list)
				counter[i]=convertToRange(dataset[i], curr_column_idx, i, 4)
				index[i]=curr_column_idx
				self.index=index
		return counter

	def rearrangeData(self):
		regrouped_data=[]
		dataset=map(list, zip(*self.parsed_data))
		for i in xrange(len(dataset)):
			if self.need_compress_catagory[i]:
				for j in xrange(len(dataset[i])):
					for k in self.index[i].keys():
						if j in self.index[i][k]:
							dataset[i][j]=k
							break
		return map(list, zip(*dataset))


class Parse(Process):
	"""docstring for Strip"""
	def __init__(self, arg):
		super(Parse, self).__init__(arg)

	def getStripText(self):
		return self.parsed_data

	def getNeedCompreeCatagory(self):
		return self.need_compress_catagory

	def getNeedCompressRowIndex(self):
		return self.index

	def getRowConuter(self):
		return self.counter

	def getGroupedParsedData(self):
		return super(Parse, self).rearrangeData()

	def getValueDataLength(self):
		return self.len_valid_dataset
		
		