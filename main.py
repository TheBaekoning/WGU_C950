from packagehashtable import PackageObject
from packagehashtable import PackageHashTable

def main():
    print("Hello world!")
    x = PackageObject(1, "10:00 AM", "Test Address", "Test City", "Test State", 11111, 10, "At Hub")
    x.print()
    print("TEST", x.get_id(), x.address)
    print(x.id_num)
    y = PackageHashTable()
    y.insert(x)
    print(y.table[0][0].address)
    x = PackageObject(2, "10:0022 AM", "Test Address22", "Test City22", "Test State", 11111, 10, "At Hub")
    y.insert(x)
    print(y.table[1][0].address)






main()
