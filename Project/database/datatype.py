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


<<<<<<< HEAD:Project/data.py
=======
campus = Campus(0,0)
>>>>>>> 8f866b828064af5c52160e7b9bcc36cea914415d:Project/database/datatype.py
