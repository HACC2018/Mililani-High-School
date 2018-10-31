import csv

with open('AnalyticsData_20181019174047.csv') as csvData: #Open test CSV as object "csvData"
    csvReader = csv.reader(csvData, delimiter=',')
    data = list(csvReader) #Cast CSV reader output to 2d list
    buildingNum = len(data[0]) - 1 #Take length of 2d array row and subtract one (for time collumn) to find # of buildings
    print(buildingNum)
