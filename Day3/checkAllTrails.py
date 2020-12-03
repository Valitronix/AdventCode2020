counters = [0] * 4
columns = [0] * 4
slopes = [1, 3, 5, 7]

steep_counter = 0
steep_column = 0
steep_slope = 1
steep_toggle = True
with open('data') as my_data:
    for map_line in my_data.readlines():
        trimmed_map = map_line.strip() #trim the \n character
        for index, trail in enumerate(counters): # for each trail (except steepest)
            if trimmed_map[columns[index]] == '#': # check the correct column
                counters[index] += 1 # increment the corresponding counter
            columns[index] += slopes[index]
            columns[index] %= len(trimmed_map)
        if steep_toggle: #if this is a steep slope row
            if trimmed_map[steep_column] == '#':
                steep_counter += 1
            steep_column += steep_slope
            steep_column %= len(trimmed_map)
        steep_toggle = not steep_toggle
print(counters, steep_counter)
