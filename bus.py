busstop_reaching_time = int(input("How much time will it take you to reach bus stop ? "))
bus_282_arriving_time = int(input("In how many min is 282 ariving in ? "))
bus_182_arriving_time = int(input("In how many min is 182 ariving in ? "))
bus_from_perla = int(input("In how many min is the bus from perla ariving in ? "))
min_282_office = int(input("In how many min is 282 going to take reach office ? "))
min_182_perla = int(input("In how many min is 182 going to reach perla ? "))
perla_to_office_min = int(input("In how many min is the bus from perla going to reach office ? "))
route_1_time_min = busstop_reaching_time,bus_182_arriving_time,bus_from_perla,min_182_perla,perla_to_office_min
route_2_time_min = busstop_reaching_time,bus_282_arriving_time,min_282_office
print("bus 282 is ariving in ",str(bus_282_arriving_time)," min")
print("bus 182 is ariving in ",bus_182_arriving_time," min")
print("bus is ariving in ",bus_from_perla," min")
if route_1_time_min >= route_2_time_min :
    print("I will take 282 to reach office in ",str(route_2_time_min)," min")
else :
    print("I will take 182 to reach office in ",str(route_1_time_min)," min")