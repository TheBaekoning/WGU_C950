import truck


def main():
    packages = [0, 1, 2]
    truck1 = truck.TruckObject(packages)

    # truck 1
    while len(packages) > 0:
        packages.pop(truck1.deliver_closest())
        print(truck1.total_miles)
        print(packages)

    print(truck1.total_miles)
    print(truck1.current_time.current)


main()
