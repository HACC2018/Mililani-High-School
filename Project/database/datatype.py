import matplotlib.pyplot as plt 

class DataPoint:

    def __init__(self, timestamp, kilowatts):#store timeStamp as a unix timestamp
        self.timestamp = timestamp
        self.kilowatts = kilowatts


class Building:

    def __init__(self):
        self.dataPoints = []