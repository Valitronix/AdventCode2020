window = 25
preamble = 25

def findSumValues(candidate_numbers, sum_number):
    for number in candidate_numbers:
        need = int(sum_number) - int(number)
        #print("let's check", number, "and", need)
        if (str(need) in candidate_numbers) and (str(need) != number):
            #print("The two numbers are ", number, " and ", need)
            return True
    return False

def findContiguousSum(candidate_numbers, sum_number):
    for index, number in enumerate(candidate_numbers):
        contiguous_sum = int(number)
        number_of_numbers = 1
        while contiguous_sum <= int(sum_number):
            if contiguous_sum == int(sum_number):
                print("If you add up", number_of_numbers, "numbers starting at", number, "at index", index, "you get", sum_number)
                return [index, number_of_numbers]
            else:
                contiguous_sum += int(candidate_numbers[index+number_of_numbers])
                number_of_numbers += 1
    print("Could not find contiguous sum")
    return [0,0]

with open('data') as my_data:
    all_data = my_data.read().splitlines()

for index, number in enumerate(all_data[preamble:]):
    index += preamble
    #print("Checking for two numbers between indexes", index-window, "and", index, "which sum to", number)
    if findSumValues(all_data[index-window:index], number):
        continue
    else:
        special_number = int(number)
        special_index = index
        print("For value ", number, " at index ", index, ", there are no two different numbers in the preceding ", window, " values which sum to ", number)
        break

[first_number, how_many_numbers] = findContiguousSum(all_data[0:special_index], special_number)
print("If you sum the numbers", all_data[first_number], "through", all_data[first_number+how_many_numbers-1], "you'll get", special_number)
print("The minimum of these numbers is", min(all_data[first_number:first_number+how_many_numbers]), "and the max of these numbers is", max(all_data[first_number:first_number+how_many_numbers]), "and they sum to", int(min(all_data[first_number:first_number+how_many_numbers])) + int(max(all_data[first_number:first_number+how_many_numbers])))

