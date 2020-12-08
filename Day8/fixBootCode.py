#get all the instructions into a list
with open('data') as my_data:
    instructions = my_data.read().splitlines()
found = False
for index, potential_bug in enumerate(instructions):
    saved = instructions[index]
    if potential_bug[0:3] == 'nop':
        instructions[index] = potential_bug.replace('nop', 'jmp')
    elif potential_bug[0:3] == 'jmp':
        instructions[index] = potential_bug.replace('jmp', 'nop')
    
    accumulator = 0
    line = 0
    visited = set()
    # start at line 0
    while line not in visited:
        visited.add(line)
        if line >= len(instructions):
            found = True
            print("Exited boot instructions!")
            break
        elif instructions[line][0:3] == 'nop':
            line += 1
        elif instructions[line][0:3] == 'acc':
            accumulator += int(instructions[line][4:])
            line += 1
        elif instructions[line][0:3] == 'jmp':
            line += int(instructions[line][4:])
        else:
            print("There is an error, instruction: ", instructions[line], "at line", line)
    if found:
        break
    else:
        instructions[index] = saved
print(accumulator)