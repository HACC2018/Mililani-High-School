import matplotlib.pyplot as plt 

class DataPoint:

    def __init__(self, timestamp, kilowatts):#store timeStamp as a unix timestamp
        self.timestamp = timestamp
        self.kilowatts = kilowatts
    def plotting(self):

        plt.plot(self.time, self.kilowatts)
        plt.xlabel('Months')
        plt.ylabel('Kilowatts')



class Building:

    def __init__(self):
        self.name = name
        self.dataPoints = dataPoints


class Campus:

    def __init__(self, name, buildings):
        self.name = name
        self.buildings = buildings