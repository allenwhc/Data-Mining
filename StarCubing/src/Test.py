car_make=2
class Test(object):
	def __init__(self):
		self.starTree=open('../output/star_tree','w')
		self.catagory=['symboling','normalized-losses','make','fuel-type','aspiration','num-of-doors',\
					'body-style','drive-wheels','engine-location','wheel-base','length','width',\
					'height','curb-weight','engine-type','num-of-cylinders','engine-size',\
					'fuel-system','bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

	def testParsedData(self, data):
		parsed_data=open('../output/parsed_data','w')
		parsed_data.write('The post parsed data is:'+'\n')
		for d in data:
			parsed_data.write(','.join(d)+'\n')
		parsed_data.close()

	def testNeedCompressCatagory(self, d):
		need_compress_catagory=open('../output/need_compressed','w')
		need_compress_catagory.write('Catagory:'+'\n')
		for i in xrange(len(self.catagory)):
			if d[i]: need_compress_catagory.write(self.catagory[i]+' needs compress'+'\n')
			else: need_compress_catagory.write(self.catagory[i]+' does not need compress'+'\n')
		need_compress_catagory.close()

	def testGroupedParsedData(self, data):
		group_data=open('../output/grouped_parsed_data','w')
		group_data.write('Regroup data is: '+'\n')
		for row in data:
			group_data.write(','.join(row)+'\n')
		group_data.close()

	def testOneDimensionAggregatation(self, table, catagory, threshold):
		one_d_table=open('../output/one_dimension_aggregation','w')
		one_d_table.write('Result of 1-D aggregation is: \n')
		global car_make
		for i, item in enumerate(table):
			#if catagory[i] or i==car_make:
			less,greater=[(k,v) for k,v in item[0].items()] if item[0] else [], [(k,v) for k,v in item[1].items()] if item[1] else []
			one_d_table.write(self.catagory[i]+'(threshold:'+str(threshold)+')'+'\n')
			one_d_table.write("Less than threshold: "+','.join(map(str,less))+'\n')
			one_d_table.write('greater than threshold:'+','.join(map(str,greater))+'\n\n')
		one_d_table.close()

	def testCompressedBaseTable(self, compressed_table):
		compress=open('../output/compressed_base_table','w')
		compress.write('Compressed base table is: \n')
		for i, (item, count) in enumerate(compressed_table,1):
			compress.write(('Item %s: '+item+'\n'+'Count:'+str(count)+'\n\n')%str(i))
		compress.close()

	def testStarTree(self, root, lv, count, indent):
		q=[]
		q.append(root)
		while q:
			sz=len(q)
			self.starTree.write('lv=%s'%(lv+1)+'\n')
			for i in range(sz):
				node=q.pop(0)
				for k,v in node.children.items():
					q.append(v)
					self.starTree.write(k+'   ')
			self.starTree.write('\n')
			lv+=1
		# for k,v in root.children.items():
		# 	self.starTree.write(indent+'item=%s'%k+', level=%s'%str(lv+1)+', count='+str(count[lv])+'\n')
		# 	self.testStarTree(v, lv+1, count, indent+'   ')
