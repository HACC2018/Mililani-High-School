#import matplotlib here
import matplotlib.pyplot as plt 
#testing
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

		plt.plot(self.time,self.kilowatts)
		
		

graph = Graph(timePoints,kilowattPoints)

graph.changePlots([1, 2, 3, 4],[100, 244, 123, 4000])
graph.plt.show()


