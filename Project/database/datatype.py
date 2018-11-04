import matplotlib.pyplot as plt 

class DataPoint:

	def __init__(self, timestamp, kilowatts):#store timestamp as a unix timestamp
		self.timestamp = timestamp
		self.kilowatts = kilowatts


class Building:

	def __init__(self):
		self.dataPoints = []

class CSV:
	def __init__(self, path, start, end)
		self.path = "csv/" + path
		self.interval = [start, end]
		self.buildings = []