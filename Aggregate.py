import collections
class Aggregation(object):
	def __init__(self,data,n):
		self.data=data
		self.threshold=n

	"""
		Time complexity: O(nk), n is # of columns in data, k is # of keys in each column
		Extra space: O(n)
	"""
	def oneDimensionalAggregates(self):
		table=[[] for i in range(len(self.data))]
		for i in range(len(self.data)):
			curr_item=self.data[i].items()
			l=[collections.defaultdict(int),collections.defaultdict(int)]
			for (key,value) in curr_item:
				if value>=self.threshold:
					l[1][key]=value
				else:
					l[0][key]=value
			table[i].append(l[0] if l[0] else [])
			table[i].append(l[1] if l[1] else [])
		return table