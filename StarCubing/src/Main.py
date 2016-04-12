from Parsing import Parse
from Cuboid import Cuboid
from Test import Test
from StarCubing import Cubing

class Main(object):
	def __init__(self):
		self.input=open('../data/data.txt','r')

	def main(self):
		""" Data parsing/processing section"""
		# parse input data 
		strip=Parse(self.input)
		parsed_data=strip.getStripText()	# Parse input data
		need_compress_catagory=strip.getNeedCompreeCatagory()	# Check which catagories need group
		grouped_data=strip.getGroupedParsedData()	# Group data

		""" Cuboid construction section """
		#Create cuboid
		division_factor=3
		min_sup=len(grouped_data)/division_factor	# Iceberg condition
		cuboid=Cuboid(strip.getRowConuter(), min_sup)
		oneDimensionTable=cuboid.getOneDimensionTable()	# Conduct 1-D aggregate
		compressedBaseTable=cuboid.getCompressedBaseTable(grouped_data, need_compress_catagory)	# Construct compressed base table

		""" Star tree/table construction section"""
		#Construct star tree and star table
		s_t=Cubing(compressedBaseTable)
		root=s_t.starCubing()
		#s_t.constructStarTree()

		""" Test/Output section """
		# test results
		t=Test()
		t.testParsedData(parsed_data)	# Test if parsed data is correct
		t.testNeedCompressCatagory(need_compress_catagory) # Test which catagory needs compress
		t.testGroupedParsedData(grouped_data)	# Test grouped data
		t.testOneDimensionAggregatation(oneDimensionTable,need_compress_catagory, min_sup)	# Test 1-D aggregation
		t.testCompressedBaseTable(compressedBaseTable)	# Test node-ordered compressed base table
		t.testStarTree(root,0,s_t.count,'')

m=Main()
m.main()