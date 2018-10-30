import csv

with open('AnalyticsData_20181019174047.csv') as csvData:
    csvReader = csv.reader(csvData, delimiter=',')
    data = list(csvReader)
    buildingNum = len(data[0]) - 1
    print(buildingNum)
