counter = 0
with open('data') as my_data:
    for entry in my_data.readlines():
        [locs, letter, password] = entry.split(' ')
        [one, other] = locs.split('-')
        password = password.strip()
        if (password[int(one)-1] == letter[0]) ^ (password[int(other)-1] == letter[0]):
            counter = counter + 1
print(counter)
