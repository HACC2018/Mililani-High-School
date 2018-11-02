#import matplotlib here
#from matplotlib.pyplot import plt, pie
import matplotlib.pyplot as plt


timePoints = [15, 30, 40, 45, 60]
kilowattPoints = [4, 5, 77, 234, 100]


class Graph:

	def __init__(self, time, kilowatts):
		self.time = time
		self.kilowatts = kilowatts


		plt.plot(self.time,self.kilowatts)


	def changePlots(self, time, kilowatts):
		self.time = time
		self.kilowatts = kilowatts

		plt.clf()

		plt.plot(self.time,self.kilowatts)

	def drawPie(self, buildings, timeFrame):
		self.buildings = buildings
		self.timeFrame = timeFrame

	def showGraph(self):
		plt.show()


graph = Graph(timePoints,kilowattPoints)

graph.changePlots([1, 2, 3, 4],[100, 244, 123, 4000])
#graph.plt.show()
# ^ This line didn't work because the object had not been taught to show the graph internally. The addition of the method showGraph() fixed it

graph.showGraph()
