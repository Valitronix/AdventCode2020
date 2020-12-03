counter = 0
column = 0
with open('data') as my_data:
    for map_line in my_data.readlines():
        trimmed_map = map_line.strip()
        if trimmed_map[column] == '#':
            counter += 1
        column += 3
        column %= len(trimmed_map)
print(counter)
