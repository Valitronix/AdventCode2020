with open('testData') as my_data:
    earliest_departure = int(my_data.readline())
    # buses = my_data.readline().split(',')
    buses_input = my_data.readline().split(',')

bus_dict = {}
max_bus = 0
# indexes = []
# buses = []
for i,b in enumerate(buses_input):
    if b != 'x':
        bus_dict{i} = b
        # indexes.append(i)
        # buses.append(int(b))
#indexes = [i - indexes[buses.index(max(bus_dict))] for i in bus_dict.keys()]
#print(indexes)
#print("Shifting index 0 to max bus ID", max(buses), "which is at index", buses.index(max(buses)), "and will now be index 0")
departures = [False] * len(bus_dict)

t = 0
while not all(departures):
    # if t == 100000000000000:
    #     print("Made it")
    for bus in enumerate(bus_dict):
        if (t + indexes[idx]) % bus == 0:
            departures[idx] = True
            continue
        else:
            departures = [False] * len(buses)
            break
    t += max(buses)
#     bus_no = int(bus)
#     bus_times = [a for a in range(0, earliest_departure + bus_no, bus_no) if a >= earliest_departure]
#     departures[index] = bus_times[0]

print("The soonest the buses depart in order is", t - max(buses) + indexes[0])
# print("The bus ID is", buses[departures.index(min(departures))])
# print("The answer is", int(buses[departures.index(min(departures))]) * (min(departures)-earliest_departure))
