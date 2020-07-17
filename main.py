import packagehashtable
import truck


def main():
    packages1 = [8, 9, 22, 23, 24, 26, 27, 28, 33, 35, 39]
    packages1priority = [1, 2, 4, 5, 7, 11, 12, 21, 30, 31, 34, 37, 40]
    packages2 = [3, 6, 18, 25, 32, 38]
    packages2priority = [10, 13, 14, 15, 16, 17, 19, 20, 29, 36]
    truck1 = truck.TruckObject(packages1priority)
    truck2 = truck.TruckObject(packages2priority)
    package_info = packagehashtable.PackageHashTable()

    # truck 1 priority first
    while len(packages1priority) > 0:
        x = truck1.deliver_closest()
        truck1.current_location = package_info.get_table().table[packages1priority[x] - 1][0].address
        print("CURRENT LOCATION: " + truck1.current_location)
        package_info.get_table().table[packages1priority[x] - 1][0].status = "Package Delievered On: " + str(
            truck1.current_time.current) + " By Truck 1"
        print(package_info.get_table().table[packages1priority[x] - 1][0])
        print("CURRENT MILES: " + str(truck1.total_miles))
        packages1priority.pop(x)
        print('**********************************************************')
    truck1.return_hub()
    print("CURRENT MILES: " + str(truck1.total_miles))

    print('=============================================================')

    # truck 1 2nd run
    truck1.package_list = packages1
    while len(packages1) > 0:
        x = truck1.deliver_closest()
        truck1.current_location = package_info.get_table().table[packages1[x] - 1][0].address
        print("CURRENT LOCATION: " + truck1.current_location)
        package_info.get_table().table[packages1[x] - 1][0].status = "Package Delievered On: " + str(
            truck1.current_time.current) + " By Truck 1"
        print(package_info.get_table().table[packages1[x] - 1][0])
        print("CURRENT MILES: " + str(truck1.total_miles))
        packages1.pop(x)
        print('**********************************************************')
    print("CURRENT MILES: " + str(truck1.total_miles))

    print('=============================================================')

    # truck 2 priority first
    while len(packages2priority) > 0:
        x = truck2.deliver_closest()
        truck2.current_location = package_info.get_table().table[packages2priority[x] - 1][0].address
        print("CURRENT LOCATION: " + truck2.current_location)
        package_info.get_table().table[packages2priority[x] - 1][0].status = "Package Delievered On: " + str(
            truck2.current_time.current) + " By Truck 2"
        print(package_info.get_table().table[packages2priority[x] - 1][0])
        print("CURRENT MILES: " + str(truck2.total_miles))
        packages2priority.pop(x)
        print('**********************************************************')

    truck2.return_hub()
    print("CURRENT MILES: " + str(truck2.total_miles))
    print("CURRENT LOCATION: " + truck2.current_location)

    print('=============================================================')

    # truck 2 2nd load
    truck2.package_list = packages2
    while len(packages2) > 0:
        x = truck2.deliver_closest()
        truck2.current_location = package_info.get_table().table[packages2[x] - 1][0].address
        print("CURRENT LOCATION: " + truck2.current_location)
        package_info.get_table().table[packages2[x] - 1][0].status = "Package Delievered On: " + str(
            truck2.current_time.current) + " By Truck 2"
        print(package_info.get_table().table[packages2[x] - 1][0])
        print("CURRENT MILES: " + str(truck2.total_miles))
        packages2.pop(x)
        print('**********************************************************')

    print("CURRENT MILES: " + str(truck2.total_miles))

    print('=============================================================')

    print(package_info.print_table())
    print("TRUCK 1 TOTAL MILES: " + str(truck1.total_miles))
    print("TRUCK 2 TOTAL MILES: " + str(truck2.total_miles))


main()
