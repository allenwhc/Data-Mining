class Process(object):
	"""docstring for Process"""
	def __init__(self, input_data):
		self.input_data = input_data

	def parseText(self):
		return [line.split(',') for line in self.input_data.read().splitlines()]


class Parsing(Process):
	"""docstring for Parsing"""
	def __init__(self, input_data):
		super(Parsing, self).__init__(input_data)

	def getParsedData(self):
		return super(Parsing, self).parseText()


		
		