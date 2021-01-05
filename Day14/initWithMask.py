
def runMask(data_val, mask):
    binary_data = format(data_val, '#038b')
    output_data = ['']*36
    for idx in range(0,36):
        if mask[idx] =='X':
            output_data[idx] = binary_data[idx+2]
        else:
            output_data[idx] = mask[idx]
    return int(''.join(output_data), 2)

with open('data') as input_data:
    instructions = input_data.readlines()

memory = [0] * 65536
for instruction in instructions:
    if instruction[:4] == 'mask':
        mask = instruction[7:]
    else:
        stop = instruction.find(']')
        #print("Assigning new value", int(instruction[stop+4:]), "to memory address", int(instruction[4:stop]))
        memory[int(instruction[4:stop])] = runMask(int(instruction[stop+4:]), mask)

#print(memory[0:12])
print("The sum of all memory values is", sum(memory))
