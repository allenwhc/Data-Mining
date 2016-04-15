class Test(object):
	def __init__(self):
		self.rules=[]

	def outputDecisionTree(self, root):
		tree=open('../data/decistion_tree','w')
		tree.write('Decision tree is:\n')
		q,lv=[root],0
		def dfs(node,path):
			if node.leaf:
				tree.write('->'.join(path)+'\n')
				path.pop()
				return
			for value, child in node.children.items():
				path.append(value)
				if child.leaf: path.append(child.label)
				dfs(child, path)
				path.pop(-1)
				
		while q:
			sz=len(q)
			tree.write('lv:%s'%str(lv)+"     ")
			for i in range(sz):
				node=q.pop(0)
				for value,child in node.children.items():
					q.append(child)
					tree.write(value+'('+node.label+')'+'     ')
			tree.write('\n')
			lv+=1
		tree.write('Decision rules are:\n')
		dfs(root,[])
		tree.close()

	def outputTestOutcome(self, test_data, test_result):
		result=open('../data/test_result','w')
		result.write("Test result is:\n")
		for D,R in zip(test_data, test_result):
			result.write('If '+','.join(D)+', then: %s\n'%R)

