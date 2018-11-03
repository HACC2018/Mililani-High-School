class DataPoint:

    def __init__(self):#store timeStamp as a unix timestamp
        self.timestamp = 0
        self.kilowatts = 0


class Building:

    def __init__(self):
        self.dataPoints = []