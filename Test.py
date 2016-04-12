class Test(object):
	def __init__(self):
		self.data_file=open('output/orginal_data_output','w')
		self.one_dimensional_aggregation_file=open('output/one_d_aggregate','w')
		self.star_table_file=open('output/star_table_output','w')

	def testOriginalData(self, data):
		self.data_file.write("Original data: \n")
		for d in data:
			self.data_file.write(','.join(d)+'\n')
		self.data_file.close()

	def testOneDimensionalAggregation(self, table, catagory, need_compressed):
		self.one_dimensional_aggregation_file.write("one dimensional aggregation: \n")
		for i,l in enumerate(table):
			if need_compressed[i]:
				less=[(k,v) for k,v in l[0].items()] if l[0] else []
				greater=[(k,v) for k,v in l[1].items()] if l[1] else []
				self.one_dimensional_aggregation_file.write('Catagory: '+catagory[i]+'\n')
				self.one_dimensional_aggregation_file.write('Less: '+','.join(map(str,less))+'\n')
				self.one_dimensional_aggregation_file.write('Greater: '+','.join(map(str,greater))+'\n')

	def testStarTable(self,table):
		self.star_table_file.write("Star table is: \n")
		for t in table:
			self.star_table_file.write(','.join(t)+'\n')
		self.star_table_file.close()