import datatype#imports our local file datatype.py

import datetime
import calendar
import time

class Database():

	buildings = []
	dataInterval = []
	#time is handled in int(unix timestamp) form (make sure you convert to int)

	def __init__(self):
		#look through the csv and add each building a list
		#in the same loop get the earliest timstamp and latest

		Database.buildings = []#total buildings list
		Database.dataInterval = [] #[startTime, endTime]
		self.prospects = []#we will append building indexes to this
		#For example prospects could equal [1,4,2,6], these refer to the 
		#index of those builings we want to look at. This makes it so
		#that we only need to store the int of its index vs the entire instance


	def SetInterval(self, start, end):
		if (start < Database.dataInterval[0]):
			start = Database.dataInterval[0]
		if (end > Database.dataInterval[1]):
			end = Database.dataInterval[1]
		self.interval = [start, end]


	def SetUnixToDate(self, unix):#input unix time as string or int
		unix = int(unix) #makes it an int
		return print(datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %I:%M:%S %p'))

	def SetDateToUnix(sef, date):#input date string
		return calendar.timegm(date.utctimetuple())


	def AddBuilding(self, buildingIndex):#send the building by index of buildings list
		self.prospect.append(buildingIndex)

	def RemoveBuilding(self, buildingIndex):
		self.prospects.remove(buildingIndex)

		#we will only refer to buildings by their index in the list, never by name


#initializes an instance of database
database = Database()