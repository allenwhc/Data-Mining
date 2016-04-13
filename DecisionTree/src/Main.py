from collections import Counter
import math	
class Main(object):
	def __init__(self):
		self.input_data=open('../data/data.txt','r')
	
	def main(self):	
		parsed_data=self.parseText()	# parse data
		occurrence=[Counter(l) for l in map(list,zip(*parsed_data))] 	#count occurrence by attribute
		gini_index=self.computeGiniIndex(occurrence, len(parsed_data))
		print gini_index

	def parseText(self):
		return [line.split(',') for line in self.input_data.read().splitlines()]

	def computeGiniIndex(self, occurrence, total_entry):
		return [round(1-sum([math.pow(round(float(v)/float(total_entry),3),2) for v in t.values()]),3) for t in occurrence]

Main().main()