from Parsing import Parsing
from FPTree import FPTree, FPTreeNode
from FrequentItemsetGeneration import FPGrowth
from Test import Test
import random
# from operator import itemgetter
# from collections import defaultdict
class Main(object):
	def __init__(self):
		self.input_data=open('../data/data.txt','r')

	def main(self):
		""" Parsing """
		parse=Parsing(self.input_data)
		parse_data=parse.parseText()	# Get parsed data
		self.input_data.close()	# Close input data

		""" FP-Tree construction """
		fp_t=FPTree(parse_data)
		reorganized_data=fp_t.getReorganizedData()	# Reordered data by support in descending order
		support=fp_t.getItemSupport()	# Support
		fpTree_root=fp_t.getFPTree(parse_data)	# FP-Tree

		""" FP-Tree itemset generation"""
		minSup=2	# Minimum support
		#target_item=random.choice([(k,v) for k,v in support.items() if v>=minSup])[0]	# Pick random item
		target_item='e'
		valid_itemset=[entry for entry in reorganized_data if entry[-1]==target_item]
		#valid_least_frequent_item=sorted([(k,v) for k,v in support.items() if v>=minSup],reverse=True)[0][0]
		growth=FPGrowth(fpTree_root, minSup)
		growth.getConditionalFPTree()

		#conditional_trees=growth.getConditionalFPTree(support.keys())	# Get conditional Fp trees

		""" Test """
		t=Test()
		t.testParsedData(parse_data)
		t.testReorganized(reorganized_data)
		t.testFPTree(fpTree_root)

Main().main()