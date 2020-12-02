counter = 0
with open('data') as my_data:
    for entry in my_data.readlines():
        [limits, letter, password] = entry.split(' ')
        [lower, upper] = limits.split('-')
        password = password.strip()
        if password.count(letter[0]) >= int(lower) and password.count(letter[0]) <= int(upper):
            counter = counter + 1
print(counter)



