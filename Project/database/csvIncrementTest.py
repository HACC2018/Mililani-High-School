import csv

with open('AnalyticsData_20181019174047.csv') as csvData: #Open test CSV as object "csvData"
    csvReader = csv.reader(csvData, delimiter=',')

    i = 1 #init value for increment
    data = list(csvReader)[1] #save first row as data

    while data != "5/15/2018 4:45:00 AM": #keep going down rows until row matching time is found
    	i = i + 1 #increment row
    	#csvReader.__next__() #not sure if needed
    	data = list(csvReader)[i] #save new row
    
    print(data) #print row with time


   '''
   File "csvIncrementTest.py", line 12, in <module>
   data = list(csvReader)[i] #save new row
   IndexError: list index out of range
   '''