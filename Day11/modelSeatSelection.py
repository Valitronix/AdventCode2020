def countNeighbors(seat_map, row, index):
    count = 0
    # check up
    look = 1
    while (row - look >= 0):
        if seat_map[row - look][index] == '#':
            count += 1
            #print("there is a chair above at row", row-look, "seat", index)
            break
        elif seat_map[row - look][index] == 'L':
            break
        else:
            look += 1
    
    # check up-right diagonal and seat_map[row - look][index + look] == '.'
    look = 1
    while (row - look >= 0) and (index + look < len(seat_map[0])):
        if seat_map[row - look][index + look] == '#':
            count += 1
            #print("there is a chair above-right at row", row-look, "seat", index+look)
            break
        elif seat_map[row - look][index + look] == 'L':
            break
        else:
            look += 1
    
    # check right 
    look = 1
    while (index + look < len(seat_map[0])):
        if seat_map[row][index + look] == '#':
            count += 1
            #print("there is a chair right at row", row, "seat", index+look)
            break
        elif seat_map[row][index + look] == 'L':
            break
        else:
            look += 1    

    # check down-right 
    look = 1
    while (row + look < len(seat_map)) and (index + look < len(seat_map[0])):
        if seat_map[row + look][index + look] == '#':
            count += 1
            #print("there is a chair below-right at row", row+look, "seat", index+look)
            break
        elif seat_map[row + look][index + look] == 'L':
            break
        else:
            look += 1

    # check down
    look = 1
    while (row + look < len(seat_map)):
        if seat_map[row + look][index] == '#':
            count += 1
            #print("there is a chair below at row", row+look, "seat", index)
            break
        elif seat_map[row + look][index] == 'L':
            break
        else:
            look += 1       

    # check down-left 
    look = 1
    while (row + look < len(seat_map)) and (index - look >= 0):
        if seat_map[row + look][index - look] == '#':
            count += 1
            #print("there is a chair below-left at row", row+look, "seat", index-look)
            break
        elif seat_map[row + look][index - look] == 'L':
            break
        else:
            look += 1

    # check left 
    look = 1
    while (index - look >= 0):
        if seat_map[row][index - look] == '#':
            count += 1
            #print("there is a chair left at row", row, "seat", index-look)
            break
        elif seat_map[row][index - look] == 'L':
            break
        else:
            look += 1

    # check up-left 
    look = 1
    while (row - look >= 0) and (index - look >= 0):
        if seat_map[row - look][index - look] == '#':
            count += 1
            #print("there is a chair above-left at row", row-look, "seat", index-look)
            break
        elif seat_map[row - look][index - look] == 'L':
            break
        else:
            look += 1
    
    # for ri in range(max(0, row-1),min(len(seat_map), row+2)):
    #     for ci in range(max(0, index-1),min(len(seat_map[0]), index+2)):
    #         if ri == row and ci == index:
    #             continue
    #         elif seat_map[ri][ci] == '#':
    #             count += 1
    return count

def goOneRound(seat_map, new_map):
    for ri, row in enumerate(seat_map):
        for ci, chair in enumerate(row):
            if chair == 'L' and countNeighbors(seat_map, ri, ci) == 0:
                new_map[ri][ci] = '#'
            elif chair == '#' and countNeighbors(seat_map, ri, ci) >= 5:
                new_map[ri][ci] = 'L'
            else:
                new_map[ri][ci] = chair

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
goOneRound(seat_map, new_map)
iter_count = 1

while new_map != seat_map:
    seat_map = new_map.copy()
    new_map = [[''] * len(seat_map[0]) for _ in range(len(seat_map))]
    goOneRound(seat_map, new_map)
    iter_count += 1

print("After", iter_count, "iterations, the seat map is:")
print('\n'.join([''.join(row) for row in new_map]))

print("The number of occupied chairs is", countOccupiedSeats(seat_map))

