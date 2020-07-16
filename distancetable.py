import csv
import decimal

class DestinationObject:
    address: str


    def __init__(self, address, distance):
        self.address = address
        self.distance = decimal.Decimal(distance)


class AddressObject:
    address: str

    def __init__(self):
        self.destination = []

    def insert(self, destination_object: DestinationObject):
        self.destination.append(destination_object)


class DistanceList:
    def __init__(self):
        self.distance = []
        self.table = []
        with open('distance.csv', newline='\n') as package_reader:
            reader = csv.reader(package_reader, delimiter=',')
            for row in reader:
                self.table.append(row)
        with open('distancevalues.csv', newline='\n') as package_reader:
            reader = csv.reader(package_reader)
            for row in reader:
                self.distance.append(row)

    def get_distance(self, originId: int, destinationId: int):
        return decimal.Decimal(self.distance[originId][destinationId])

    def location_id(self, location_string):
        return self.table[0].index(location_string)
