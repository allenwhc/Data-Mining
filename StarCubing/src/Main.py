from Parsing import Parse
from Cuboid import Cuboid
from Test import Test


class Main(object):
	def __init__(self):
		self.input=open('../data/data.txt','r')

	def main(self):
		# parse input data 
		strip=Parse(self.input)
		parsed_data=strip.getStripText()	# Parse input data
		need_compress_catagory=strip.getNeedCompreeCatagory()	# Check which catagories need group
		#row_counter=strip.getRowConuter()
		grouped_data=strip.getGroupedParsedData()

		#Create cuboid
		division_factor=4
		#threshold=[x/division_factor for x in strip.getValueDataLength()]
		min_sup=len(grouped_data)/division_factor
		cuboid=Cuboid(strip.getRowConuter(), min_sup)
		oneDimensionTable=cuboid.getOneDimensionTable()
		compressedBaseTable=cuboid.getCompressedBaseTable(grouped_data)
		nodeOrdering=cuboid.getNodeOrdering(compressedBaseTable)

		# test results
		t=Test()
		t.testParsedData(parsed_data)	# Test if parsed data is correct
		t.testNeedCompressCatagory(need_compress_catagory) # Test which catagory needs compress
		t.testGroupedParsedData(grouped_data)
		t.testOneDimensionAggregatation(oneDimensionTable,need_compress_catagory, min_sup)
		t.testCompressedBaseTable(compressedBaseTable)

m=Main()
m.main()