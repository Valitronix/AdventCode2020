
def runMask(address, mask): #take int address in
    binary_addr = format(address, '#038b') #convert in address to binary string
    count_Xs = sum([1 if x=='X' else 0 for x in mask]) #how many floats determines how many output addresses
    inv_count_Xs = 0 # tool for below
    count_floats = pow(2, count_Xs) # 3 floats means 2^3 = 8 output addresses
    output_addrs = [['']*36 for _ in range(count_floats)] # 2D array of output addresses, each 36 bits long
    for idx in range(0,36): # going through the mask
        if mask[idx] =='0':
            overwrite = [binary_addr[idx+2]] * count_floats # keep original address bit for all output addresses
        elif mask[idx] == '1':
            overwrite = ['1'] * count_floats # overwrite with 1 for all addresses
        else: # need combination of 0 and 1.
            # The first of 3 Xs will be replaced with 2^2 0s then 2^2 1s, 2^0 times
            # The second X will be replaced with 2^1 0s then 2^1 1s, 2^1 times
            # The third X will be replaced with 2^0 0s then 2^0 1s, 2^2 times
            # and so on...
            overwrite = ('0' * pow(2, count_Xs-1) + '1' * pow(2, count_Xs-1)) * pow(2, inv_count_Xs)
            count_Xs -= 1 
            inv_count_Xs += 1
        #print("overwrite values are:")
        #print(overwrite)
        for index in range(0,count_floats):
            output_addrs[index][idx] = overwrite[index] #write the output bit to each output address
    return [int(''.join(addr), 2) for addr in output_addrs]

with open('data') as input_data:
    instructions = input_data.readlines()

memory = {}#[0] * 65536
for instruction in instructions:
    if instruction[:4] == 'mask':
        mask = instruction[7:]
    else:
        stop = instruction.find(']')
        #print('Assigning new value', int(instruction[stop+4:]), "to these addresses:")
        #print(runMask(int(instruction[4:stop]), mask))
        for addr in runMask(int(instruction[4:stop]), mask):
            memory[addr] = int(instruction[stop+4:])

#print(memory[0:30])
print("The sum of all memory values is", sum(memory.values()))
