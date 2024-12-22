tram_arriving_in_min = input("In how many minutes is the tram coming ? ")
bus_arriving_in_min = input("In how many minutes is the bus coming in ? ")
print("tram is ariving in " + tram_arriving_in_min + " min")
print("bus is ariving in " + bus_arriving_in_min + " min")
if tram_arriving_in_min <= bus_arriving_in_min:
    print("i will wait at the tram stop ")
else:
    print("i will wait at the bus stop ")