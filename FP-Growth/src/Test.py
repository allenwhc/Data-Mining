class Test(object):
	def __init__(self):
		pass

	def testParsedData(self, parsed_data):
		parse=open('../test/parsed_data','w')
		parse.write('Parsed data is:\n')
		for d in parsed_data:
			parse.write(','.join(d)+'\n')
		parse.close()

	def testReorganized(self, d):
		support=open('../test/reorganized_data','w')
		support.write('Reorganized data is:\n')
		for k in d:
			support.write(','.join(k)+'\n')
		support.close()

	def testFPTree(self, root):
		tree=open('../test/FPTree','w')
		tree.write('FPTree is: \n')
		lv,q=0,[root]
		tree.write('lv:0   root\n')
		while q:
			sz=len(q)
			lv+=1
			tree.write('lv:%s   '%str(lv))
			for i in range(sz):
				node=q.pop(0)
				for v in node.children.values():
					q.append(v)
					tree.write(v.val+'('+str(v.count)+') -> '+(v.next.val+'('+str(v.next.count)+')' if v.next else 'null')+'   ')
			tree.write('\n')
		tree.close()