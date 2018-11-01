import csv

csvReader = csv.reader(open("AnalyticsData_20181019174047.csv"), delimiter=",")

data = list(csvReader)[0]
i = 0

while data[0] != " 3/6/2018 7:00:00 PM":
	i += 1
	print(i)
	csvReader = csv.reader(open("AnalyticsData_20181019174047.csv"), delimiter=",")
	data = list(csvReader)[i]

print(data)
