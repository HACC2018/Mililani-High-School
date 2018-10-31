import matplotlib.pyplot as plt 

class DataPoint:

    def __init__(self, date, time, kilowatts):
        self.date = date
        self.time = time
        self.kilowatts = kilowatts
    def plotting(self):

        plt.plot(self.time, self.kilowatts)
        plt.xlabel('Months')
        plt.ylabel('Kilowatts')



class Building(DataPoint):

    def __init__(self, name, dataPoints):
        self.name = name
        self.dataPoints = dataPoints


class Campus(Building):

    def __init__(self, name, buildings):
        self.name = name
        self.buildings = buildings

