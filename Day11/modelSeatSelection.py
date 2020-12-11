def countNeighbors(seat_map, row, index):
    count = 0
    for ri in range(max(0, row-1),min(len(seat_map), row+2)):
        for ci in range(max(0, index-1),min(len(seat_map[0]), index+2)):
            #print("Checking row", ri, ", seat", ci, ", which is a", seat_map[ri][ci])
            if ri == row and ci == index:
                #print("whoops that's the current cell")
                continue
            elif seat_map[ri][ci] == '#':
                # print("it's a #! count++ ")
                count += 1
            #print("it's a", seat_map[ri][ci])
    return count

def goOneRound(seat_map, new_map):
    for ri, row in enumerate(seat_map):
        for ci, chair in enumerate(row):
            #print("Checking row", ri, ", seat", ci, "which is a", chair)
            if chair == 'L' and countNeighbors(seat_map, ri, ci) == 0:
                #print("No neighbors, changing to #")
                new_map[ri][ci] = '#'
            elif chair == '#' and countNeighbors(seat_map, ri, ci) >= 4:
                #print("Too many neighbors, changing to L")
                new_map[ri][ci] = 'L'
            else:
                new_map[ri][ci] = chair
    return new_map # [''.join(row) for row in new_map]

def countOccupiedSeats(seat_map):
    count = 0
    for row in seat_map:
        for chair in row:
            if chair == '#':
                count += 1
    return count 

with open('data') as my_data:
    str_seat_map = my_data.read().splitlines()
    seat_map = [list(row) for row in str_seat_map]

new_map = [[''] * len(seat_map[0]) for _ in range(len(seat_map))]
new_map = goOneRound(seat_map, new_map)
iter_count = 1

# print("After", iter_count, "iterations, the seat map is:")
# print('\n'.join([''.join(row) for row in new_map]))
while new_map != seat_map:
    seat_map = new_map.copy()
    new_map = [[''] * len(seat_map[0]) for _ in range(len(seat_map))]
    # print("Starting with seat map:")
    # print('\n'.join([''.join(row) for row in seat_map]))
    new_map = goOneRound(seat_map, new_map)
    iter_count += 1

print("After", iter_count, "iterations, the seat map is:")
print('\n'.join([''.join(row) for row in new_map]))

print("The number of occupied chairs is", countOccupiedSeats(seat_map))

# print(len(seat_map))
# print(seat_map[0][2])
# print('\n'.join(seat_map))