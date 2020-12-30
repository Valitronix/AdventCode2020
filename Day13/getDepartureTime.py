with open('data') as my_data:
    earliest_departure = int(my_data.readline())
    # buses = my_data.readline().split(',')
    buses = list(filter(lambda a: a != 'x', my_data.readline().split(',')))

departures = [0] * len(buses)
for index, bus in enumerate(buses):
    bus_no = int(bus)
    bus_times = [a for a in range(0, earliest_departure + bus_no, bus_no) if a >= earliest_departure]
    departures[index] = bus_times[0]

print("The soonest departure after", earliest_departure, "is", min(departures), "which is a", min(departures)-earliest_departure, "minute wait")
print("The bus ID is", buses[departures.index(min(departures))])
print("The answer is", int(buses[departures.index(min(departures))]) * (min(departures)-earliest_departure))
