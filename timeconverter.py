import datetime


class DeliveryTime:
    def __init__(self, start_hour, start_minute):
        self.current = datetime.timedelta(0, 0, 0, 0, start_minute, start_hour, 0)

    def add_minutes(self, minutes):
        self.current = self.current + datetime.timedelta(0, 0, 0, 0, minutes, 0, 0)

    def add_minutes_by_miles(self, miles):
        miles = miles/18
        minutes = miles * 60
        self.current = self.current + datetime.timedelta(0, 0, 0, 0, float(minutes), 0, 0)

    def print_current(self):
        print(self.current)

    def get_current(self):
        return self.current
