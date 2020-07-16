import decimal

import distancetable
import packagehashtable
import timeconverter


class TruckObject:
    package_list = []
    total_miles: float
    current_location = str

    def __init__(self, packages):
        self.package_list = packages
        self.current_location = "4001 South 700 East"
        self.total_miles = decimal.Decimal(0)
        self.current_time = timeconverter.DeliveryTime(8, 0)

    def deliver_closest(self):
        current_index = 0
        closest_location = decimal.Decimal(0)
        for package in self.package_list:
            x = distancetable.DistanceList().location_id(self.current_location)
            y = distancetable.DistanceList().location_id(packagehashtable.PackageHashTable().look_up(package).address)
            if closest_location == 0:
                closest_location = distancetable.DistanceList().get_distance(x, y)
            else:
                if closest_location > distancetable.DistanceList().get_distance(x, y):
                    closest_location = distancetable.DistanceList().get_distance(x, y)
                    current_index = packagehashtable.PackageHashTable().look_up(package).id_num - 1

        self.current_time.add_minutes_by_miles(closest_location)
        self.total_miles = self.total_miles + closest_location
        print(self.current_time.current)
        return current_index
