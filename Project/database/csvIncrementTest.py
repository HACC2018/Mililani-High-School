import csv

with open('AnalyticsData_20181019174047.csv') as csvData: #Open test CSV as object "csvData"
    csvReader = csv.reader(csvData, delimiter=',')

    i = 0 #init value for increment
    data = list(csvReader) #save entire csv as data
    
    date = " " + input("Enter date: mm/dd/yy h:mm:ss AM/PM : ")

    while data[i][0] != date: #keep going down rows until row matching time is found
    	i = i + 1 #increment row
    	#print(i)
    
    print(data[i]) #print row with time
