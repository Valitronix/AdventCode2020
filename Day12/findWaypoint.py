import math

with open('data') as my_data:
    instructions = my_data.read().splitlines()

status = [0,0,1,10] # [ship N/S, ship E/W, waypoint N/S, waypoint E/W]
for command in instructions:
    if command[0] == 'F':
        status[0] += int(command[1:]) * status[2]
        status[1] += int(command[1:]) * status[3]
        # status[0] = status[0] - (int(command[1:]) * math.sin(math.radians(status[2])))
        # status[1] = status[1] + (int(command[1:]) * math.cos(math.radians(status[2])))
    elif command[0] == 'R':
        for i in range(0, int(command[1:]), 90):
            save_ns = status[2]
            save_ew = status[3]
            status[3] = save_ns
            status[2] = -save_ew
        # status[2] = (status[2] + int(command[1:])) % 360
    elif command[0] == 'L':
        for i in range(0, int(command[1:]), 90):
            save_ns = status[2]
            save_ew = status[3]
            status[3] = -save_ns
            status[2] = save_ew
        # status[2] = (status[2] - int(command[1:])) % 360
    elif command[0] == 'W':
        status[3] = status[3] - int(command[1:])
    elif command[0] == 'S':
        status[2] = status[2] - int(command[1:])
    elif command[0] == 'E':
        status[3] = status[3] + int(command[1:])
    elif command[0] == 'N':
        status[2] = status[2] + int(command[1:])
    
    
print("Final distance is N-S", status[0], "E-W", status[1], "Manhattan distance:", abs(status[0]) + abs(status[1]))

