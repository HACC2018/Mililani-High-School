import datatype#imports our local file datatype.py

import calendar
import csv
import datetime
import time

class Database():

	buildings = []
	dataInterval = []
	#time is handled in int(unix timestamp) form (make sure you conve rt to int)

	def __init__(self, csvFile):
		#look through the csv and add each building a list
		#in the same loop get the earliest timstamp and latest

		Database.buildings = list(csv.reader(open(csvFile), delimiter=','))[0]#total buildings list
		del Database.buildings[0]#delete time entry from building list
		self.selectedBuildings = []#we will append building indexes to this
		#For example prospects could equal [1,4,2,6], these refer to the 
		#index of those builings we want to look at. This makes it so
		#that we only need to store the int of its index vs the entire instance
		csvRows = len(list(csv.reader(open(csvFile), delimiter=',')))#number of rows in csv starting at 1
		Database.dataInterval = [int(self.SetDateToUnix(list(csv.reader(open(csvFile), delimiter=','))[1][0])),#time at begining of csv
								 int(self.SetDateToUnix(list(csv.reader(open(csvFile), delimiter=','))[csvRows - 1][0]))]
		#add time at end of csv (subtract 1 from rows)
		#print(Database.dataInterval[0])
		#print(self.SetUnixToDate(Database.dataInterval[0]))



	def SetInterval(self, start, end):#input as datetime string
		if (int(self.SetDateToUnix(start)) < Database.dataInterval[0]):
			start = self.SetUnixToDate(Database.dataInterval[0])
		if (int(self.SetDateToUnix(end)) < Database.dataInterval[1]):
			end = self.SetUnixToDate(Database.dataInterval[1])
		self.unixInterval = [int(self.SetDateToUnix(start)), int(self.SetDateToUnix(end))]
		self.dateInterval = [start, end]


	def SetUnixToDate(self, unix):#input unix time as string or int
		unix = int(unix) #gets rid of utc time difference of 10 hours
		return datetime.datetime.utcfromtimestamp(unix).strftime(' %m/%d/%Y %I:%M:%S %p')

	def SetDateToUnix(self, date):#input date string
		#print(date)# the utc problem happens at the unix conversion
		utc = datetime.datetime.strptime(date, ' %m/%d/%Y %I:%M:%S %p')
		return int(utc.timestamp()) - 36000#unix is UTC time which is 10 hours ahead (36000 seconds)


	def AddBuilding(self, selectedBuilding):#send the building by index of buildings list
		self.selectedBuildings.append(selectedBuilding)

	def RemoveBuilding(self, selectedBuilding):
		self.selectedBuildings.remove(selectedBuilding)

		#we will only refer to buildings by their index in the list, never by name

	def ReadCSV(self):#put a list of indexes as the parameter
		for i in self.selectedBuildings:
			print("fuck python")
			building = datatype.Building()
			#print("building", self.selectedBuildings[i])
			CSVDATA = csv.reader(open("csv/AnalyticsData_20181019174047.csv"), delimiter=",")
			print(len(list(CSVDATA)))
			self.buildings = []
			currentLine = []
			for j in range(1, len(list(CSVDATA))):
				print("before")
				#currentLine = CSVDATA.__next__()
				print("after")
				if int(self.SetDateToUnix(currentLine[0])) >= int(self.unixInterval[0]):
					datapoint = datatype.DataPoint(int(self.SetDateToUnix(currentLine[0])), currentLine[self.selectedBuildings[i]])
					building.dataPoints.append(datapoint)
					print(dataPoint.timestamp, " : ", dataPoint.kilowatts)
				if int(self.SetDateToUnix(currentLine[0])) > int(self.unixInterval[1]):
					j = len(list(CSVDATA))
			self.buildings.append(building)
		return self.buildings

#initializes an instance of database
database = Database('csv/AnalyticsData_20181019174047.csv')#test csv
#building = Building(buildings[0])

database.SetInterval(" 1/3/2018 10:30:00 AM", " 1/10/2018 10:30:00 AM")
database.AddBuilding(1)


database.ReadCSV()
