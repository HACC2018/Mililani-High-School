import database.datatype as datatype #imports our local file datatype.py

import calendar
import csv
import datetime
import glob
import time

class Database:

	buildings = []
	dataInterval = []
	#time is handled in int(unix timestamp) form (make sure you conve rt to int)

	def __init__(self):
		#look through the csv and add each building a list
		#in the same loop get the earliest timstamp and latest

		self.csv = list(glob.glob(".\\database\\csv\\*.csv"))[0]
		with open(self.csv) as file:
			CSVDATA = csv.reader(file, delimiter=",")
			rowNum = 0
			for row in CSVDATA:
				if rowNum == 0:
					columnNum = 0
					for column in row:
						if columnNum != 0:
							building = datatype.Building()
							building.name = row[columnNum]
							building.index = columnNum
							Database.buildings.append(building)
						columnNum += 1
				else:
					break
				rowNum += 1

		#verifies all buildings index and name on csv
		#for i in range(0, len(self.buildings)):
		#	print(self.buildings[i].index, self.buildings[i].name)

		Database.buildings = list(csv.reader(open(self.csv), delimiter=','))[0]#total buildings list
		del Database.buildings[0]#delete time entry from building list
		self.selectedBuildings = []#we will append building indexes to this
		#For example prospects could equal [1,4,2,6], these refer to the 
		#index of those builings we want to look at. This makes it so
		#that we only need to store the int of its index vs the entire instance
		csvRows = len(list(csv.reader(open(self.csv), delimiter=',')))#number of rows in csv starting at 1
		Database.dataInterval = [int(self.SetDateToUnix(list(csv.reader(open(self.csv), delimiter=','))[1][0])),#time at begining of csv
								 int(self.SetDateToUnix(list(csv.reader(open(self.csv), delimiter=','))[csvRows - 1][0]))]
		#add time at end of csv (subtract 1 from rows)
		#print(Database.dataInterval[0])
		#print(self.SetUnixToDate(Database.dataInterval[0]))



	def SetInterval(self, start, end):#input as datetime string
		if (int(self.SetDateToUnix(start)) < Database.dataInterval[0]):
			start = self.SetUnixToDate(Database.dataInterval[0])
		if (int(self.SetDateToUnix(end)) > Database.dataInterval[1]):
			end = self.SetUnixToDate(Database.dataInterval[1])
		self.unixInterval = [int(self.SetDateToUnix(start)), int(self.SetDateToUnix(end))]
		self.dateInterval = [start, end] #in utc format, not csv format


	def SetUnixToDate(self, unix):#input unix time as string or int
		return datetime.datetime.utcfromtimestamp(unix).strftime(' %m/%d/%Y %I:%M:%S %p')

	def SetDateToUnix(self, date):#input date string
		utc = datetime.datetime.strptime(date, ' %m/%d/%Y %I:%M:%S %p')
		return int(utc.timestamp()) - 36000#unix is UTC time which is 10 hours ahead (36000 seconds)


	def SetUnixToLabel(self, unix):
		return datetime.datetime.utcfromtimestamp(unix).strftime('%m/%d/%y %I:%M %p')


	def ChangeBuilding(self, selectedBuilding):#send the building by index of buildings list
		if selectedBuilding not in self.selectedBuildings:
			self.selectedBuildings.append(selectedBuilding)
		elif selectedBuilding in self.selectedBuildings:
			self.selectedBuildings.remove(selectedBuilding)


		#we will only refer to buildings by their index in the list, never by name

	def ReadData(self):#read selected buildings and corresponding data points into classes
		self.buildingsData = []
		hasData = False
		if self.selectedBuildings == []:
			return []

		for i in self.selectedBuildings:
			building = datatype.Building()
			self.buildingsData.append(building)

		with open(self.csv) as csvFile:

			CSVDATA = csv.reader(csvFile, delimiter=",")
			rowNum = 0
			for row in CSVDATA:
				if rowNum == 0:#set names of selected buildings if on first row
					for i in range(0,len(self.selectedBuildings)):
						self.buildingsData[i].name = row[self.selectedBuildings[i]]#skips first column because it is empty
				else:
					columnNum = 0
					for column in row:
						if self.SetDateToUnix(row[0]) >= self.unixInterval[0]:
							if columnNum in self.selectedBuildings:#only add data if column is selected
								dataPoint = datatype.DataPoint(row[0], row[columnNum])
								hasData = True
								self.buildingsData[self.selectedBuildings.index(columnNum)].dataPoints.append(dataPoint)#add data points to building classes
						if self.SetDateToUnix(row[0]) > self.unixInterval[1]:
							break
						columnNum += 1
				rowNum += 1

		if hasData == False:
			return False
		elif hasData == True:
			return True

		#for buildingNum in range(0, len(self.buildingsData)):
		#	print(self.buildingsData[buildingNum].name)
		#	for dataPointNum in range(0, len(self.buildingsData[buildingNum].dataPoints)):
		#		print(self.buildingsData[buildingNum].dataPoints[dataPointNum].timestamp, " | ", self.buildingsData[buildingNum].dataPoints[dataPointNum].kilowatts)

		return self.buildingsData#return list of building classes


#initializes an instance of database
#database = Database('csv/AnalyticsData_20181019174047.csv')#test csv
#building = Building(buildings[0])

#database.SetInterval(" 1/3/2018 10:30:00 AM", " 1/10/2018 10:30:00 AM")
#database.AddBuilding(3)
#database.AddBuilding(1)

#database.ReadData()