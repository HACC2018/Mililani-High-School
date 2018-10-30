class DataPoint:

    def __init__(self, date, time, kilowatts):
        self.date = date
        self.time = time
        self.kilowatts = kilowatts


class Building:

    def __init__(self, name, dataPoints):
        self.name = name
        self.dataPoints = dataPoints


class Campus:

    def __init__(self, name, buildings):
        self.name = name
        self.buildings = buildings
