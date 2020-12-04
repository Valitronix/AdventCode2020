import re
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_passport(passport):

    return all([check_byr(passport), 
                check_iyr(passport), 
                check_eyr(passport), 
                check_pid(passport),
                check_ecl(passport),
                check_hcl(passport),
                check_hgt(passport)])

def check_byr(passport):
    try:
        length_check = (len(passport['byr']) == 4)
        date_check = (1920 <= int(passport['byr']) <= 2002)
    except:
        length_check = False
        date_check = False
    return length_check and date_check

def check_iyr(passport):
    try:
        length_check = (len(passport['iyr']) == 4)
        date_check = (2010 <= int(passport['iyr']) <= 2020)
    except:
        length_check = False
        date_check = False
    return length_check and date_check

def check_eyr(passport):
    try:
        length_check = (len(passport['eyr']) == 4)
        date_check = (2020 <= int(passport['eyr']) <= 2030)
    except:
        length_check = False
        date_check = False
    return length_check and date_check

def check_pid(passport):
    try:
        length_check = (len(passport['pid']) == 9)
    except:
        length_check = False
    return length_check

def check_ecl(passport):
    try:
        color_check = any(color == passport['ecl'] for color in eye_colors)
    except:
        color_check = False
    return color_check

def check_hcl(passport):
    try:
        regex = re.compile("#[0-9a-f]{6}")
        color_check = (regex.search(passport['hcl']) is not None)
    except:
        color_check = False
    return color_check

def check_hgt(passport):
    try:
        height_string = passport['hgt']
        if height_string.find("cm") >= 0:
            try:
                height_cm = int(height_string[:height_string.find("cm")])
            except:
                height_cm = 0
            height_check = 150 <= height_cm <= 193
        elif height_string.find("in") >= 0:
            try:
                height_in = int(height_string[:height_string.find("in")])
            except:
                height_in = 0
            height_check = 59 <= height_in <= 76
        else:
            height_check = False
    except:
        height_check = False

    return height_check