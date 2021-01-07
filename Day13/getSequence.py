with open('data') as my_data:
    earliest_departure = int(my_data.readline())
    buses_input = my_data.readline().split(',')

indexes = []
buses = []
for i,b in enumerate(buses_input):
    if b != 'x':
        indexes.append(i)
        buses.append(int(b))
highest = max(buses)
no_buses = len(buses)
indexes = [i - indexes[buses.index(highest)] for i in indexes]
print(indexes)
print("Shifting index 0 to max bus ID", highest, "which is at index", buses.index(highest), "and will now be index 0")
departures = [False] * no_buses

t = 100000000000000
while not all(departures):
    for idx in range(no_buses):
        if (t + indexes[idx]) % buses[idx] == 0:
            departures[idx] = True
        else:
            departures = [False] * no_buses
            break
    t += highest

print("The soonest the buses depart in order is", t - max(buses) + indexes[0])
