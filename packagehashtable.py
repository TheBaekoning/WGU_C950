from dataclasses import dataclass


class PackageHashTable:
    _container = {}

    def __init__(self):
        self.table = []
        for i in range(40):
            self.table.append([])

    def insert(self, item):
        bucket = item.get_id() - 1
        self.table[bucket].append(item)

@dataclass
class PackageObject:
    id_num: int
    deadline: str
    address: str
    city: str
    state: str
    zip: int
    weight: int
    status: str

    def __init__(self, id_num, deadline, address, city, state, zip, weight, status):
        self.id_num = id_num
        self.deadline = deadline
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.weight = weight
        self.status = status

    def setstatus(self, new_status):
        self.status = new_status

    def print(self):
        print("Package ID: ", self.id_num, " | Address: ", self.address, " | City: ", self.city, " | State: ",
              self.state, " | Zip: ", self.zip,
              " | Deadline: ", self.deadline, " | Weight: ", self.weight, " | Status: ", self.status)

    def get_id(self):
        return self.id_num





