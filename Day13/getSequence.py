with open('data') as my_data:
    earliest_departure = int(my_data.readline())
    # buses = my_data.readline().split(',')
    buses_input = my_data.readline().split(',')

indexes = []
buses = []
for i,b in enumerate(buses_input):
    if b != 'x':
        indexes.append(i)
        buses.append(int(b))
indexes = [i - indexes[buses.index(max(buses))] for i in indexes]
print(indexes)
print("Shifting index 0 to max bus ID", max(buses), "which is at index", buses.index(max(buses)), "and will now be index 0")
departures = [False] * len(buses)
t = 100000000000000
#t = 0
while not all(departures):
    for idx, bus in enumerate(buses):
        # if bus == 'x':
        #    departures[index] = True
        #    continue
        # elif (t + index) % int(bus) == 0:
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
