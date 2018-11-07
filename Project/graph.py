#import matplotlib here
'''
import matplotlib.pyplot as plt
import database.database as data

#List of coordinates for plotting 

class Graph:

	def __init__(self, database):
		#Initialize graph after prospects 
		#Loop for grabbing buildings and data points 
		self.ticks = []
		self.labels = []
		for buildingNum in range(0, len(database.buildingsData)):
			self.timestamps = []
			self.kilowatts = []
			for dataPoint in range(0, len(database.buildingsData[buildingNum].dataPoints)):
				self.timestamps.append(database.SetDateToUnix(database.buildingsData[buildingNum].dataPoints[dataPoint].timestamp))
				self.kilowatts.append(float(database.buildingsData[buildingNum].dataPoints[dataPoint].kilowatts))
			plt.plot(self.timestamps,self.kilowatts,label=str(database.buildingsData[buildingNum].name))
			plt.xlabel('Timestamp')
			plt.ylabel('Kilowatts')
			plt.legend()

		tickNum = 8
		for x in range(0, tickNum):
			self.ticks.append((x * ((database.unixInterval[1] - database.unixInterval[0]) / tickNum) + database.unixInterval[0]))
			#print(self.ticks[x])#verifies the graph ticks
			self.labels.append(database.SetUnixToDate((x * ((database.unixInterval[1] - database.unixInterval[0]) / tickNum) + database.unixInterval[0])))
			#print(self.labels[x])#verifies the graph tick labels
		self.ticks.append(database.unixInterval[1])
		self.labels.append(database.SetUnixToDate(database.unixInterval[1]))
		plt.xticks(ticks=self.ticks, labels=self.labels, rotation=15)
		plt.title("Dynamic Kilowatt/hr Graph")
		plt.show()

 
database = data.Database('database/csv/AnalyticsData_20181019174047.csv')#test csv
#building = Building(buildings[0])

database.SetInterval(" 1/3/2018 10:30:00 AM", " 2/3/2018 10:30:00 AM")
for i in range(5, len(database.buildings)):
	database.ChangeBuilding(i)

database.ReadData()
graph = Graph(database)

'''