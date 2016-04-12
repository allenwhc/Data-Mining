from Parsing import Parsing
from Aggregate import Aggregation
from Cuboid import Cuboid
from Test import Test
def main(file):
	s=[line for line in file.read().splitlines()]
	file.close()
	data=[line.split(',') for line in s]
	#	data catagory: 
	#	1. symboling:                -3, -2, -1, 0, 1, 2, 3.
	#  	2. normalized-losses:        continuous from 65 to 256.
	#  3. make:                     alfa-romero, audi, bmw, chevrolet, dodge, honda,
		# 						   isuzu, jaguar, mazda, mercedes-benz, mercury,
		# 						   mitsubishi, nissan, peugot, plymouth, porsche,
		# 						   renault, saab, subaru, toyota, volkswagen, volvo
	 #  4. fuel-type:                diesel, gas.
	 #  5. aspiration:               std, turbo.
	 #  6. num-of-doors:             four, two.
	 #  7. body-style:               hardtop, wagon, sedan, hatchback, convertible.
	 #  8. drive-wheels:             4wd, fwd, rwd.
	 #  9. engine-location:          front, rear.
	 # 10. wheel-base:               continuous from 86.6 120.9.
	 # 11. length:                   continuous from 141.1 to 208.1.
	 # 12. width:                    continuous from 60.3 to 72.3.
	 # 13. height:                   continuous from 47.8 to 59.8.
	 # 14. curb-weight:              continuous from 1488 to 4066.
	 # 15. engine-type:              dohc, dohcv, l, ohc, ohcf, ohcv, rotor.
	 # 16. num-of-cylinders:         eight, five, four, six, three, twelve, two.
	 # 17. engine-size:              continuous from 61 to 326.
	 # 18. fuel-system:              1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi.
	 # 19. bore:                     continuous from 2.54 to 3.94.
	 # 20. stroke:                   continuous from 2.07 to 4.17.
	 # 21. compression-ratio:        continuous from 7 to 23.
	 # 22. horsepower:               continuous from 48 to 288.
	 # 23. peak-rpm:                 continuous from 4150 to 6600.
	 # 24. city-mpg:                 continuous from 13 to 49.
	 # 25. highway-mpg:              continuous from 16 to 54.
	 # 26. price:                    continuous from 5118 to 45400.

	#Compress all continuous catagory
	compressed_catagory=['normalized-losses','wheel-base',\
			'length','width','height','curb-weight','engine-size',\
			'bore','stroke','compression-ratio','horsepower','peak-rpm','city-mpg','highway-mpg','price']

	data=groupMaker(data)	

	# Get compressed data
	parse=Parsing(data,compressed_catagory)
	agg=Aggregation(parse.getNeedCompressedCounter(),len(data[1:])/4)	# get grouped data
	aggregatedTable=agg.oneDimensionalAggregates()	# get 1-D aggregates
	cuboid=Cuboid(data, aggregatedTable, parse.getNeedCompressedIndex(), parse.getNeedCompressedCatagory())
	starTable=cuboid.constructStarTable()

	""" Test Section"""
	test=Test()
	test.testOriginalData(data[1:])	# test original data
	test.testOneDimensionalAggregation(aggregatedTable, data[0], parse.getNeedCompressedCatagory())
	#test.testStarTable(starTable)	# test star table

def groupMaker(data):
	data=map(list,zip(*data))
	for i in xrange(len(data)):
		if data[i][0]=='make':
			for j in xrange(1,len(data[i])):
				if data[i][j] in ['nissan','toyota','mazda','honda','isuzu','subaru','mitsubishi']: data[i][j]='japenese-make'
				elif data[i][j] in ['volkswagen','bmw','audi','mercedes-benz']: data[i][j]='german-make'
				elif data[i][j] in ['peugot','renault']: data[i][j]='french-make'
				elif data[i][j] in ['plymouth','dodge','chevrolet']: data[i][j]='american-make'
				else: data[i][j]='others-make'
	return map(list,zip(*data))

def printCompressedData(data):
	for i in data:
		print i

def printAggregates(table):
	for t in table:
		print t

def printStarTable(table):
	for i, t in enumerate(table):
		print i, t
	
file=open('data.txt','r')
main(file)