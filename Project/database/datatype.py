class DataPoint:

    def __init__(self):
        self.date = date
        self.time = time
        self.kilowatts = kilowatts


class Building:

    def __init__(self):
        self.name = name
        self.dataPoints = dataPoints


class Campus:

    def __init__(self, name, buildings):
        print("CAMPUS")
        self.name = name
        self.buildings = buildings


campus = Campus(0,0)