import passportValidity

valid = 0
fieldnames = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid'
passport = {} #dict.fromkeys(fieldnames,'')
with open('data') as my_data:
    for entry in my_data.read().splitlines():       #for each line of text
        if entry:                                   #if the line has text
            #update fields in current passport      
            for key_val in entry.split():           #for each key-value pair in the line
                key, value = key_val.split(':')     #separate key and value
                passport[key] = value               #add key:value to the current passport
            # check if all necessary fields are populated 
            if passportValidity.check_passport(passport):
                valid += 1                          #count another valid passport
                print("Valid passport: ", passport)
                passport = {} #dict.fromkeys(fieldnames,'')
            # if all(keys in passport.keys() for keys in fieldnames): #if all the keys listed in fieldnames are present in the current passport's keys
            #     valid += 1                          #count another valid passport
            #     print("Valid passport: ", passport)
            #     passport = {} #dict.fromkeys(fieldnames,'')

        else:                                       #if the line is empty, new passport
            #reset, new passport
            passport = {} #dict.fromkeys(fieldnames,'')

    print("There are ", valid, " valid passports")