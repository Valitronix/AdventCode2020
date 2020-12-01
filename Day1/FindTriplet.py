list_of_numbers = set()
with open('data') as my_data:
    for number in my_data.readlines():
        this_number = int(number.strip())
        list_of_numbers.add(this_number)
        need = 2020 - this_number
        for second_num in list_of_numbers:
            if second_num == this_number:
                break
            try_need = need - second_num
            if try_need in list_of_numbers:
                print("The three numbers are ", this_number, ", ", second_num, ", and ", try_need, " and their product is ",  this_number * second_num * try_need)
                break