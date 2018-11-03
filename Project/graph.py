#import matplotlib here

import matplotlib.pyplot as plt
#import database.database as database 

#List of coordinates for plotting 

class Graph:

	def __init__(self): 
		plt.plot()
		plt.show()

	def setInterval(self, start, end):
		database.setInterval





	'''def __init__(self):
		self.timeStamps = []
		self.kilowatts = []
		#Initialize graph after prospects 
		#Loop for grabbing buildings and data points 
		for i in database.buildingData:
			for j in database.buildingData[i].dataPoints[j]:
				self.timeStamps.append(database.buildingData[i].dataPoints[j].timestamp)
				self.kilowatts.append(database.buildingData[i].dataPoints[j].kilowatts)

			#plt.xticks(ticks= , labels=, rotation=45)
			plt.plot(self.timeStamps,self.kilowatts,label=str(database.buildingData[i].name))
			plt.xlabel('Date/Time')
			plt.ylabel('Kilowatts')
			plt.title('Buildings')
			plt.legend()
			plt.show()

'''

graph = Graph()

