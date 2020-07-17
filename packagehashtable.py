import csv
from dataclasses import dataclass


class HashTable:
    def __init__(self):
        self.table = []
        for i in range(40):
            self.table.append([])

    def insert(self, item):
        bucket = item.get_id() - 1
        self.table[bucket].append(item)


class PackageHashTable:
    hash_table: HashTable

    def __init__(self):
        self.hash_table = HashTable()
        with open('package.csv', newline='\n') as package_reader:
            reader = csv.reader(package_reader)
            for row in reader:
                row[0] = int(row[0])
                x = PackageObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                self.hash_table.insert(x)

    def get_table(self):
        return self.hash_table

    def look_up(self, id: int):
        return self.hash_table.table[id - 1][0]

    def print_table(self):
        index = 0
        while (index < 40):
            print("Package ID: ", self.hash_table.table[index][0].id_num, " | Address: ",
                  self.hash_table.table[index][0].address, " | City: ", self.hash_table.table[index][0].city,
                  " | State: ",
                  self.hash_table.table[index][0].state, " | Zip: ", self.hash_table.table[index][0].zip,
                  " | Deadline: ", self.hash_table.table[index][0].deadline, " | Weight: ",
                  self.hash_table.table[index][0].weight, " | Status: ", self.hash_table.table[index][0].status)
            index = index + 1


@dataclass
class PackageObject:
    id_num: int
    deadline: str
    address: str
    city: str
    state: str
    zip: str
    weight: str
    status: str

    def __init__(self, id_num, address, city, state, zip, deadline, weight, status):
        self.id_num = id_num
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
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
