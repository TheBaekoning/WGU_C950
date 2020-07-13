import datetime


class DeliveryTime:
    def __init__(self):
        self.current = datetime.timedelta(0, 0, 0, 0, 0, 8, 0)

    def add_minutes(self, minutes):
        self.current = self.current + datetime.timedelta(0, 0, 0, 0, minutes, 0, 0)

    def print_current(self):
        print(self.current)
