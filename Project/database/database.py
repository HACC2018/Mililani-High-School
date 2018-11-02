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
		self.prospects = []#we will append building indexes to this
		#For example prospects could equal [1,4,2,6], these refer to the 
		#index of those builings we want to look at. This makes it so
		#that we only need to store the int of its index vs the entire instance
		csvRows = len(list(csv.reader(open(csvFile), delimiter=',')))#number of rows in csv starting at 1
		Database.dataInterval = [self.SetDateToUnix(list(csv.reader(open(csvFile), delimiter=','))[1][0]),#time at begining of csv
								 self.SetDateToUnix(list(csv.reader(open(csvFile), delimiter=','))[csvRows - 1][0])]
		#add time at end of csv (subtract 1 from rows)
		print(Database.dataInterval[0])
		print(self.SetUnixToDate(Database.dataInterval[0]))



	def SetInterval(self, start, end):
		if (start < Database.dataInterval[0]):
			start = Database.dataInterval[0]
		if (end > Database.dataInterval[1]):
			end = Database.dataInterval[1]
		self.interval = [start, end]


	def SetUnixToDate(self, unix):#input unix time as string or int
		unix = int(unix) #gets rid of utc time difference of 10 hours
		return datetime.datetime.utcfromtimestamp(unix).strftime(' %m/%d/%Y %I:%M:%S %p')

	def SetDateToUnix(self, date):#input date string
		print(date)# the utc problem happens at the unix conversion
		utc = datetime.datetime.strptime(date, ' %m/%d/%Y %I:%M:%S %p')
		return int(utc.timestamp()) - 36000#unix is UTC time which is 10 hours ahead (36000 seconds)


	def AddBuilding(self, buildingIndex):#send the building by index of buildings list
		self.prospect.append(buildingIndex)

	def RemoveBuilding(self, buildingIndex):
		self.prospects.remove(buildingIndex)

		#we will only refer to buildings by their index in the list, never by name

	def ReadCSV(self):
		pass



#initializes an instance of database
database = Database('AnalyticsData_20181019174047.csv')#test csv
#building = Building(buildings[0])