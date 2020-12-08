#get all the instructions into a list
with open('data') as my_data:
    instructions = my_data.read().splitlines()

accumulator = 0
line = 0
visited = set()
# start at line 0
while line not in visited:
    visited.add(line)
    if instructions[line][0:3] == 'nop':
        line += 1
    elif instructions[line][0:3] == 'acc':
        accumulator += int(instructions[line][4:])
        line += 1
    elif instructions[line][0:3] == 'jmp':
        line += int(instructions[line][4:])
    else:
        print("There is an error, instruction: ", instructions[line], "at line", line)

print(accumulator)