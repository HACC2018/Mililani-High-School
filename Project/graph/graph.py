#import matplotlib here
#from matplotlib.pyplot import plt, pie
import matplotlib.pyplot as plt

#List of coordinates for plotting 
timePoints = [15, 30, 40, 45, 60]
kilowattPoints = [4, 5, 77, 234, 100]


class Graph:
#Set init paramaters to interval and buildingIndex
	def __init__(self, buildingName, time, kilowatts):
		self.buildingName = buildingName 
		self.time = time
		self.kilowatts = kilowatts
		plt.plot(self.time,self.kilowatts,label=str(self.buildingName))
		plt.xlabel('Date/Time')
		plt.ylabel('Kilowatts')
		plt.title('Buildings')
		plt.legend()

	def changePlots(self, time, kilowatts):
		self.time = time
		self.kilowatts = kilowatts

		plt.clf()
		plt.plot(self.time,self.kilowatts,label=str())
		plt.xlabel('Date/Time')
		plt.ylabel('Kilowatts')
		plt.title('Buildings')
		plt.legend()
		plt.plot(self.time,self.kilowatts)

	def drawPie(self, buildings, timeFrame):
		self.buildings = buildings
		self.timeFrame = timeFrame

	def showGraph(self):
		plt.show()


graph = Graph('BuildingA', timePoints,kilowattPoints)

#graph.plt.show()
# ^ This line didn't work because the object had not been taught to show the graph internally. The addition of the method showGraph() fixed it

graph.showGraph()
