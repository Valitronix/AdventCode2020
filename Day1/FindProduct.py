list_of_numbers = set()
with open('data') as my_data:
    for number in my_data.readlines():
        this_number = int(number.strip())
        list_of_numbers.add(this_number)
        need = 2020 - this_number
        if need in list_of_numbers:
            print("The two numbers are ", this_number, " and ", need, " and their product is ",  this_number * need)
            break